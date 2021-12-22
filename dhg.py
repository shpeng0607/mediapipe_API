from tqdm import tqdm
import pickle
import numpy as np
import json
import os

for testsplit in range(1, 21):
    part = ['train', 'val']
    Train = pickle.load(open("DHG1428/train" + str(testsplit) + ".pkl", "rb"))
    Test = pickle.load(open("DHG1428/test" + str(testsplit) + ".pkl", "rb"))

    actionset28 = ['Grab', 'Tap',  'Expand', 'Pinch', 'Rotation Clockwise',
                'Rotation Counter Clockwise', 'Swipe Right', 'Swipe Left', 'Swipe Up', 
                'Swipe Down',  'Swipe X',  'Swipe +',  'Swipe V', 'Shake', 'F Grab',
                'F Tap', 'F Expand', 'F Pinch', 'F Rotation Clockwise', 'F Rotation Counter Clockwise',
                'F Swipe Right', 'F Swipe Left', 'F Swipe Up', 'F Swipe Down', 'F Swipe X', 'F Swipe +',
                'F Swipe V', 'F Shake']

    actionset14 = ['Grab', 'Tap',  'Expand', 'Pinch', 'Rotation Clockwise',
                'Rotation Counter Clockwise', 'Swipe Right', 'Swipe Left',  'Swipe Up', 
                'Swipe Down',  'Swipe X',  'Swipe +',  'Swipe V', 'Shake']

    actionset28_count = [1]*28
    actionset14_count = [1]*14
    print(len(Train['pose'][1]))

    os.mkdir("./JSON_data/DHG2016_" + str(testsplit))
    os.mkdir("./JSON_data/DHG2016_" + str(testsplit) + "/fine/")
    os.mkdir("./JSON_data/DHG2016_" + str(testsplit) + "/fine/train")
    os.mkdir("./JSON_data/DHG2016_" + str(testsplit) + "/fine/val")
    os.mkdir("./JSON_data/DHG2016_" + str(testsplit) + "/coarse/")
    os.mkdir("./JSON_data/DHG2016_" + str(testsplit) + "/coarse/train")
    os.mkdir("./JSON_data/DHG2016_" + str(testsplit) + "/coarse/val")
    

    for p in part:
        if p == 'train':
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


                coarse_json_dict = {
                    "data": data_list,
                    "label": actionset14[Train['coarse_label'][i] - 1],
                    "label_index": int(Train['coarse_label'][i] - 1)
                }

                coarse_json_object = json.dumps(coarse_json_dict, indent = 4)

                outpath = "./JSON_data/DHG2016_" + str(testsplit) + "/coarse/" + p + "/action" + str(Train['coarse_label'][i]) + "_" + str(actionset14_count[Train['coarse_label'][i] - 1]) + ".json"
                actionset14_count[Train['coarse_label'][i] - 1] += 1
                with open(outpath, "w") as outfile:
                    outfile.write(str(coarse_json_object))

                fine_json_dict = {
                    "data": data_list,
                    "label": actionset28[Train['fine_label'][i] - 1],
                    "label_index": int(Train['fine_label'][i] - 1)
                }

                fine_json_object = json.dumps(fine_json_dict, indent = 4)

                outpath = "./JSON_data/DHG2016_" + str(testsplit) + "/fine/" + p + "/action" + str(Train['fine_label'][i]) + "_" + str(actionset28_count[Train['fine_label'][i] - 1]) + ".json"
                actionset28_count[Train['fine_label'][i] - 1] += 1
                with open(outpath, "w") as outfile:
                    outfile.write(str(fine_json_object))
        else:
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


                coarse_json_dict = {
                    "data": data_list,
                    "label": actionset14[Test['coarse_label'][i] - 1],
                    "label_index": int(Test['coarse_label'][i] - 1)
                }

                coarse_json_object = json.dumps(coarse_json_dict, indent = 4)

                outpath = "./JSON_data/DHG2016_" + str(testsplit) + "/coarse/" + p + "/action" + str(Test['coarse_label'][i]) + "_" + str(actionset14_count[Test['coarse_label'][i] - 1]) + ".json"
                actionset14_count[Test['coarse_label'][i] - 1] += 1
                with open(outpath, "w") as outfile:
                    outfile.write(str(coarse_json_object))

                fine_json_dict = {
                    "data": data_list,
                    "label": actionset28[Test['fine_label'][i] - 1],
                    "label_index": int(Test['fine_label'][i] - 1)
                }

                fine_json_object = json.dumps(fine_json_dict, indent = 4)

                outpath = "./JSON_data/DHG2016_" + str(testsplit) + "/fine/" + p + "/action" + str(Test['fine_label'][i]) + "_" + str(actionset28_count[Test['fine_label'][i] - 1]) + ".json"
                actionset28_count[Test['fine_label'][i] - 1] += 1
                with open(outpath, "w") as outfile:
                    outfile.write(str(fine_json_object))