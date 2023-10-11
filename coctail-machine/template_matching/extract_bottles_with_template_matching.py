import cv2
from liquid_level import *

img = cv2.imread('../../images/template-matching-1.JPG')
img_gray = cv2.split(img)[0]

martini = cv2.imread('../../images/template-matching-martini.JPG', 0)
bitterol = cv2.imread('../../images/template-matching-bitterol.JPG', 0)
tanquery = cv2.imread('../../images/template-matching-tanquery.JPG', 0)

martini_height, martini_width = martini.shape
bitterol_height, bitterol_width = bitterol.shape
tanquery_height, tanquery_width = tanquery.shape

img_copy = img.copy()
img_gray_copy = img_gray.copy()

# result
martini_result = cv2.matchTemplate(img_gray_copy, martini, cv2.TM_CCOEFF_NORMED)
_, _, martini_min_loc, martini_max_loc = cv2.minMaxLoc(martini_result)

bitterol_result = cv2.matchTemplate(img_gray_copy, bitterol, cv2.TM_CCOEFF_NORMED)
_, _, bitterol_min_loc, bitterol_max_loc = cv2.minMaxLoc(bitterol_result)

tanquery_result = cv2.matchTemplate(img_gray_copy, tanquery, cv2.TM_CCOEFF_NORMED)
_, _, tanquery_min_loc, tanquery_max_loc = cv2.minMaxLoc(tanquery_result)


martini_location = martini_max_loc
bitterol_location = bitterol_max_loc
tanquery_location = tanquery_max_loc


martini_bottle = img[martini_location[1]:martini_location[1]+martini_height, martini_location[0]:martini_location[0] + martini_width]
cv2.imwrite('../../images/template-matching-martini-crop.png',martini_bottle)

bitterol_bottle = img[bitterol_location[1]:bitterol_location[1]+bitterol_height, bitterol_location[0]:bitterol_location[0] + bitterol_width]
cv2.imwrite('../../images/template-matching-bitterol-crop.png',bitterol_bottle)

tanquery_bottle = img[tanquery_location[1]:tanquery_location[1]+tanquery_height, tanquery_location[0]:tanquery_location[0] + tanquery_width]
cv2.imwrite('../../images/template-matching-tanquery-crop.png',tanquery_bottle)

is_bottle_full("../../images/template-matching-bitterol-crop.png")
is_bottle_full("../../images/template-matching-tanquery-crop.png")
