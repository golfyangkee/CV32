### 선형 필터링 작업

import cv2
import numpy as np

# 가우시안 커널을 만들어서 filter2D 함수를 통해 블러링 작업
# 이미지에 적용하게 되면 커널 크기와 표준 편차에 맞는 블러링 효과를 리턴 받는다.

img = cv2.imread('../img/apple.jpg')

# 가우시안 1D 커널 생성
k2 = cv2.getGaussianKernel(3, 0)  # 마스크 커널 만들어짐
print(k2)
# 커널 크기는 홀수로 줘야 한다. 3, 5, 7
# 시그마가 가우시안 커널의 k 사이즈 생성해서 표준편차 계산해서 리턴해다오.
# 시그마 0을 주면 k사이즈를 자동계산
# ktype 커널의 데이터 타입

# 2D 가우신 커널 생성 (1D 커널을 외적으로 만들어서) 적용해보자.
gauss_2D = np.outer(k2, k2.T) # 2차원 배열을 반환

# filter2D 함수를 적용해서 가우시안 커널을 적용하자.
blur2 = cv2.filter2D(img, -1, gauss_2D)
# 2D라서 1차원 연산을 안 한다. 그래서 2차원으로 만들어줘야 진행된다.
# 컨볼루션 연산

merged = np.hstack((img, blur2))
cv2.imshow('gaussian blur', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()