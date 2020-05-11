import cv2
import os
cls = lambda: os.system('cls')
cls()
img = cv2.imread('opencv.jpg')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
