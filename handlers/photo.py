import cv2
import numpy as np

img = cv2.imread('images/sam.jpg')
img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))          #(img.shape[1] // 2, img.shape[0] // 2))
new_img = np.zeros(img.shape, dtype ='uint8')
# mirror отзеркаливание видео
# img = cv2.flip(img, 1)

#circiut контуры
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (3, 3), 0) #Blur

img = cv2.Canny(img, 50, 50)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(new_img, con, -1, (0,127,257), 1)

cv2.imshow('Good!', new_img)
cv2.waitKey(0)

