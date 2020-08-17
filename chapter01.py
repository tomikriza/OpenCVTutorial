import cv2
import numpy as np

# 1.
#img = cv2.imread("Resources/lena.png")
#cv2.imshow("Output",img)
#cv2.waitKey(0)

# 2.
#videoPath = "Resources/test_video.mp4"
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# cap.set(10,100)

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# 3.

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # to grayscale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img, 150  , 200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations = 1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

# cv2.imshow("Gray Image",imgGray)jj
# cv2.imshow("Blur Gray Image",imgBlur)
cv2.imshow("Canny Edges",imgCanny)
cv2.imshow("Dialation Edges",imgDialation)
cv2.imshow("Eroded Edges",imgEroded)


cv2.waitKey(0)


















