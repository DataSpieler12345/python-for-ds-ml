import cv2
video_cap = cv2.VideoCapture(0)
if not video_cap.isOpened():
   print("No Camera attached")
   exit()
while True:
   camera_typ, Camera = video_cap.read()
   grays = cv2.cvtColor(Camera, cv2.COLOR_BGR2GRAY)
   
   cv2.imshow("Live Camera", grays)
   if cv2.waitKey(1)==ord("q"):
      break
video_cap.release()
cv2.destroyAllWindows()

#press q to close camera