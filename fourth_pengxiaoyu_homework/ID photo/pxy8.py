import cv2


img = cv2.imread("image.png")


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b, g, r = img[i, j]
        if b > 30 and g < 40 and r > 170:
            img[i,j]=(255,255,255)

cv2.imshow('res',img)

cv2.waitKey(0)

cv2.imwrite('res.png', img)

