# 이미지를 불러온 후 Canny 엣지 검출 알고리즘을 사용하여 엣지를 검출합니다.

import cv2
apple_image = cv2.imread('Apples.jpg')

edges = cv2.Canny(apple_image, 100, 200)
cv2.imwrite('apple_edges.jpg', edges)

