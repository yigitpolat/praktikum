import cv2
import random

img = cv2.imread('../images/bean.JPG')

# read image greyscale
# img_greyscale = cv2.imread('assets/bean.JPG', 0)

# read image with somevalues
# img_something = cv2.imread('assets/bean.JPG', 1)

# resize
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# rotate
# img = cv2.rotate(img, cv2.ROTATE_180)

# Type:  <class 'numpy.ndarray'> (image is a numpy array)
print("Type: ", type(img))

# Shape: (3840, 2160, 3)
# 3 is called channel. RGB for coloured image
print("Shape: ", img.shape)

# pixel value at 3839x1000
# print("Pixel 3839x1000", img[3839][1000])
print(img[3839][1000:2159])

# crop, display, and print image in an array
bean = img[400:1500, 800:2000]
cv2.imshow('cropped bean', bean)
print(bean)

# iterate over rows
for i in range(int(img.shape[0] / 2)):
    # iterate over columns
    for j in range(img.shape[1]):
        # assign random color
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('random images', img)

# cv2.imwrite('assets/new_bean.jpg', img)
# cv2.imshow('window_label', img_greyscale)
# cv2.imshow('window_label', img_something)


cv2.waitKey(0)  # wait infinite
cv2.destroyAllWindows()

# draw line
# img = cv2.line(img, ...)

# draw rectangle
# img = cv2.rectangle(img, ...)

# write text
# img = cv2.putText(img, ...)
