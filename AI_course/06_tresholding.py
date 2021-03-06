import cv2

img = cv2.imread(r'F:\Users\BardKrzysztof\PycharmProjects\computer-vision\assets\grey.png')
print(img)
cv2.imshow('img', img)

threshold_binary = cv2.threshold(src=img, thresh=150, maxval=255, type=cv2.THRESH_BINARY)[1]

for threshold in [0, 50, 100, 150, 200]:
    threshold_binary = cv2.threshold(src=img, thresh=threshold, maxval=255, type=cv2.THRESH_BINARY)[1]
    cv2.imshow(f'threshold value : {threshold}', threshold_binary)
    cv2.waitKey(2000)
    cv2.destroyWindow(f'threshold value : {threshold}')

cv2.waitKey(0)