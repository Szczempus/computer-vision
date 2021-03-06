import cv2
import numpy as np

#image = cv2.imread(filename=r'F:\Users\BardKrzysztof\PycharmProjects\computer-vision\assets\bear.jpg')
#cv2.imshow(winname='image', mat=image)
#cv2.waitKey(delay=0)

original_img = cv2.imread(filename=r'F:\Users\BardKrzysztof\PycharmProjects\computer-vision\assets\dog.jpeg')
img = original_img.copy()

# cv2.imshow(winname='img', mat=img)
# cv2.waitKey(0)

height, width = img.shape[:2]
print(f'Wysokość: {height}')
print(f'Szerokość: {width}')

# cv2.line(img=img, pt1=(0,0), pt2=(width, height), color=(0, 123, 200), thickness=2)
# cv2.imshow(winname='img', mat=img)
# cv2.waitKey(0)

# cv2.rectangle(img=img, pt1= (200,50), pt2=(300, 100), color=(250, 110, 100), thickness=4, lineType=cv2.LINE_AA )
# cv2.imshow(winname='img', mat=img)
# cv2.waitKey(0)

# cv2.circle(img=img, center=(width // 2, height // 2), radius=100, color=(20, 80, 180), thickness=-1)
# cv2.imshow(winname='img', mat=img)
# cv2.waitKey(0)

# img = original_img.copy()
# pts = np.array([[300, 140], [200, 200], [200, 50], [300, 50]], dtype='int32').reshape((-1, 1, 2))
# cv2.polylines(img=img, pts=[pts], isClosed=False, color=(0, 255, 0), thickness=3)
# cv2.imshow('logo', img)
# cv2.waitKey(0)

# -------------
# ---polygon---
# -------------
# img = original_img.copy()
# pts = np.array([[300, 140], [200, 200], [200, 50], [300, 50]], dtype='int32').reshape((-1, 1, 2))
# cv2.polylines(img=img, pts=[pts], isClosed=True, color=(0, 255, 0), thickness=3)
# cv2.imshow('logo', img)
# cv2.waitKey(0)

# ----------
# ---text---
# ----------
# img = original_img.copy()
# cv2.putText(
#     img=img,
#     text='Python rulez',
#     org=(20, 40),
#     fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#     fontScale=1.5,
#     color=(0, 255, 0),
#     thickness=2
# )
#
# cv2.imshow('logo', img)
# cv2.waitKey(0)

