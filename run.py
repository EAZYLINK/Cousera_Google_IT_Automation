#!/usr/bin/env python3

import requests
import os

fruits = {}
path = "supplier-data/descriptions/"
url = "http://34.123.22.5/fruits/"
for file in os.listdir(path):
  with open(path+file, 'r') as opened:
    line = opened.readlines()
    fruits["name"] = line[0].replace("\n", '')
    fruits["weight"] = int(line[1].replace(" lbs\n", ''))
    fruits["description"] = line[2].replace("\n", '')
    fruits["image_name"] = file.replace("txt", "jpeg")
  r = requests.post(url, data=fruits)
  print(r.status_code)
