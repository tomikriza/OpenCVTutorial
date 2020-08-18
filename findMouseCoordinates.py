import cv2
import numpy as np

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       # draw circle here (etc...)
       print('x = %d, y = %d'%(x, y))


def Main():
    img = cv2.resize(cv2.imread("Resources/cards.jpg"),(512,512))
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',onMouse)

    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
        elif k == ord('a'):
            cv2.putText(img,str((x,y)),(x,y),cv2.FONT_HERSHEY_COMPLEX,1,4)

Main()