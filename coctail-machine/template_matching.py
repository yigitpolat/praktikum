import numpy as np
import cv2

img = cv2.imread('../images/img-white-background-4.JPG', 0)
martini = cv2.imread('../images/martini.JPG', 0)
bitterol = cv2.imread('../images/bitterol.JPG', 0)
tanquery = cv2.imread('../images/tanquery.JPG', 0)

h, w = martini.shape

# tries every method one-by-one
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    # result
    martini_result = cv2.matchTemplate(img2, martini, method)
    _, _, martini_min_loc, martini_max_loc = cv2.minMaxLoc(martini_result)

    bitterol_result = cv2.matchTemplate(img2, bitterol, method)
    _, _, bitterol_min_loc, bitterol_max_loc = cv2.minMaxLoc(bitterol_result)

    tanquery_result = cv2.matchTemplate(img2, tanquery, method)
    _, _, tanquery_min_loc, tanquery_max_loc = cv2.minMaxLoc(tanquery_result)

    # these method takes the min_loc
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        martini_location = martini_min_loc
        bitterol_location = bitterol_min_loc
        tanquery_location = tanquery_min_loc
    else:
        martini_location = martini_max_loc
        bitterol_location = bitterol_max_loc
        tanquery_location = tanquery_max_loc

    bottom_right = (martini_location[0]+ w, martini_location[1]+h)
    bitterol_location = (bitterol_location[0]+ w, bitterol_location[1]+h)
    tanquery_location = (tanquery_location[0]+ w, tanquery_location[1]+h)
    cv2.rectangle(img2, martini_location, bottom_right, 255,5)
    cv2.rectangle(img2, bitterol_location, bottom_right, 255,5)
    cv2.rectangle(img2, tanquery_location, bottom_right, 255,5)
    cv2.imshow('match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# method 2 and 6 worked for img-white-background-1.JPG
# mothod 2 worked for img-white-background-2.JPG
# method 3 and 4 did not work for image-white-background-3.JPG
# method 3 did not work for img-white-background-4.JPG