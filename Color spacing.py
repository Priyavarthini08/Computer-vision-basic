import os
import cv2
img = cv2.imread(os.path.join('.', 'C:\\Users\PRIYA\Downloads\\bird.jpg'))

#colour combination
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
#cvColor()-convert img from one color space to another color space

cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_rcb', img_rgb)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('img_hls', img_hls)

cv2.waitKey(0)
##one such is application-color detection
