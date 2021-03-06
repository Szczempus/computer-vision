import cv2
import imutils

img = cv2.imread(r'F:\Users\BardKrzysztof\PycharmProjects\computer-vision\assets\1.jpg')
cv2.imshow('salata', img)
# cv2.waitKey(0)

for threshold1_val in range (0,256,10):
    for threshold2_val in range (0,256,10):
        canny = cv2.Canny(image=img, threshold1=threshold1_val, threshold2=threshold2_val)
        cv2.imshow(f'threshold value : {threshold1_val} , {threshold2_val}', canny)
        cv2.waitKey(1)
        cv2.destroyWindow(f'threshold value : {threshold1_val}, {threshold2_val}')

cv2.waitKey(0)