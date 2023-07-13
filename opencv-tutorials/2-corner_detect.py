import cv2
import numpy as np

img = cv2.imread('../images/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# convert colors
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# corner detaction algorithm

# parameter position 3 = qualility of corners
# parameter position 3 = 0
# parameter position 4 = minimum distance
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# prints in array of array
corners = np.int0(corners)
print(corners)

# draws blue circles
for corner in corners:
    x, y = corner.ravel()  # flatten numpy array
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

# draws lines between corners
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
