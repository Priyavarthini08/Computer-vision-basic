import os
import cv2
img = cv2.imread(os.path.join('.', 'C:\\Users\PRIYA\Downloads\\bird.jpg'))
k_size = 7

#averageblur
img_blur = cv2.blur(img, (k_size, k_size))
#Gaussian blue
img_gaussianblur = cv2.GaussianBlur(img, (k_size, k_size),5)
#Median blur
img_median = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussianblur', img_gaussianblur)
cv2.imshow('img_median',img_median)
cv2.waitKey(0)

# 3 types of blur
# (Average/Gaussian/Median)
