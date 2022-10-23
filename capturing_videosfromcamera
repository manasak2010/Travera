# STARTING VIDEO STREAM AND SAVING IT IN 
#      1) IN LOCAL STORAGE
#      2) IN CLOUD STORAGE

video = cv2.VideoCapture(0)
if (video.isOpened() == False):
    print("Error reading video file")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('C:/Users/KIIT/Desktop/picsample/new.mp4', cv2.VideoWriter_fourcc(*'MPEG'), 10, size)
while(True):
    ret, frame = video.read()
    if ret == True:
        result.write(frame) 
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

            
video.release()
result.release()
storage.child("/video/new.mp4").put("C:/Users/KIIT/Desktop/picsample/new.mp4")
cv2.destroyAllWindows()

print("The video was successfully saved")
