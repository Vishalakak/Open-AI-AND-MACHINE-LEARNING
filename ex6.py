import cv2
img = cv2.imread('vishal.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshImg = cv2.threshold(gray, 80, 130, cv2.THRESH_BINARY)[1]
cv2.imwrite('theresoldImage2.jpg', threshImg)