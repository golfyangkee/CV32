# 거리계산에 관한 기본적인 내용

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지 생성 및 거리 변환
img = np.zeros((256, 256), dtype="uint8")
cv2.circle(img, (70, 70), 50, (255, 255, 255), (-1))
cv2.circle(img, (140, 140), 70, (255, 255, 255), (-1))

dist_transform = cv2.distanceTransform(img, cv2.DIST_L2, 3)
plt.imshow(dist_transform)
plt.show()
