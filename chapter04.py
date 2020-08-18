import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
img[:] = 255,0,255

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),8)
cv2.rectangle(img,(0,0),(512,500),(0,0,118),cv2.FILLED)
cv2.circle(img,(400,50),30,(255,255,119),5)
cv2.putText(img," OpenCV ", (300,200),cv2.FONT_HERSHEY_COMPLEX,1,(150,0,0),2)


cv2.imshow("Image", img)



cv2.waitKey(0)