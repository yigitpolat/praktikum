import cv2

img = cv2.imread('../../images/template-matching-2.JPG')
img_gray = cv2.split(img)[0]

martini = cv2.imread('../../images/template-matching-martini.JPG', 0)
bitterol = cv2.imread('../../images/template-matching-bitterol.JPG', 0)
tanquery = cv2.imread('../../images/template-matching-tanquery.JPG', 0)

martini_height, martini_width = martini.shape
bitterol_height, bitterol_width = bitterol.shape
tanquery_height, tanquery_width = tanquery.shape

# tries every method one-by-one
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img_copy = img.copy()
    img_gray_copy = img_gray.copy()

    # result
    martini_result = cv2.matchTemplate(img_gray_copy, martini, method)
    _, _, martini_min_loc, martini_max_loc = cv2.minMaxLoc(martini_result)

    bitterol_result = cv2.matchTemplate(img_gray_copy, bitterol, method)
    _, _, bitterol_min_loc, bitterol_max_loc = cv2.minMaxLoc(bitterol_result)

    tanquery_result = cv2.matchTemplate(img_gray_copy, tanquery, method)
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

    martini_bottom_right = (martini_location[0]+martini_width, martini_location[1]+martini_height)
    bitterol_bottom_right = (bitterol_location[0]+bitterol_width, bitterol_location[1]+bitterol_height)
    tanquery_bottom_right = (tanquery_location[0]+tanquery_width, tanquery_location[1]+tanquery_height)

    cv2.rectangle(img_copy, martini_location, martini_bottom_right, 255,5)
    cv2.rectangle(img_copy, bitterol_location, bitterol_bottom_right, 255,5)
    cv2.rectangle(img_copy, tanquery_location, tanquery_bottom_right, 255,5)

    cv2.imshow('template-matching', img_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# template-matching-1.JPG method 1 2   4 5 6
# template-matching-2.JPG method   2
# template-matching-3.JPG method 1 2
# template-matching-4.JPG method 1 2   4 5 6

# TM_CCOEFF_NORMED