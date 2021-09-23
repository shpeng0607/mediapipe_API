from tqdm import tqdm
import pickle
import numpy as np
import json

part = ['train', 'val']
Train = pickle.load(open("SHREC/train.pkl", "rb"))
Test = pickle.load(open("SHREC/test.pkl", "rb"))
actionset = ['Grab', 'F Grab', 'Tap', 'F Tap', 'Expand', 'F Expand', 'Pinch', 'F Pinch', 'Rotation Clockwise',
             'F Rotation Clockwise', 'Rotation Counter Clockwise', 'F Rotation Counter Clockwise',
             'Swipe Right', 'F Swipe Right', 'Swipe Left', 'F Swipe Left', 'Swipe Up', 'F Swipe Up',
             'Swipe Down', 'F Swipe Down', 'Swipe X', 'F Swipe X', 'Swipe +', 'F Swipe +', 'Swipe V',
             'F Swipe V', 'Shake', 'F Shake']

for p in part:
    if p == 'train':
        count = 1
        now_action = 1
        for i in tqdm(range(len(Train['pose']))):
            data_list = []
            frameNum = 1
            for pose in Train['pose'][i]:
                skeletonlist = []
                list = []

                for num in range(1, 65, 3):
                    list.append(pose[num - 1].item())
                    list.append(pose[num + 1].item())
                    list.append(pose[num].item())

                skeletonlist.append(list)

                frame_dict = {
                    "frame_index": frameNum,
                    "skeleton": skeletonlist
                }

                json.dumps(frame_dict)
                data_list.append(frame_dict)
                frameNum = frameNum + 1


            json_dict = {
                "data": data_list,
                "label": actionset[Train['fine_label'][i] - 1],
                "label_index": int(Train['fine_label'][i] - 1)
            }

            # Serializing json
            json_object = json.dumps(json_dict, indent = 4)

            # Writing to sample.json
            if Train['fine_label'][i] != now_action:
                count = 1
                now_action = Train['fine_label'][i]
            outpath = "./JSON_data/SHREC_" + p + "/action" + str(Train['fine_label'][i]) + "_" + str(count) + ".json"
            count = count + 1
            with open(outpath, "w") as outfile:
                outfile.write(str(json_object))
    else:
        count = 1
        now_action = 1
        for i in tqdm(range(len(Test['pose']))):
            data_list = []
            frameNum = 1
            for pose in Test['pose'][i]:
                skeletonlist = []
                list = []

                for num in range(1, 65, 3):
                    list.append(pose[num - 1].item())
                    list.append(pose[num + 1].item())
                    list.append(pose[num].item())

                skeletonlist.append(list)

                frame_dict = {
                    "frame_index": frameNum,
                    "skeleton": skeletonlist
                }

                json.dumps(frame_dict)
                data_list.append(frame_dict)
                frameNum = frameNum + 1


            json_dict = {
                "data": data_list,
                "label": actionset[Test['fine_label'][i] - 1],
                "label_index": int(Test['fine_label'][i] - 1)
            }

            # Serializing json
            json_object = json.dumps(json_dict, indent = 4)

            # Writing to sample.json
            if Test['fine_label'][i] != now_action:
                count = 1
                now_action = Test['fine_label'][i]
            outpath = "./JSON_data/SHREC_" + p + "/action" + str(Test['fine_label'][i]) + "_" + str(count) + ".json"
            count = count + 1
            with open(outpath, "w") as outfile:
                outfile.write(str(json_object))
