import cv2
import imutils

img = cv2.imread('vishal.jpg')
resizedImg = imutils.resize(img, width=5)
cv2.imshow('Vishal.jpg', resizedImg)