import cv2
from matplotlib import pyplot as plt
import imutils
import numpy as np
import cv2
import random

# original_image = cv2.imread('../images/test_1.JPG')
# image_in_gray = cv2.split(original_image)[0]
# # img_greyscale = cv2.imread('../images/white_background_10.JPG', 0)
#
# image_in_gray = cv2.GaussianBlur(image_in_gray, (7, 7), 1000)
#
# edges = cv2.Canny(original_image, 0, 80)
# # cv2.imshow('image_in_gray', edges)

##########

original_image = cv2.imread('../images/test_2.JPG')

lower_blue = np.array([190, 190, 190])
upper_blue = np.array([225, 225, 225])

# preparing the mask to overlay
mask = cv2.inRange(original_image, lower_blue, upper_blue)
result = cv2.bitwise_and(original_image, original_image, mask=mask)
# cv2.imshow('blur_image', result)

# lower_black = np.array([0,0,0], dtype = "uint16")
# upper_black = np.array([170,170,170], dtype = "uint16")
# black_mask = cv2.inRange(original_image, lower_black, upper_black)
#
# black_mask[np.where((black_mask == [0] ).all(axis = 1))] = [255]
# cv2.imshow('mask1',black_mask)

# blackandwhite = cv2.bitwise_not(original_image)

# cv2.imshow('blur_image', original_image)



# image_in_gray = cv2.split(original_image)[0]

# blur_image = cv2.GaussianBlur(image_in_gray, (21, 21), 0)
# cv2.imshow('blur_image', blur_image)


# plt.hist(blur_image.ravel(), 256,[0, 256])
# plt.show()
# (T, image_modified) = cv2.threshold(blur_image, 100, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('image greyscale', image_modified)
# # #
edges = cv2.Canny(result, 150, 300)
cv2.imshow('image_in_gray', edges)
# # #
# contours, hierarchy = cv2.findContours(black_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# # # #
# final_image = original_image.copy()
# cv2.drawContours(final_image,  contours, -1, (255, 0, 0), 5)
# cv2.imshow('image_in_gray', final_image)
# print(len(contours))

# for count in contours:
#     epsilon = 0.01 * cv2.arcLength(count, True)
#     approximations = cv2.approxPolyDP(count, epsilon, True)
# cv2.drawContours(final_image, [approximations], 0, (0), 3)

############

# plt.hist(image_in_gray.ravel(), 256,[0, 256]); plt.show()
# (T, image_modified) = cv2.threshold(image_in_gray, 150, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('image greyscale', image_modified)



# hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
# # cv2.imshow('hsv', hsv)
# lower_blue = np.array([150])
# # setup numpy array for a blue color
# upper_blue = np.array([200])
# # take the blue colors between above values
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
# result = cv2.bitwise_and(image_in_gray, image_in_gray, mask=mask)
# cv2.imshow('result', result)


# contours = cv2.findContours(result.copy(), cv2.THRESH_BINARY, cv2.CHAIN_APPROX_SIMPLE)
# contours = imutils.grab_contours(contours)
# original_image_copy1 = original_image.copy()
# original_image_copy2 = original_image.copy()
# cv2.drawContours(original_image_copy1, contours, -1, (255, 0, 0), 10)
# cv2.imshow("All Contours", original_image_copy1)
#
# areas = [cv2.contourArea(contour) for contour in contours]
# (contours, areas) = zip(*sorted(zip(contours, areas), key=lambda a:a[1]))
# cv2.drawContours(original_image_copy2, [contours[-1]], -1, (255, 0, 0), 10)
# cv2.imshow("Biggest", original_image_copy2)


cv2.waitKey(0)  # wait infinite
cv2.destroyAllWindows()