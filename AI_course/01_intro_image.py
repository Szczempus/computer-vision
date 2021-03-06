import cv2
import numpy as np

#image = cv2.imread(filename=r'F:\Users\BardKrzysztof\PycharmProjects\computer-vision\assets\bear.jpg')
#cv2.imshow(winname='image', mat=image)
#cv2.waitKey(delay=0)

original_img = cv2.imread(filename=r'assets/dog.jpeg')
img = original_img.copy()

cv2.imshow(winname='img', mat=img)
cv2.waitKey(0)

