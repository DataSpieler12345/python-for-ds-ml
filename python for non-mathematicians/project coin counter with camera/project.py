import cv2
import numpy as np

# Definition of functions
def point(points):
    n_points = np.concatenate([points[0], points[1], points[2], points[3]]).tolist()
    y_order = sorted(n_points, key=lambda point: point[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda point: point[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda point: point[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

# Definition of work area alignment
def alignment(image, width, height):
    aligned_image = None
    grays = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, hold = cv2.threshold(grays, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("hold", hold)
    
# Contour alignment and hierarchy
    contours = cv2.findContours(hold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
    
    for contour in contours:
        epsilon = 0.01 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if len(approx) == 4:
            points = point(approx)
            p1 = np.float32(points)
            p2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            M = cv2.getPerspectiveTransform(p1, p2)
            aligned_image = cv2.warpPerspective(image, M, (width, height))
    
    return aligned_image

# Video capture
video_capt = cv2.VideoCapture(0)

# Verify camera operation
while True:
    cam_type, camera = video_capt.read()
    if not cam_type:
        break
    
    image_A6 = alignment(camera, width=480, height=677)  # Work area
    
    if image_A6 is not None:
        image_gray = cv2.cvtColor(image_A6, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(image_gray, (5, 5), 1)  # Blurring the image with a Gaussian pattern
        _, hold_2 = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
        cv2.imshow("hold", hold_2)
        
        contour2 = cv2.findContours(hold_2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(image_A6, contour2, -1, (255, 0, 0), 2)
        
        sum1 = 0.0
        sum2 = 0.0
        
        for c_2 in contour2:
            area = cv2.contourArea(c_2)
            moments = cv2.moments(c_2)
            
            if moments["m00"] == 0:
                moments["m00"] = 1.0
            
            x = int(moments["m10"] / moments["m00"])
            y = int(moments["m01"] / moments["m00"])
            
            # 20/100
            if area < 12000 and area > 6701:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image_A6, "S/. 0.20", (x, y), font, 0.75, (0, 255, 0), 2)
                sum1 = sum1 + 0.2
            
            # 10/100
            if area < 6702 and area > 6700:
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image_A6, "S/. 0.10", (x, y), font, 0.75, (0, 255, 0), 2)
                sum2 = sum2 + 0.2
        
        total = sum1 + sum2
        print("Total Sum in cents:", round(total, 2))
        
        cv2.imshow("image_A6", image_A6)
        cv2.imshow("camera", camera)
    
  # Turn off the camera
    if cv2.waitKey(1) == ord('q'):
        break

video_capt.release()
cv2.destroyAllWindows()
