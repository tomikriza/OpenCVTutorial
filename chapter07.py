import cv2
import numpy as np

def empty():
    pass

path = "Resources/lambo.jpg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",700,700)
cv2.createTrackbar("Hue Min","TrackBars",12,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",72,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",95,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",250,255,empty)
cv2.createTrackbar("Val Min","TrackBars",56,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while (True):
    img = cv2.resize(cv2.imread(path),(250,250))
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    hue_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    hue_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    sat_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    sat_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    val_min = cv2.getTrackbarPos("Val Min","TrackBars")
    val_max = cv2.getTrackbarPos("Val Max","TrackBars")
    lower = np.array([hue_min,sat_min,val_min])
    upper = np.array([hue_max,sat_max,val_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    
    cv2.imshow("Images",np.hstack((img,imgHSV,imgResult)))


    cv2.waitKey(10)