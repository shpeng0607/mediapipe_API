import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

# 使用 XVID 編碼
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# 建立 VideoWriter 物件，輸出影片至 output.avi
# FPS 值為 30.0，解析度為 640x360
out = cv2.VideoWriter('data/action2_11.avi', fourcc, 30.0, (640, 360))

frameNum = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        if frameNum == 300:
            break
        out.write(frame)
        frameNum = frameNum + 1
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()