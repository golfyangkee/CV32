### 선형 필터링 작업

import cv2
import numpy as np

img = cv2.imread('../img/apple.jpg')


k1 = np.array([[1, 2, 1],
                [2, 4, 2],
                [1, 2, 1]]) *(1/16)
print(k1)

blur1 = cv2.filter2D(img, -1, k1)


k2 = cv2.getGaussianKernel(3, 0)  # 마스크 커널 만들어짐
print(k2)
'''
sigma = 0
[[0.25]
 [0.5 ]
 [0.25]]
 
 sigma = 1.5
 [[0.30780133]
 [0.38439734]
 [0.30780133]]
'''

blur2 = cv2.filter2D(img, -1, k2*k2.T) # T : 행렬 바꾼거
# k2 그냥 넣으면 원본 이미지랑 크게 달라지지 않는다.

blur3 = cv2.GaussianBlur(img, (3, 3), 0)
print(type(blur3),'-------') # <class 'numpy.ndarray'> -------

print('k1:', k1)
print('k2:', k2*k2.T)
merged = np.hstack((img, blur1, blur2, blur3))
cv2.imshow('gaussian blur', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()