import cv2
import numpy as np

def empty(a): # This is a mandatory empty method used to create trackbar
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

path = 'Resources/hand-cards-trump-spades.jpg'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
# Creating Trackbar. Named Window should be same. First Element e.g. 24 is the number which we want want the particular portion to detect the color
cv2.createTrackbar("Hue Min","TrackBars",24,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",160,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",39,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",31,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

# Setting in infinite loop so that whenever we change the values it will be in real time
while True:
    img = cv2.imread(path)
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")

    print(h_min,h_max,s_min,s_max,v_min,v_max)

    lower = np.array([h_min,s_min,v_min])  # Minimum values
    upper = np.array([h_max,s_max,v_max]) # Maximum values
    mask = cv2.inRange(imgHsv,lower,upper) # mask is used to apply the above settings in the image. For e.g. make it as white as possible what we want to show and other things as black

    imgResult = cv2.bitwise_and(img,img,mask=mask) # Adding original image and masked applied image to form a new image to detect color

    imgstack = stackImages(0.6,([img,imgHsv],[mask,imgResult]))

    cv2.imshow("Stacked Images",imgstack)

  #  cv2.imshow("Original",img)
 #    cv2.imshow("hsv",imgHsv)
  #  cv2.imshow("mask", mask)
 #   cv2.imshow("imgResult", imgResult)
    cv2.waitKey(1)