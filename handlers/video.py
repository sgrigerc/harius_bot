import cv2
import numpy as np

# img = cv2.imread('images/OpenCV.jpg')
# cv2.imshow('Result', img)
#
# cv2.waitKey(0)

cap = cv2.VideoCapture(0)    #'videos/ashaley.mp4'
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    success, img = cap.read()
    new_img = np.zeros(img.shape, dtype='uint8')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 0)

    img = cv2.Canny(img, 20, 20)

    kernel = np.ones((2, 2), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)

    img = cv2.erode(img, kernel, iterations=1)

    con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(new_img, con, -1, (189, 21, 105), 1)

    cv2.imshow('Good!', new_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break