import numpy as np
import cv2

original_image = cv2.imread('../../images/test_1.JPG')
image_hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# Take S and remove any value that is less than half
s = image_hsv[:, :, 1]
s = np.where(s < 127, 0, 1)

# We increase the brightness of the image and then mod by 255
v = (image_hsv[:, :, 2] + 127) % 255
v = np.where(v > 127, 1, 0)

# Combine our two masks
foreground = np.where(s + v > 0, 1, 0).astype(np.uint8)

background = np.where(foreground == 0, 255, 0).astype(np.uint8)
background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)
foreground = cv2.bitwise_and(original_image, original_image, mask=foreground)
finalimage = background + foreground
cv2.imshow('image', finalimage)

cv2.waitKey(0)
cv2.destroyAllWindows()