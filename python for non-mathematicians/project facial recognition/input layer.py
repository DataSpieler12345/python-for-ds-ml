import cv2
import numpy as np
import os
import imutils

# folders to capture images
model = '007Agent Pictures'
rout1 = 'E:/PYTHON DS & ML BILDUNG/python for non-mathematicians/project facial recognition'
full_path = rout1 + '/' + model
# ask python if this rout exist
if not os.path.exists(full_path):
   os.makedirs(full_path)
   
noises = cv2.CascadeClassifier('E:\PYTHON DS & ML BILDUNG\python for non-mathematicians\project facial recognition\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')

# frame the face
camera = cv2.VideoCapture(0)
id = 0
while True:
   answer,capture = camera.read()
   if answer == False:break
   capture = imutils.resize(capture,width=640) # camera pixels down
   
   
   
   grays = cv2.cvtColor(capture, cv2.COLOR_BGR2GRAY)
   id_capture = capture.copy()
   face = noises.detectMultiScale(grays, 1.3,5)
   
   for(x,y,e1,e2) in face:
      cv2.rectangle(capture, (x,y), (x+e1,y+e2), (0,255,0),2)
      face_capture = id_capture[y:y+e2,x:x+e1]
      face_capture = cv2.resize(face_capture, (160,160),interpolation=cv2.INTER_CUBIC)
      cv2.imwrite(full_path+'/image_{}.jpg'.format(id), face_capture)
      id = id+1
         
   # show the user
   cv2.imshow("Result Face", capture)
   
   if id==51: # or cv2.waitKey(1) ==ord('q'):
      break

# close the loops
camera.release()
cv2.destroyAllWindows()
   