# Welcome to HackLB/restaurant-closures

This repository is intended to mirror and archive the [restaurant closures list](http://www.longbeach.gov/health/inspections-and-reporting/inspections/restaurant-closures/) which the [Long Beach Health Department](http://www.longbeach.gov/health) publishes. We opted for JSON as a more convenient format for consuming and analyzing restaurant closure records, and git in order to maintain a historical record including changes over time to each case record.

This project is an activity of [HackLB](https://github.com/HackLB).

## Using this repo

### Clone it and go

You may easily [clone](https://github.com/HackLB/restaurant-closures.git) or [download](https://github.com/HackLB/restaurant-closures/archive/master.zip) the contents of this library using any git client (including the Github Web interface) to begin working with restaurant closures records in JSON format. The records are contained within the `_data` directory, organized by district number, with each restaurant closure record stored in a separate JSON file named according to a hash of its location.

### Maintaining your own mirror

If you'd rather download the current records yourself, I've included the same script `update.sh` I wrote to maintain this repo. Here's what you need to know.

#### Requirements

1. `Python 3.5+` (it should work on Python 2.7 but I haven't tested it)
4. Several Python packages installed with pip, documented in `requirements.txt`

#### How to Use update.sh

1. make a Python virtualenv for this project
2. `pip install -r requirements.txt` to satisfy dependencies
3. `./update.sh`

The script will create a `_data` directory if it doesn't already exist, and then save current JSON records in subdirectories. If you delete the contents of `_data` before running `update.py` you will get only current records.


### Contributing to this repo

Pull requests are welcome - if you have an idea for an improvement (for instance, porting `update.py` to another language) you're welcome to make it and open a PR, or open an issue first for discussion.

### Sample record

A typical record is shown below for reference:

```
{
    "address": "3424 64TH ST",
    "case_num": "CEAC224978",
    "description": "GARAGE BURNED AND THE DEBRIS IS STILL THERE; JUNK CARS IN YARD, AT LEAST ONE OF WHICH IS BURNED FROM THE GARAGE FIRE; JUNK IN BACK YARD. PEOPLE LIVING IN RV IN BACKYARD ON LEFT SIDE PLUGGED INTO HOUSE",
    "district": 9,
    "last_insp_date": "08/26/2016",
    "last_insp_type": "Pre-Citation Inspection",
    "start_date": "10/29/2015"
}
```