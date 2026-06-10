import cv2
frame=cv2.imread("robot_vision.jpg")
gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cv2.rectangle(gray_frame,(10,10),(100,100),(0,255,0),3)
cv2.imshow("robotvision",gray_frame)
cv2.waitKey(1)
#ANSWER
"""A → False (OpenCV loads images in BGR format by default not in RGB)
B → True (gray_frame is a single-channel grayscale image, so rectangle will not appear green )
C → True (cv2.waitKey(1) waits only 1 millisecond and the window closes immediately)
D → False ((10,10) and (100,100) are top-left and bottom-right coordinates, not center and width-height)

Correct Option: B and C""""""