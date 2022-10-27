import cv2


img = cv2.imread("t2.png")


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b, g, r = img[i, j]
        if b < 250 and g < 250 and r < 250:
            img[i,j]=(252,252,252)

cv2.imshow('t2.1',img)

cv2.waitKey(0)

cv2.imwrite('t2.1.png', img)