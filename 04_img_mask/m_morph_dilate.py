import cv2
import numpy as np

# img = cv2.imread('../img/apple.jpg')
img = cv2.imread('../img/Lenna.png')

# 구조화 요소 커널, 사각형 (3x3) 생성 명시 생성
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)) # 컨볼루션 계산

# 팽창 연산 적용
dst = cv2.dilate(img, k)
# apple은 밖에 아무것도 없으니까 안에 점이 확장 되는 느낌
# Lenna는 안에 눈이 좀 커지는 느낌

# 결과 출력
merged = np.hstack((img, dst))
cv2.imshow('Dilation', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
