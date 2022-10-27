import cv2
import numpy as np

img = cv2.imread("lena.jpeg") ##Choose any image
shape = img.shape
print(img.shape)
imgResize = cv2.resize(img,(224,224)) ##Decrease size
imgResize2 = cv2.resize(img,(1300,1300)) ##Increase size
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Increase size",imgResize2)
print(imgResize.shape)
cv2.waitKey(0)

cv2.imwrite('lena1.jpeg',imgResize)
cv2.imwrite('lena2.jpeg',imgResize2)
