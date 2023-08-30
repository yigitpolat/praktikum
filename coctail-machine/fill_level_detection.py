import cv2
from matplotlib import pyplot as plt
import imutils

# read image grayscale
# bottle_image = cv2.imread("../images/sample_bottle.png", 0)

# read image and take first channel only
bottle_image = cv2.imread("../images/sample_bottle.png")
bottle_gray = cv2.split(bottle_image)[0]

# blur image
bottle_gray = cv2.GaussianBlur(bottle_gray, (7, 7), 0)

# manual threshold
# plt.hist(bottle_gray.ravel(), 256,[0, 256]); plt.show()
(T, bottle_threshold) = cv2.threshold(bottle_gray, 27.5, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("Bottle Gray Threshold 27.5", bottle_threshold)

# apply opening operation to remove the white edges of the water
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
bottle_open = cv2.morphologyEx(bottle_threshold, cv2.MORPH_OPEN, kernel)
# cv2.imshow("Bottle Open 5 x 5", bottle_open)

# find all contours
contours = cv2.findContours(bottle_open.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
bottle_original_image = bottle_image.copy()
cv2.drawContours(bottle_original_image, contours, -1, (255, 0, 0), 2)
cv2.imshow("All Contours", bottle_original_image)

# sort contours by area
areas = [cv2.contourArea(contour) for contour in contours]
(contours, areas) = zip(*sorted(zip(contours, areas), key=lambda a:a[1]))

# print contour with largest area
bottle_original_image = bottle_image.copy()
cv2.drawContours(bottle_original_image, [contours[-1]], -1, (255, 0, 0), 2)
# cv2.imshow("Largest contour", bottle_original_image)

# draw bounding box, calculate aspect and display decision
bottle_original_image = bottle_image.copy()
(x, y, w, h) = cv2.boundingRect(contours[-1])
aspectRatio = w / float(h)
if aspectRatio < 0.4:
    cv2.rectangle(bottle_original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(bottle_original_image, "Full", (x + 10, y + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
else:
    cv2.rectangle(bottle_original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(bottle_original_image, "Low", (x + 10, y + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
cv2.imshow("Decision", bottle_original_image)
cv2.waitKey(0)