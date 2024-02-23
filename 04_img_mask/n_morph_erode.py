import cv2
import numpy as np

img = cv2.imread('../img/Lenna.png')
# img = cv2.imread('../img/apple.jpg')

# 구조화 요소 커널, 사각형 (3x3) 생성 명시 생성
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# 침식 연산 적용
erosion = cv2.erode(img, k)
# apple은 안에 점 없어짐
# Lenna는
# 침식은 안의 대상을 매꾸거나 제거할 때

# 결과 출력
merged = np.hstack((img, erosion))
cv2.imshow('Erode', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()