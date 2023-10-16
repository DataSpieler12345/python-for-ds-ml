import cv2
image = cv2.imread('Introduction to face recognition Contours/media/frame.jpg')
cv2.imshow('image',image)
cv2.waitKey(0) # the value 0 is static
cv2.destroyAllWindows() # destroy all windows (open more than 2)