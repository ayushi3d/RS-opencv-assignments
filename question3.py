import cv2
img = cv2.imread("scenario.jpeg")
if img is None:
    print("Image not found!")
    exit()
denoised = cv2.medianBlur(img, 5)
cv2.imwrite("denoised_image.png",denoised)
height, width, channels = img.shape
pixels = height * width

print("Height =", height)
print("Width =", width)
print("Channels =", channels)
print("Total Pixels =", pixels)

img_small=cv2.resize(img,(80,50))
denoised_small=cv2.resize(denoised,(80,50))

cv2.imshow("Original Image", img)
cv2.imshow("Denoised Image", denoised)

cv2.waitKey(0)
cv2.destroyAllWindows()