# Breaking image into pixels
#///// Developed By @abhi_laksh aka Abhishek Soni

# Importing modules
import numpy as np
import pandas as pd
import cv2

path=input("Enter path of image : ").replace("\\","/")
# cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
img =  cv2.imread(path)

print(img.shape)
resImg= cv2.resize(img,(1000,1000))
cv2.imshow('image',resImg)
while True:
	key = cv2.waitKey(10)
	if key== ord('q'):
		break