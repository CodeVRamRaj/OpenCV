import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
import time

cap = cv2.VideoCapture('video2.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ram1.mp4', fourcc, 20, (640, 480))

while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.resize(frame, (640, 480), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        out.write(b)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture('back.mp4')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ram2.mp4', fourcc, 20, (640, 480))

while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.resize(frame, (640, 480), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        out.write(b)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()



cap = cv2.VideoCapture('ram1.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ramm1.mp4',fourcc, 20, (640,480))
# img = cv2.imread('images/b11.jpg')
# img= cv2.resize(img, (640, 480))

cap1 = cv2.VideoCapture('ram2.mp4')

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()
while True:
    ret, frame = cap.read()
    ret1, frame2 = cap1.read()
    time.sleep(1 / 20)

    if ret == True:
        frame1 = segmentor.removeBG(frame, frame2, threshold=0.9)  # threshold to cut
        out.write(frame1)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

