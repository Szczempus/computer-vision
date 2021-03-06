import cv2
import imutils

img = cv2.imread(r'F:\Users\BardKrzysztof\PycharmProjects\computer-vision\assets\bear.jpg')
view = cv2.imread(r'F:\Users\BardKrzysztof\PycharmProjects\computer-vision\assets\view.jpeg')

img = imutils.resize(img, height=600)

# cv2.imshow('img', img)
# cv2.imshow('view', view)
# cv2.waitKey(0)

#Region of Interest - RoI
rows, cols, channels = img.shape
roi = view[:rows, :cols]
# cv2.imshow('roi', roi)
# cv2.waitKey(0)

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

mask = cv2.threshold(src=gray, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('mask', mask)


mask_inv = cv2.bitwise_not(src=mask)
# cv2.imshow('mask_inv', mask_inv)
# cv2.waitKey(0)

img_bg = cv2.bitwise_and(src1=roi, src2=roi, mask=mask)
bear_fg = cv2.bitwise_and(src1=img, src2=img, mask=mask_inv)
# cv2.imshow('bear_fg', bear_fg)
# cv2.waitKey(0)

dst = cv2.add(src1=img_bg, src2=bear_fg)
img[:rows, :cols] = dst
cv2.imshow('dst', dst)
cv2.imshow('add_out', img)
cv2.waitKey(0)