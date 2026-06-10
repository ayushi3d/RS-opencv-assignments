import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened() :
    print("not")
kernel=5
while True:
    ret,frame =cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(kernel,kernel),0)
    edges=cv2.Canny(blur,50,150)
    cv2.imshow("EdgesDetection",edges)
    key=cv2.waitKey(1)
    if key==ord('w'):
        kernel+=2
    elif key==ord('d'):
        kernel-=2
    elif key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()