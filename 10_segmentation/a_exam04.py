import cv2
import numpy as np
#  5*5 크기의 검은 색 이미지를 만들고  중앙에 전경 픽셀을 추가한 후  거리 변환을 계산해 보자.
image = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0]], dtype=np.uint8)

dist_transform = cv2.distanceTransform(image, cv2.DIST_L2, 3)
normalized_dist_transform = cv2.normalize(dist_transform, None, 0, 255, cv2.NORM_MINMAX)

print(dist_transform)