import numpy as np
import cv2 as cv

# np.zeros() - 모든 값이 0인 배열 생성
zeros_array = np.zeros((3, 3))
print("Zeros Array:\n", zeros_array, "\n")

# np.ones() - 모든 값이 1인 배열 생성
ones_array = np.ones((3, 3))
print("Ones Array:\n", ones_array, "\n")
cv.imwrite("img_res/a.png",ones_array)

################이미지 생성 ===========================
# 이미지 크기  640*480
ones_array = np.ones((640, 480,3),dtype=np.uint8) *255
print("Ones Array:\n", ones_array, "\n")
cv.imwrite("img_res/a1.png",ones_array)



# np.full() - 모든 값이 특정 값으로 채워진 배열 생성
# 경계가 모호할 때 특정 색으로 채우고 싶을 때 사용
full_array = np.full((3, 3), 7)
print("Full Array with 7:\n", full_array, "\n")

# np.eye() - 단위 행렬 생성
eye_array = np.eye(5)
print("Eye Array:\n", eye_array, "\n")

# np.fliplr() - 행렬의 왼쪽과 오른쪽을 뒤집기
# 오른쪽 대각선은 만드는 함수는 없어서 eye를 뒤집어서 사용 - 많이 사용
# 저수준은 원본은 나두고 사이즈 조절 등 외부요소만 조정
flipped_eye_array = np.fliplr(eye_array)
print("Flipped Eye Array:\n", flipped_eye_array, "\n")

# np.linspace() - 선형 간격의 배열 생성   :  소리 음파 확인  -> 파형 생성
# 노이즈 생성 후 추가 _ 테스트용
linspace_array = np.linspace(0, 10, 30)
print("Linspace Array from 0 to 10 with 30 elements:\n", linspace_array, "\n")

# np.arange() - 주어진 간격으로 배열 생성
arange_array = np.arange(0, 51, 5)
print("Arange Array from 0 to 50 with step 5:\n", arange_array, "\n")
