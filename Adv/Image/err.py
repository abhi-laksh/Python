import os

try:
	from PIL import  Image
	import cv2
	import numpy as np
except ImportError:
	module = ['pillow', 'opencv-python']
	for mod in  module:
		os.system("python -m pip install " + mod)

	import cv2
	from PIL import Image
	import numpy as np


 #  ----  To write image
# cv2.imwrite('messigray.png',img)
# img = Image.open("cap.png")

image = cv2.imread("cap.png",cv2.IMREAD_GRAYSCALE )



# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


ret,thresh_img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)

# cv2.imwrite('bw.png',thresh_img)

crpImg= thresh_img[18:62, 25:190]

gray = cv.bitwise_not(gray)
bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                                cv.THRESH_BINARY, 15, -2)




# img = Image.open('bw.png')

# img= img.crop((29,0,186,80))

n=6




#  ----    Split image into each char

def getChar(n,img):
	ht,wd=img.shape
	charc_width = wd//n
	for i in range(0, n):
		x = charc_width * i
		y = 0
		w = charc_width+x
		h = ht+y
		print(y , " | " , h , " /|\ " , x , " | " , w)

		cropped = img[y:h , x:w]
		# cropped.save("crp" + str(i) + ".png")
		cv2.imwrite("crp" + str(i) + ".png" , cropped)

getChar(n,crpImg)



#  ----  getting cordimates of a image
H,W = crpImg.shape
cordnates=[]
# print(crpletterg[H-10][W-20])		# pixel value at (x,y) of letterage

for x in range(H):
	for y in range(W):
		if crpImg[x][y] !=0:
			# crpImg[x][y] = 111
			pass
			
			

cv2.imwrite("mod.png", crpImg )




# print(thresh_img)
while True:
    cv2.imshow('frame', crpImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

