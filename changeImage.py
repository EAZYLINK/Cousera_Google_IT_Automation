#!/usr/bin/env python3
from PIL import Image
import os

path = "supplier-data/images/"

for file in os.listdir(path):
  if file.endswith(".tiff"):
    im = Image.open(path+file)
    new_im = im.convert("RGB").resize((600, 400))
    new_file = os.path.splitext(file)[0] + ".jpeg"
    new_im.save(os.path.join(path, new_file), "JPEG")
