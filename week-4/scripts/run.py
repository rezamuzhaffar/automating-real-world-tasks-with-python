#! /usr/bin/env python3

import os
import requests

directory = "supplier-data/descriptions/"
dict = {}
content_format = ['name', 'weight', 'description']

for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as txtfile:
        reader = txtfile.read().split("\n")
        for i in range(len(content_format)):
            dict[content_format[i]] = reader[i]
        image_file = filename.replace('.txt', '.jpeg')
        dict['weight'] = int(dict['weight'].replace(' lbs', ''))
        dict['image_name'] = image_file
    response = requests.post("http://34.66.202.69/fruits/", json = dict)
    if not response.ok:
        raise Exception("POST failed with status code {}, file: {}".format(response.status_code, filename))
    print("POST {} success!".format(filename))