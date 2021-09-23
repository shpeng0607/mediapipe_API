import cv2
import mediapipe as mp
from google.protobuf.json_format import MessageToDict

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def draw_texts(frame, text, position):
    cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)

cap = cv2.VideoCapture("origin_data/action2/action2_1.avi")
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        leftORright = []

        if not results.multi_hand_landmarks:
            continue
        else:
            for hand_handedness in results.multi_handedness:
                print(MessageToDict(hand_handedness))
                leftORright.append(MessageToDict(hand_handedness)['classification'][0])

        if (len(leftORright) > 1) and (leftORright[0]['label'] == leftORright[1]['label']):
            if leftORright[0]['score'] > leftORright[1]['score']:
                if leftORright[0]['label'] == 'Left':
                    leftORright[1]['label'] = 'Right'
                else:
                    leftORright[1]['label'] = 'Left'
            elif leftORright[0]['score'] < leftORright[1]['score']:
                if leftORright[1]['label'] == 'Left':
                    leftORright[0]['label'] = 'Right'
                else:
                    leftORright[0]['label'] = 'Left'
            else:
                pass
        print(leftORright)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image_hight, image_width, _ = image.shape
        i = 0
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                draw_texts(image, leftORright[i]['label'],(int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width),
                                                           int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_hight)))
                i = i + 1
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()