import cv2
import numpy as np
print("Package Imported")

img = cv2.imread("Resources/shutterstock_1386882278-1.jpg")
kernel = np.ones((5,5),np.uint8) # This will give 0 to 255 image i.e. 8 bits

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # Grayscale Image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1) # Blurred Image
imgCanny = cv2.Canny(img,150,200) # To find edges
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) # to increase dark edges
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blurred Image Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)

