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
    "closed": "2016-05-06T00:00:00",
    "coordinates": {
        "address": "141 E Willow St, Long Beach, CA 90806, USA",
        "latitude": 33.805574,
        "longitude": -118.190648
    },
    "name": "Papa John's Pizza",
    "place": "141 E. Willow St",
    "reason": "No Hot Water",
    "reopened": "2016-05-06T00:00:00"
}
```