import cv2
import numpy as np

img = cv2.imread("Resources/shutterstock_1386882278-1.jpg")

print(img.shape)

imgResize = cv2.resize(img,(300,200)) # in opencv width is first then height


imgCropped = img[0:200,200:500] # Without opencv height is first then width and we need to mention it using ranges

cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)