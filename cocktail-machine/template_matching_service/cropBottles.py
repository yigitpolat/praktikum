import cv2
import base64

def cropBottles(img):
    img = cv2.imread(img)

    img_gray = cv2.split(img)[0]

    martini = cv2.imread('./images/template-matching-martini.JPG', 0)
    bitterol = cv2.imread('./images/template-matching-bitterol.JPG', 0)
    tanqueray = cv2.imread('./images/template-matching-tanqueray.JPG', 0)

    martini_height, martini_width = martini.shape
    bitterol_height, bitterol_width = bitterol.shape
    tanqueray_height, tanqueray_width = tanqueray.shape

    img_copy = img.copy()
    img_gray_copy = img_gray.copy()

    # result
    martini_result = cv2.matchTemplate(img_gray_copy, martini, cv2.TM_CCOEFF_NORMED)
    _, _, martini_min_loc, martini_max_loc = cv2.minMaxLoc(martini_result)

    bitterol_result = cv2.matchTemplate(img_gray_copy, bitterol, cv2.TM_CCOEFF_NORMED)
    _, _, bitterol_min_loc, bitterol_max_loc = cv2.minMaxLoc(bitterol_result)

    tanqueray_result = cv2.matchTemplate(img_gray_copy, tanqueray, cv2.TM_CCOEFF_NORMED)
    _, _, tanqueray_min_loc, tanqueray_max_loc = cv2.minMaxLoc(tanqueray_result)

    martini_location = martini_max_loc
    bitterol_location = bitterol_max_loc
    tanqueray_location = tanqueray_max_loc

    martini_bottle = img[martini_location[1]:martini_location[1] + martini_height,
                     martini_location[0]:martini_location[0] + martini_width]
    retval, buffer = cv2.imencode('.jpg', martini_bottle)
    martini_base64 = base64.b64encode(buffer)

    bitterol_bottle = img[bitterol_location[1]:bitterol_location[1] + bitterol_height,
                      bitterol_location[0]:bitterol_location[0] + bitterol_width]
    retval, buffer = cv2.imencode('.jpg', bitterol_bottle)
    bitterol_base64 = base64.b64encode(buffer)

    tanqueray_bottle = img[tanqueray_location[1]:tanqueray_location[1] + tanqueray_height,
                      tanqueray_location[0]:tanqueray_location[0] + tanqueray_width]
    retval, buffer = cv2.imencode('.jpg', tanqueray_bottle)
    tanqueray_base64 = base64.b64encode(buffer)

    return {"martini_base64": martini_base64,
            "bitterol_base64": bitterol_base64,
            "tanqueray_base64": tanqueray_base64
            }