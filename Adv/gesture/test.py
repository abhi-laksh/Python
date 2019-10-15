import cv2
import numpy as np
import imutils as im

cam = cv2.VideoCapture(0)

while(True):
    ret, frame = cam.read()

    # Following is for particular color(Wear glubs of blue color for recogniton)

    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower = np.array([83, 62, 62])
    # upper = np.array([130, 255, 255])

    # mask = cv2.inRange(hsv, lower, upper)

    # This is general
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # blur = cv2.GaussianBlur(mask, (5, 5), 0)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    ret, thresh1 = cv2.threshold(
        blur, 70, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)

    _, contours, hierarchy = cv2.findContours(
        thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    draw = np.zeros(frame.shape, np.uint8)
    max_area = 0
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        if(area > max_area):
            max_area = area
            ci = i
    cnt = contours[ci]
    hull = cv2.convexHull(cnt)
    moments = cv2.moments(cnt)
    if moments['m00'] != 0:
        cx = int(moments['m10']/moments['m00'])  # cx = M10/M00
        cy = int(moments['m01']/moments['m00'])  # cy = M01/M00

    centr = (cx, cy)

    cv2.circle(frame, centr, 10, [255, 255, 0], 3)
    cv2.drawContours(draw, [cnt], 0, (0, 255, 0), 2)
    cv2.drawContours(draw, [hull], 0, (0, 0, 255), 2)

    cnt = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    hull = cv2.convexHull(cnt, returnPoints=False)

    if(True):
        defects = cv2.convexityDefects(cnt,hull)
        minDef = 0
        maxDef = 0

        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            dist = cv2.pointPolygonTest(cnt,centr,True)
            cv2.line(frame,start,end,[0,255,0],2)                
            cv2.circle(frame,far,5,[0,0,255],-1)
            print(i)
    cv2.imshow('frame', frame)
    # cv2.imshow('gray', mask)
    cv2.imshow('gray', gray)
    cv2.imshow('blur', blur)
    cv2.imshow('thershold', draw)

    # Press q to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
cam.release()
