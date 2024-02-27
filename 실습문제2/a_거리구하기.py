# 1. 아래의 코드에서 빈칸을 채워서 거리구하기 코드를 작성해 보세요
# a_ .py

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 빈 이미지 생성
img = np.zeros((256, 256), dtype="uint8")

# 2. 원 그리기
cv2.circle(img, (70, 70), 50, (255, 255, 255), -1)
cv2.circle(img, (140, 140), 70, (255, 255, 255), -1)

# 3. 거리 변환 수행
dist_transform = cv2.distanceTransform(img, cv2.DIST_L2, 3)

# 4. 결과 시각화
plt.imshow(dist_transform)
plt.show()