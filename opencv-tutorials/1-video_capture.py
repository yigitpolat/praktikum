import numpy as np
import cv2

# cap = cv2.VideoCapture(0)  # 0=first webcam
cap = cv2.VideoCapture('../images/video.mp4')

while True:
    # if frame is read correctly, returns true
    ret, frame = cap.read()

    # 3 is width
    width = int(cap.get(3))
    # 3 is height
    height = int(cap.get(4))

    # numpy zero array
    image = np.zeros(frame.shape, np.uint8)

    # resize video frame
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # place small frame 4 times
    image[:height // 2, :width // 2] = smaller_frame
    image[height // 2:, :width // 2] = smaller_frame
    image[:height // 2, width // 2:] = smaller_frame
    image[height // 2:, width // 2:] = smaller_frame

    # image show
    cv2.imshow('image', image)

    # press q to quit
    if cv2.waitKey(100) == ord('q'):
        break

# release camera resource
cap.release()
cv2.destroyAllWindows()
