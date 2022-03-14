#! /usr/bin/env python3

import os
import requests

directory = "/data/feedback"
dict = {}
feedback_format = ["title", "name", "date", "feedback"]

for filename in os.listdir(directory):
  with open(os.path.join(directory, filename), "r") as file:
    reader = file.read().split("\n")
    for i in range(len(feedback_format)):
      dict[feedback_format[i]] = reader[i]
  response = requests.post("http://35.226.84.68/feedback/", json = dict)
  if not response.ok:
    raise Exception("POST failed with status code {}".format(response.status_code))
  print("ok.")
