# color codes are mentioned as 0,150,0 or 0,255,0 in brackets

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) # This will give 0 to 255 image i.e. 8 bits
print(img.shape[1]) # To check dimensions of image

#img[:] = 255,0,0  # colon is for the whole image. Same concept as did in Chapter 2 and define the color code besides

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # to get full diagonal

cv2.line(img,(0,0),(300,300),(0,255,0),3) # To get half diagonal

cv2.rectangle(img,(0,0),(250,300),(0,0,255),cv2.FILLED) # cv2.filled fills the area with the color. 0 is horizontal movement of circle and 0 is vertical movement

cv2.circle(img,(400,50),30,(255,255,0),5) # 30 is the radius. 400 is horizontal movement of circle and 50 is vertical movement

cv2.putText(img,"Open CV",(300,200),cv2.FONT_HERSHEY_DUPLEX,1,(0,150,0),3) # 1 is the size of text and 3 is the thickness

cv2.imshow("Image",img)

cv2.waitKey(0)