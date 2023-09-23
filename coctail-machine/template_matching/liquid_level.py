import cv2
from matplotlib import pyplot as plt
import imutils


def is_bottle_full(image):
    bottle_image = cv2.imread(image)
    bottle_gray = cv2.split(bottle_image)[0]

    # manual threshold
    plt.hist(bottle_gray.ravel(), 256,[0, 256]); plt.show()
    (T, bottle_threshold) = cv2.threshold(bottle_gray, 78, 255, cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    bottle_open = cv2.morphologyEx(bottle_threshold, cv2.MORPH_OPEN, kernel)
    # cv2.imshow("Bottle Open 5 x 5", bottle_open)

    contours = cv2.findContours(bottle_open.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    # bottle_original_image = bottle_image.copy()
    # cv2.drawContours(bottle_gray, contours, -1, (0, 255, 0), 5)
    # cv2.imshow("All Contours", bottle_original_image)

    areas = [cv2.contourArea(contour) for contour in contours]
    (contours, areas) = zip(*sorted(zip(contours, areas), key=lambda a: a[1]))
    bottle_original_image = bottle_image.copy()
    cv2.drawContours(bottle_original_image, [contours[-1]], -1, (255, 0, 0), 2)
    cv2.imshow("Largest contour", bottle_original_image)

    # cv2.imshow("Bottle Gray Threshold 27.5", bottle_threshold)
    #
    # # bottle_gray = cv2.GaussianBlur(bottle_gray, (7, 7), 0)


    # cv2.imshow("Decision", bottle_gray)
    cv2.waitKey(0)