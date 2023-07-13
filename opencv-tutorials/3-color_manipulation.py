import numpy as np
import cv2

# cap = cv2.VideoCapture(0)  # 0=first webcam
cap = cv2.VideoCapture('../images/video.mp4')

while True:
    ret, frame = cap.read()  # ret = return true false

    width = int(cap.get(3))
    height = int(cap.get(4))

    # convert frame into some color format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # setup numpy array for a blue color
    lower_blue = np.array([90, 50, 50])
    # setup numpy array for a blue color
    upper_blue = np.array([130, 255, 255])
    # take the blue colors between above values
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # bitwise to frames with mask
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('image', result)
    cv2.imshow('mask', mask)

    # ord is q's ascii value
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()  # release camera resource
cv2.destroyAllWindows()
