import cv2
import numpy as np

img = cv2.imread("lena.jpeg")
img_line = cv2.line(img,(349,809),(780,816),(0,255,0),3)
cv2.imshow("Image_line",img_line)
cv2.waitKey(0)

cv2.imwrite('lena7.jpeg', img_line)
