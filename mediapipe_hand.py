from sys import path
import cv2
import json
import os
from os import listdir
from os.path import isfile, isdir, join
import mediapipe as mp
from google.protobuf.json_format import MessageToDict

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

part = ['train', 'val']
actionset = ["wipe", "spin", "hold"]

for p in part:
    for num, action in enumerate(actionset):
        path = "./origin_data/action" + str(num+1) + "/" + p + "/"
        fileList = os.listdir(path)

        for f in fileList:
            fullpath = join(path, f)
            # For webcam input:
            cap = cv2.VideoCapture(fullpath)

            with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
                data_list = []
                frameNum = 1
                while cap.isOpened():
                    success, image = cap.read()
                    if frameNum == 300:
                        print("Ignoring empty camera frame.")
                        break

                    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                    image.flags.writeable = False
                    results = hands.process(image)
                    skeletonlist = []

                    # Draw the hand annotations on the image.
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    if results.multi_hand_landmarks:
                        for hand_landmarks in results.multi_hand_landmarks:
                            # MessageToDict(hand_handedness) label is not accurate
                            print(MessageToDict(hand_landmarks)['landmark'])
                            list = []
                            for i in MessageToDict(hand_landmarks)['landmark']:
                                list.append(i['x'])
                                list.append(i['y'])
                                list.append(i['z'])

                            if len(list) < 63: print("??")
                            skeletonlist.append(list)
                            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    # if len(skeletonlist) == 1:
                    #     list = []
                    #     for i in range(63):
                    #         list.append(0)
                    #     skeletonlist.append(list)
                    #     print("#" + str(frameNum))
                    # elif len(skeletonlist) == 0:
                    #     list = []
                    #     for i in range(63):
                    #         list.append(0)
                    #     skeletonlist.append(list)
                    #     skeletonlist.append(list)
                    #     print("##" + str(frameNum))

                    frame_dict = {
                        "frame_index": frameNum,
                        "skeleton": skeletonlist
                    }

                    json.dumps(frame_dict)
                    data_list.append(frame_dict)
                    frameNum = frameNum + 1
                    cv2.imshow('MediaPipe Hands', image)
                    if cv2.waitKey(1) == 27:
                        break

            json_dict = {
                "data": data_list,
                "label": action,
                "label_index": num
            }

            # Serializing json
            json_object = json.dumps(json_dict, indent = 4)

            # Writing to sample.json
            outpath = "./JSON_data/mediapipe_" + p + "/" + f.split('.')[0] + ".json"
            with open(outpath, "w") as outfile:
                outfile.write(str(json_object))

            cap.release()