#!/usr/bin/env bash

dtstamp=$(date +%Y%m%d_%H%M%S)
. ~/.virtualenvs/restaurant-closures/bin/activate

git pull
./restaurant-closures.py
git add -A
git commit -m "$dtstamp"
git push

deactivate