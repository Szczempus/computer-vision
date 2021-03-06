import cv2

orignal_img = cv2.imread(r'F:\Users\BardKrzysztof\PycharmProjects\computer-vision\assets\view.jpeg')
img = orignal_img.copy()
# cv2.imshow('original_img', img)

thresh_val = 120
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(src=gray, thresh=thresh_val, maxval=255, type=cv2.THRESH_BINARY)[1]
cv2.imshow(f'threshold value : {thresh_val}', thresh)

contours = cv2.findContours(image= thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'[INFO] Liczba wykrytych konturów {len(contours)}')

# cont = 40
# img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[cont]], contourIdx=-1, color=(0, 255, 0), thickness=2)
# cv2.imshow('img_cnt', img_cnt)
#
# area = cv2.contourArea(contour=contours[cont], oriented=True)
# print(area)

max_area = 0

for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour=contour, oriented=True)
    if area > max_area:
        max_area = area
        idx_flag_area = idx

print(f'[INFO] Index konturu o największym polu:  {idx_flag_area} \nPole: {max_area}')

img_cnt_max_area = cv2.drawContours(image=img.copy(), contours=[contours[idx_flag_area]], contourIdx=-1, color=(0, 255, 0), thickness=2)

cv2.imshow('img_cnt_max_area', img_cnt_max_area)

perimeter = cv2.arcLength(curve=contours[idx_flag_area], closed=True)
print(perimeter)


# ----- Salata Tamplate -----#
# orignal_img = cv2.imread(r'F:\Users\BardKrzysztof\PycharmProjects\computer-vision\assets\1.jpg')
# img = orignal_img.copy()
# cv2.imshow('original_img', img)
#
# gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# for thres_val in range (60, 90, 1):
#     thres = cv2.threshold(src=gray, thresh=thres_val, maxval=255, type=cv2.THRESH_BINARY)[1]
#     cv2.imshow(f'threshold value : {thres_val}', thres)
#     cv2.waitKey(10)
# ----- Salata Tamplate -----#





cv2.waitKey(0)
