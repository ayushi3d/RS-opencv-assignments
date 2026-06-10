import cv2
import time
cap=cv2.VideoCapture(0)
prev=0
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    curr=time.time()
    fps=1/(curr-prev)
    prev=curr

    cv2.putText(frame,f":{int(fps)}",(20,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("webcam",frame)
    key=cv2.waitKey(1)
    if key==ord('a'):
        cv2.imwrite("capture.jpg",frame)
        print("image saved")
        if key==ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
