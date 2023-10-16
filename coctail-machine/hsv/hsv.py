import numpy as np
import cv2

# cap = cv2.VideoCapture(0)  # 0=first webcam
cap = cv2.VideoCapture('../images/video.mp4')

while True:

    ###### option 1
    #
    # original_image = cv2.imread('../../images/test_2.JPG')
    #
    # lower_blue = np.array([190, 190, 190])
    # upper_blue = np.array([225, 225, 225])
    # #
    # # # preparing the mask to overlay
    # mask = cv2.inRange(original_image, lower_blue, upper_blue)
    # result = cv2.bitwise_and(original_image, original_image, mask=mask)
    # cv2.imshow('blur_image', result)

    # lower_black = np.array([0,0,0], dtype = "uint16")
    # upper_black = np.array([170,170,170], dtype = "uint16")
    # black_mask = cv2.inRange(original_image, lower_black, upper_black)
    #
    # black_mask[np.where((black_mask == [0] ).all(axis = 1))] = [255]
    # cv2.imshow('mask1',black_mask)

    # blackandwhite = cv2.bitwise_not(original_image)

    # cv2.imshow('blur_image', original_image)

    ######


    ####### option 2

    # hsv = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    # # cv2.imshow('hsv', hsv)
    # lower_blue = np.array([150])
    # # setup numpy array for a blue color
    # upper_blue = np.array([200])
    # # take the blue colors between above values
    # mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # result = cv2.bitwise_and(image_in_gray, image_in_gray, mask=mask)
    # cv2.imshow('result', result)

    #######option 3


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
