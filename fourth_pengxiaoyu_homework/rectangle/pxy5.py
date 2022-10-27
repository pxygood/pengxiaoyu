import cv2
import numpy as np


img = cv2.imread("lena.jpeg")

img_rectangle = cv2.rectangle(img,(300,900),(750,480),(255,0,255),2)

cv2.imshow("Image_rectangle",img_rectangle)

cv2.waitKey(0)

cv2.imwrite('lena6.jpeg', img_rectangle)
