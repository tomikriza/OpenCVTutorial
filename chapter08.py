import cv2
import numpy as np
from getContours import *

path = "Resources/shapes.png"
img = cv2.imread(path)
imgContour = img.copy()

imgGrayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrayscale,(7,7),1)

imgCanny = cv2.Canny(imgBlur,50,50)

getContours(imgCanny,imgContour)

cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Contour Image", imgContour)
# cv2.imshow("Original", img)
# cv2.imshow("Grayscale", imgGrayscale)
# cv2.imshow("Blureds", imgBlur)
cv2.waitKey(0)