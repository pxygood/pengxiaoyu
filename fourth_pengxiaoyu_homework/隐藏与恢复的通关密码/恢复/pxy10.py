import cv2


img = cv2.imread("t.png")


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b, g, r = img[i, j]
        if b < 255 and g < 255 and r < 255:
            img[i,j]=(255,0,0)

cv2.imshow('t2.2',img)

cv2.waitKey(0)

cv2.imwrite('t2.2.png', img)