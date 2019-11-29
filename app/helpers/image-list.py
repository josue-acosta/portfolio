import os
import json

image_list = []

# list all files in a directory using scandir()
basepath = '../static/images/grace-kelly'

with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            # use entry.name get name from scandir() object
            image_list.append(entry.name)

# create json file with names of images
with open(basepath + '/grace-kelly-images.json', 'w') as outfile:
    json.dump(image_list, outfile)