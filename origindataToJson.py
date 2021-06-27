import json
import os
from os import listdir
from os.path import isfile, isdir, join

part = ['train', 'val']
actionset = ["wipe", "spin", "hold"]

for p in part:
    dictionary = {}
    for action in actionset:
        path = "./origin_data/action" + str(actionset.index(action) + 1) + "/" + p
        fileList = os.listdir(path)
        # Data to be written
        datadict = {
            "has_skeleton": True,
            "label": action,
            "label_index": actionset.index(action)
        }

        for f in fileList:
            fname = f.split(".")[0]
            dictionary[fname] = datadict

    # Serializing json
    json_object = json.dumps(dictionary, indent = 4)

    # Writing to sample.json
    filepath = "./JSON_data/mediapipe_" + p + "_label.json"
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