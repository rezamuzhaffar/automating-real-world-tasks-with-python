#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
directory = "supplier-data/images/"

for file in os.listdir(directory):
    if file.lower().endswith('.jpeg'):
        with open(os.path.join(directory, file), 'rb') as opened:
            r = requests.post(url, files={'file': opened})