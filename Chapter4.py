import cv2
import numpy as np

img = cv2.imread("Resources/hand-cards-trump-spades.jpg")

width,height = 400,600

pst1 = np.float32([[225,93],[430,136],[164,383],[365,426]])  # top left, top right, bottom left, bottom right in order pixels
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pst1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)