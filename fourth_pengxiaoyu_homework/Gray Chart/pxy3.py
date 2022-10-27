import cv2
import numpy as np


img = cv2.imread("lena.jpeg")
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Image_gray",img_gray)
cv2.imshow("Image",img)
cv2.waitKey(0)

cv2.imwrite('lena4.jpeg', img_gray)