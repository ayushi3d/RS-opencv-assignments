import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    frame = cv2.flip(frame, 1)

    h, w = frame.shape[:2]
    half = cv2.resize(frame, (w//2, h//2))
    gray = cv2.cvtColor(half, cv2.COLOR_BGR2GRAY)
    quarter = cv2.resize(frame, (w//2, h//2))
    top_left = quarter
    top_right = cv2.flip(quarter, 0)
    hsv = cv2.cvtColor(quarter, cv2.COLOR_BGR2HSV)
    bottom_left = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    b, g, r = cv2.split(quarter)

    red_only = np.zeros_like(quarter)
    red_only[:, :, 2] = r

    # Combining 4 views
    top = np.hstack((top_left, top_right))
    bottom = np.hstack((bottom_left, red_only))
    final = np.vstack((top, bottom))
    cv2.imshow("Half Size Grayscale", gray)
    cv2.imshow("4 Window View", final)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()