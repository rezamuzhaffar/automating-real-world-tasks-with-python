#!/usr/bin/env python3

import os
from PIL import Image

# Assign directory
directory = "images"

# Iterate over files in directory
for filename in os.listdir(directory):
    if not filename.startswith('.'):
        file_path = os.path.join(directory, filename)
        im = Image.open(file_path)
        im.rotate(90).resize((128,128)).convert("RGB").save("/opt/icons/"+filename+".jpg")
