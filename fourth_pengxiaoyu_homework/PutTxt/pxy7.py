import cv2
import numpy as np


img = cv2.imread("lena.jpeg")
img_putText = cv2.putText(img,"HELLO",(120,250),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

cv2.imshow("Image_putText",img_putText)

cv2.waitKey(0)

cv2.imwrite('lena8.jpeg', img_putText)