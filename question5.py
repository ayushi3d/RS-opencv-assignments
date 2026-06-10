import cv2
import numpy as np
img = cv2.imread("mountain.jpeg")
img = cv2.resize(img, (500, 300))
b, g, r = cv2.split(img)
cv2.imwrite("blue_channel.jpg",b)
cv2.imwrite("green_channel.jpg",g)
cv2.imwrite("red_channel.jpg",r)
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)


g = np.zeros_like(g)
merged = cv2.merge([b, g, r])

cv2.imshow("Merged Without Green", merged)
cv2.imwrite("mountain_without_green.jpg", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()