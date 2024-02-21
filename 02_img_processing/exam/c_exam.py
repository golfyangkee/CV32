# 1. apple 이미지 로드
# 2. 빨간색을 추출해보자. (마스크를 생서해서 마스크 값에 해당되면 추출하자)
import numpy as np
import cv2 as cv

apple=cv.imread('../../img/apple.jpg')

# 1. 색공간 변환 해보자. HSV
hsv_img = cv.cvtColor(apple, cv.COLOR_BGR2HSV)

# 2. 빨간색 범위를 HSV 형식으로 정의
lower_red = np.array([0, 100, 100]) # 낮은 범위
upper_red = np.array([10, 255, 255]) # 높은 범위

# 3. 범위에 해당하는 마스크 설정
mask = cv.inRange(hsv_img, lower_red, upper_red)
print(mask)

# 4. 마스크를 사용해서 원본이미지에서 빨간색 부분만 추출해보자.
red_part = cv.bitwise_and(hsv_img, hsv_img, mask=mask) # (원본이미지, 대상이미지, 기준)





# 저장
cv.imwrite('../img_res/hsv_img.jpg', hsv_img)

# 보여주기
cv.imshow('original', apple)
cv.imshow('red_part', red_part)
cv.imshow('hsv', hsv_img)
cv.waitKey(0)
cv.destroyAllWindows()
