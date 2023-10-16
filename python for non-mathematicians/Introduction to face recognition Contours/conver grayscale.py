import cv2
# the path
image = cv2.imread('Introduction to face recognition Contours/media/frame.jpg')
# convert to black and white 
# cvtColor ("https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# separates the object from its environment
# https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
_,room = cv2.threshold(gray,100,255,cv2.THRESH_BINARY) #_, dummy variable
# identifying contours
# https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
contour, hierarchy = cv2.findContours(room,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# Draw the contour
# https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
# cv2.drawContours(image,contour, 1,(65, 105, 225),3)
# cv2.drawContours(image,contour, 2,(65, 105, 225),3)
cv2.drawContours(image,contour, -1,(65, 105, 225),3)

# show the image
cv2.imshow('original image',image)
cv2.imshow('image in gray',gray)
cv2.imshow('room image',room)
cv2.waitKey(0) # the value 0 is static
cv2.destroyAllWindows() # destroy all windows (open more than 2)