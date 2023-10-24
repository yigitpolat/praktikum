import numpy as np
import cv2

original_image = cv2.imread('../../images/test_1.JPG')
#
# # convert frame into some color format
# hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
#
# lower_white = np.array([0, 0, 0])
# upper_white = np.array([0, 0, 255])
#
# # take the blue colors between above values
# mask = cv2.inRange(hsv_image, lower_white, upper_white)
# # bitwise to frames with mask
# result = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)
#
# cv2.imshow('image', result)

myimage_hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# Take S and remove any value that is less than half
s = myimage_hsv[:, :, 1]
s = np.where(s < 127, 0, 1)  # Any value below 127 will be excluded

# We increase the brightness of the image and then mod by 255
v = (myimage_hsv[:, :, 2] + 127) % 255
v = np.where(v > 127, 1, 0)  # Any value above 127 will be part of our mask

# Combine our two masks based on S and V into a single "Foreground"
foreground = np.where(s + v > 0, 1, 0).astype(np.uint8)  # Casting back into 8bit integer

background = np.where(foreground == 0, 255, 0).astype(np.uint8)  # Invert foreground to get background in uint8
background = cv2.cvtColor(background, cv2.COLOR_GRAY2BGR)  # Convert background back into BGR space
foreground = cv2.bitwise_and(original_image, original_image, mask=foreground)  # Apply our foreground map to original image
finalimage = background + foreground  # Combine foreground and background
cv2.imshow('image', finalimage)

cv2.waitKey(0)
cv2.destroyAllWindows()