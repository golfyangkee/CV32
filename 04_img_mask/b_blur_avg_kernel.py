import cv2
import numpy as np

img = cv2.imread('../img/apple.jpg') # 그냥 기본으로 가지고 온 것
# 내부적으로 채널 분리해서 필터로 컨볼루션연산하고 다시 합쳐서 블러 작업한 결과 나오는 것

'''
#5x5 평균 필터 커널 생성   
kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04],
                   [0.04, 0.04, 0.04, 0.04, 0.04]])
'''
# 5x5 평균 필터 커널 생성
kernel = np.ones((5,5))/5**2
kernel3 = np.ones((3,3))/5**2

# 필터 적용
blured = cv2.filter2D(img, -1, kernel) # 사용자 커널 생성 함수
# 컨볼루션 연산
blured3 = cv2.filter2D(img, -1, kernel3) # 사용자 커널 생성 함수

# 결과 출력
cv2.imshow('origin', img)
cv2.imshow('avrg blur', blured)
cv2.imshow('avrg3 blur', blured3)
cv2.waitKey()
cv2.destroyAllWindows()