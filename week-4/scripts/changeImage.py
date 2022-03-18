#!/usr/bin/env python3

import os
from PIL import Image

# Assign directory
directory = "supplier-data/images/"

# Iterate over files in directory
for filename in os.listdir(directory):
  if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
    file_path = os.path.join(directory, filename)
    im = Image.open(file_path)
    file_split = filename.split(".")
    im.resize((600,400)).convert("RGB").save(directory+file_split[0]+".jpeg")