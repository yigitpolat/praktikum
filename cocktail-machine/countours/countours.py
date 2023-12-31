import cv2
from matplotlib import pyplot as plt
import imutils
import numpy as np
import cv2

original_image = cv2.imread('../../images/test_1.JPG')
image_in_gray = cv2.split(original_image)[0]

blur_image = cv2.GaussianBlur(image_in_gray, (7, 7), 1000)
# cv2.imshow('blur_image', blur_image)

# Plot on histogram
plt.hist(blur_image.ravel(), 256,[0, 256])
# plt.show()

# Apply threshold
(T, image_modified) = cv2.threshold(blur_image, 110, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('image greyscale', image_modified)

# Apply Canny
canny_image = cv2.Canny(blur_image, 50, 250)
# cv2.imshow('canny_image', canny_image)

# Find Countours and sort them to find the biggest enclosed area whic is white surface
# This method discarded
# contours = cv2.findContours(canny_image, cv2.THRESH_BINARY, cv2.CHAIN_APPROX_SIMPLE)
# contours = imutils.grab_contours(contours)
# areas = [cv2.contourArea(contour) for contour in contours]
# (contours, areas) = zip(*sorted(zip(contours, areas), key=lambda a:a[1]))
# cv2.drawContours(original_image_copy2, [contours[-1]], -1, (255, 0, 0), 10)
# cv2.imshow("Biggest", original_image_copy2)

# Apply Contours
contours = cv2.findContours(canny_image, cv2.THRESH_BINARY, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
final_image = original_image.copy()
cv2.drawContours(final_image,  contours, -1, (255, 0, 0), 5)
cv2.imshow('image_in_gray', final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()