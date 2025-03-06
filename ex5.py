import cv2
img = cv2.imread('vishal.jpg')
gauBlur = cv2.GaussianBlur(img, (21, 21), 0)
cv2.imwrite('vishal.jpg', gauBlur)
