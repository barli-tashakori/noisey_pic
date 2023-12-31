from random import choices
import cv2 as cv

img=cv.imread("me.jpg",0)
height,width=img.shape

for i in range(height):
    for j in range(width):
        pixel_noise=choices([True,False],cum_weights=(5,95))[0]
        if pixel_noise==True:
            img[i,j]=255-img[i,j]

cv.imshow("output",img)
cv.waitKey()