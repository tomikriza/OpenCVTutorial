import cv2
import numpy as np

img = cv2.resize(cv2.imread("Resources/cards.jpg"),(512,512))

width, height = 250,350
pts1 = np.float32([[323,149],[468,204],[225,366],[421,475]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Warped image",imgOutput)
cv2.imwrite("Resources/acquired card.jpg",imgOutput)

cv2.waitKey(0)