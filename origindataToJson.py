import json
import os
from os import listdir
from os.path import isfile, isdir, join

part = ['train', 'val']
actionset = ["wipe", "spin", "hold"]
shrec_actionset = ['Grab', 'F Grab', 'Tap', 'F Tap', 'Expand', 'F Expand', 'Pinch', 'F Pinch', 'Rotation Clockwise',
                   'F Rotation Clockwise', 'Rotation Counter Clockwise', 'F Rotation Counter Clockwise',
                   'Swipe Right', 'F Swipe Right', 'Swipe Left', 'F Swipe Left', 'Swipe Up', 'F Swipe Up',
                   'Swipe Down', 'F Swipe Down', 'Swipe X', 'F Swipe X', 'Swipe +', 'F Swipe +', 'Swipe V',
                   'F Swipe V', 'Shake', 'F Shake']

for p in part:
    dictionary = {}
    path = "./JSON_data/SHREC_" + p
    fileList = os.listdir(path)

    for file in fileList:
        fname = file.split(".")[0]
        file_label = fname.split("_")[0].replace("action", "")
        datadict = {
            "has_skeleton": True,
            "label": shrec_actionset[int(file_label) - 1],
            "label_index": int(file_label) - 1
        }
        dictionary[fname] = datadict

    # Serializing json
    json_object = json.dumps(dictionary, indent = 4)

    # Writing to sample.json
    filepath = "./JSON_data/SHREC_" + p + "_label.json"
    with open(filepath, "w") as outfile:
        outfile.write(json_object)



# path = "./origin_data/action1"
# fileList = os.listdir(path)
# # Data to be written
# dictionary = {}
# labelName = "wipe" # spin
# labelNum = 0
# datadict = {
#     "has_skeleton": True,
#     "label": labelName,
#     "label_index": labelNum
# }

# for f in fileList:
#     fname = f.split(".")[0]
#     dictionary[fname] = datadict

# path = "./origin_data/action2"
# fileList = os.listdir(path)
# # Data to be written
# labelName = "spin"
# labelNum = 1
# datadict = {
#     "has_skeleton": True,
#     "label": labelName,
#     "label_index": labelNum
# }

# for f in fileList:
#     fname = f.split(".")[0]
#     dictionary[fname] = datadict

# path = "./origin_data/action3"
# fileList = os.listdir(path)
# # Data to be written
# labelName = "hold"
# labelNum = 2
# datadict = {
#     "has_skeleton": True,
#     "label": labelName,
#     "label_index": labelNum
# }

# for f in fileList:
#     fname = f.split(".")[0]
#     dictionary[fname] = datadict

# # Serializing json
# json_object = json.dumps(dictionary, indent = 4)

# # Writing to sample.json
# with open("./JSON_data/mediapipe_val_label.json", "w") as outfile:
#     outfile.write(json_object)