import cv2
import imutils


def is_bottle_full(image):
    bottle_image = cv2.imread(image)
    bottle_gray = cv2.split(bottle_image)[0]

    (T, bottle_threshold) = cv2.threshold(bottle_gray, 96, 255, cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    bottle_open = cv2.morphologyEx(bottle_threshold, cv2.MORPH_OPEN, kernel)

    contours = cv2.findContours(bottle_open.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    areas = [cv2.contourArea(contour) for contour in contours]
    (contours, areas) = zip(*sorted(zip(contours, areas), key=lambda a: a[1]))

    (x, y, w, h) = cv2.boundingRect(contours[-1])
    aspectRatio = w / float(h)
    if aspectRatio < 0.4:
        return {"bottle_fill": "true"}
    else:
        return {"bottle_fill": "false"}
