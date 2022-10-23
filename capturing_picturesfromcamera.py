#INITIALIZING FIREBASE AT START

import cv2
cam = cv2.VideoCapture(0)  #cam1

cv2.namedWindow("Camera")
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Camera", frame)  #display the frame

    k = cv2.waitKey(1)&0xFF
    if k == 27:
        print("Exit")
        break
    elif k == 32:
   
        img_name = "C:/Users/KIIT/Desktop/picsample/opencv_frame_{}.png".format(img_counter)
        path_on_cloud = "day1/"+str(img_counter)+".png"
        local_path = img_name
        storage.child(path_on_cloud).put(local_path)
        print("C:/Users/KIIT/Desktop/picsample/opencv_frame_{}.png".format(img_counter))
        
        cv2.imwrite(img_name, frame)
        print("{} captured".format(img_name))
        img_counter += 1

cam.release() 
cv2.destroyAllWindows()
