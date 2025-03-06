
import cv2
img = cv2.imread('vishal.jpg')
cv2.imshow('Vishal', img)
cv2.imwrite('vishal_copy.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
