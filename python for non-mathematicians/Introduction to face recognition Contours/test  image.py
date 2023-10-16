import cv2

image = cv2.imread('frame.jpg')

if image is not None:
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Unable to load image "frame.jpg"')