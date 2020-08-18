import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
print(img.shape)

imgResize = cv2.resize(img, (240,240))

cv2.imshow("Image", img)
cv2.imshow("Image 2", imgResize)

imgCropped = img[0:200,200:500]
cv2.imshow("3", imgCropped)

cv2.waitKey(0)