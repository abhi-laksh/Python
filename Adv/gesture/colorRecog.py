import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)

# low_arr = []
# up_arr = []
# for i in range(1, 4):
#     rgb_low = int(input("Enter lower value  for RGB to convert"))
#     rgb_up = int(input("Enter upper value for RGB to convert"))
#     low_arr.append(rgb_low)
#     up_arr.append(rgb_up)

while(True):
    rett, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # lower = np.array(low_arr)
    # upper = np.array(up_arr)
    lower = np.array([83, 62, 62])
    upper = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)

    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
