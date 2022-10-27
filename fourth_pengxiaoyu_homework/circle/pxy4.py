import cv2
import numpy as np


img = cv2.imread("lena.jpeg")

img_circle = cv2.circle(img,(580,600),200,(255,255,0),2)
cv2.imshow("Image circle",img_circle)

cv2.waitKey(0)

cv2.imwrite('lena5.jpeg', img_circle)