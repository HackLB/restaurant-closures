#!/usr/bin/env python
import os, sys
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import simplejson as json
import hashlib
import datetime

from geopy.geocoders import Nominatim, GoogleV3
from geopy.exc import GeocoderTimedOut


with open('../secrets.json') as f:    
    secrets = json.load(f)

geolocator = GoogleV3(api_key=secrets['google_api_key'])

url = 'http://www.longbeach.gov/health/inspections-and-reporting/inspections/restaurant-closures/'


def getmd5(message):    
    """
    Returns MD5 hash of string passed to it.
    """
    return hashlib.md5(message.encode('utf-8')).hexdigest()


def get_subdirectory(base_name):
    """
    Takes the base filename and returns a path to a subdirectory, creating it if needed.
    """
    # sub_dir = os.path.join(data_path)
    # os.makedirs(sub_dir, exist_ok=True)
    return data_path


def geocode(address_stub):
    address = '{}, LONG BEACH, CA'.format(address_stub)

    try:
        location = geolocator.geocode(address, timeout=2)
        if location:
            return {"latitude": location.latitude, "longitude": location.longitude, "address": location.address}
        else:
            return None
    except GeocoderTimedOut:
        return geocode(address)


def save_records(records):
    """
    Saves records to invidual JSON files.
    Records are per-address. Each new restaurant closure for 
    a given address gets appended to its existing file.
    Files are named and organized based on an MD5 of 
    the address.
    """
    print('Saving restaurant closure data...')
    for record in records:

        closure_key = '{}-{}-{}-{}'.format(record['name'], record['place'], record['closed'], record['reopened'])

        record_hash = getmd5(closure_key)
        file_name = '{}.json'.format(record_hash)
        directory = get_subdirectory(record_hash)

        path = os.path.join(directory, file_name)

        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump(record, f, indent=4, ensure_ascii=False, sort_keys=True)


def scrape_records():
    """
    Extracts restaurant closure records from the health department's
    restaurant closure Web page, then puts each record into a dictionary 
    and returns a list of dictionaries.
    """
    print('Getting restaurant closure data...')
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    rows = soup.find('table').find_all('tr')
    records = []
    for row in rows[1:]:
        cells = row.find_all('td')

        record = {}

        # get text and clean it
        location_text = str(cells[0]).replace('&amp;', '&').replace('<br/>', '\r\n').replace('<br />', '\r\n').replace('<td>', '').replace('<td colspan="1">','').replace('</td>', '').replace('<p>', '').replace('</p>', '').replace('\r\n\r\n', '\r\n').strip()

        location_items = [x.strip() for x in location_text.split('\r\n')]

        record['name'] = location_items[0]
        record['place'] = location_items[1]

        if not (record['name'].endswith('Truck') and record['place'].startswith('Lic #')):
            address = '{}, Long Beach, CA'.format(location_items[1])
            record['coordinates'] = geocode(address)

        record['closed'] = date_parse(cells[1].string.strip())
        record['reopened'] = date_parse(cells[2].string.strip())
        record['reason'] = cells[3].string.strip()

        records.append(record)
        pprint(record)

    return records

def date_parse(date_string):
    comp = date_string.split('/')
    m = int(comp[0])
    d = int(comp[1])
    y = int(comp[2]) + 2000
    date = datetime.datetime(y, m, d).isoformat()

    return date

if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.realpath(sys.argv[0])) # Path to current directory
    data_path = os.path.join(repo_path, '_data')               # Root path for record data
    os.makedirs(data_path, exist_ok=True)

    records = scrape_records()                  # Scrape restaurant closure records...
    save_records(records)                       # Save the scraped records to JSON files...

