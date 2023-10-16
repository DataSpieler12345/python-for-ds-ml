import cv2
import numpy as np

valueGauss=1
valueKernel=7
original=cv2.imread('project coin counter with static images/media/soles.jpg')
gray=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
gauss=cv2.GaussianBlur(gray, (valueGauss,valueGauss), 0)
canny=cv2.Canny(gauss, 60,100)
kernel=np.ones((valueKernel,valueKernel),np.uint8)
closing=cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

contour, hierarchy=cv2.findContours(closing.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("coins found: {}".format(len(contour)))
cv2.drawContours(original, contour, -1, (0,0,255),2)

# Show the results
# cv2.imshow("grays",gray)
# cv2.imshow("gauss",gauss)
# cv2.imshow("canny",canny)
# cv2.imshow("closing",closing)

cv2.imshow("Result:", original)
cv2.waitKey(0)