import cv2
import numpy as np
import math


cam = cv2.VideoCapture(0)


while cam.isOpened():
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    cv2.rectangle(frame, (300, 300), (100, 100), (0, 255, 0), 0)
    cropFrame = frame[100:300, 100:300]
# ==  ==  ==  Following is for particular color(Wear glubs of blue color for recogniton)  ==  ==  ==

    hsv = cv2.cvtColor(cropFrame, cv2.COLOR_BGR2HSV)

    lower = np.array([83, 62, 62])
    upper = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

# ==  ==  ==  This is general  ==  ==  ==
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(mask, (5, 5), 0)

    # blur = cv2.GaussianBlur(gray, (5, 5), 0)

    

    # gray = cv2.cvtColor(cropFrame, cv2.COLOR_BGR2GRAY)

    # blur = cv2.GaussianBlur(gray, (35, 35), 0)

    _, thresh = cv2.threshold(
        blur, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    cv2.imshow("Thresh", thresh)

    image, contours, hierarchy = cv2.findContours(
        thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    cntrs = max(contours, key=lambda x: cv2.contourArea(x))

    x, y, w, h = cv2.boundingRect(cntrs)
    cv2.rectangle(cropFrame, (x, y), (x+w, y+h), (0, 0, 255), 0)

    hull = cv2.convexHull(cntrs)

    draw = np.zeros(cropFrame.shape, np.uint8)
    cv2.drawContours(draw, [cntrs], 0, (0, 255, 0), 0)
    cv2.drawContours(draw, [hull], 0, (0, 0, 255), 0)
    cntrs = cv2.approxPolyDP(cntrs, 0.01*cv2.arcLength(cntrs, True), True)
    hull = cv2.convexHull(cntrs, returnPoints=0)

    if cntrs is not None or hull is not None:
        defects = cv2.convexityDefects(cntrs, hull)
        count_defects = 0

        cv2.drawContours(thresh, contours, -1, (0, 255, 0), 3)
    
        if(True):
            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]

                start = tuple(cntrs[s][0])
                end = tuple(cntrs[e][0])
                far = tuple(cntrs[f][0])
                dist = cv2.pointPolygonTest(cntrs,far,True)
                a = math.sqrt((end[0]-start[0])**2 + (end[1] + start[1])**2)
                b = math.sqrt((far[0]-start[0])**2 + (far[1] + start[1])**2)
                c = math.sqrt((end[0]-far[0])**2 + (end[1] + far[1])**2)

                angle = math.acos((b**2+c**2-a**2)/(2*b*c)) *57

                if angle<=90:
                    count_defects=count_defects + 1
                    cv2.circle( cropFrame,far,5,[0,0,255],-1)

                cv2.line(cropFrame,start,end,[0,255,0],2)
            
            if count_defects == 2:
                cv2.putText(frame,"This is 1",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,2)
            elif count_defects == 3:
                cv2.putText(frame,"I am Abhishek", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            elif count_defects == 4:
                cv2.putText(frame,"This is 4 :P", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            elif count_defects == 5:
                cv2.putText(frame,"Hi!!!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
            else:
                cv2.putText(frame,"Please Don't Punch Me!!", (2, 50),cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
    else:
        print("No countr detected")

    cv2.imshow("Frame",frame)
    cv2.imshow("Drawing",draw)
    cv2.imshow("Cropped",cropFrame)
    key= cv2.waitKey(10)
    if key== ord('q'):
        break