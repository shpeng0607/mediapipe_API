import json
import os
from os import listdir
from os.path import isfile, isdir, join

version = ['coarse', 'fine']
part = ['train', 'val']
actionset = ["wipe", "spin", "hold"]
shrec_actionset = ['Grab', 'F Grab', 'Tap', 'F Tap', 'Expand', 'F Expand', 'Pinch', 'F Pinch', 'Rotation Clockwise',
                   'F Rotation Clockwise', 'Rotation Counter Clockwise', 'F Rotation Counter Clockwise',
                   'Swipe Right', 'F Swipe Right', 'Swipe Left', 'F Swipe Left', 'Swipe Up', 'F Swipe Up',
                   'Swipe Down', 'F Swipe Down', 'Swipe X', 'F Swipe X', 'Swipe +', 'F Swipe +', 'Swipe V',
                   'F Swipe V', 'Shake', 'F Shake']
dhg_actionset = ['Grab', 'Tap',  'Expand', 'Pinch', 'Rotation Clockwise',
              'Rotation Counter Clockwise', 'Swipe Right', 'Swipe Left', 'Swipe Up', 
              'Swipe Down',  'Swipe X',  'Swipe +',  'Swipe V', 'Shake', 'F Grab',
              'F Tap', 'F Expand', 'F Pinch', 'F Rotation Clockwise', 'F Rotation Counter Clockwise',
              'F Swipe Right', 'F Swipe Left', 'F Swipe Up', 'F Swipe Down', 'F Swipe X', 'F Swipe +',
              'F Swipe V', 'F Shake']
# for p in part:
#     dictionary = {}
#     path = "./JSON_data/SHREC_" + p
#     fileList = os.listdir(path)

#     for file in fileList:
#         fname = file.split(".")[0]
#         file_label = fname.split("_")[0].replace("action", "")
#         datadict = {
#             "has_skeleton": True,
#             "label": dhg_actionset[int(file_label) - 1],
#             "label_index": int(file_label) - 1
#         }
#         dictionary[fname] = datadict

#     # Serializing json
#     json_object = json.dumps(dictionary, indent = 4)

#     # Writing to sample.json
#     filepath = "./JSON_data/SHREC_" + p + "_label.json"
#     with open(filepath, "w") as outfile:
#         outfile.write(json_object)

for i in range(1, 21):
    for v in version:
        for p in part:
            dictionary = {}
            path = "./JSON_data/DHG2016_" + str(i) + "/" + v + "/" + p
            fileList = os.listdir(path)

            for file in fileList:
                fname = file.split(".")[0]
                file_label = fname.split("_")[0].replace("action", "")
                datadict = {
                    "has_skeleton": True,
                    "label": dhg_actionset[int(file_label) - 1],
                    "label_index": int(file_label) - 1
                }
                dictionary[fname] = datadict

            # Serializing json
            json_object = json.dumps(dictionary, indent = 4)

            # Writing to sample.json
            filepath = "./JSON_data/DHG2016_"  + str(i) + "/" + v + "/DHG2016_" + str(i) + "_" + p + "_label.json"
            with open(filepath, "w") as outfile:
                outfile.write(json_object)
