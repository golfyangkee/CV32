# cv2모듈에서는 환경설정 구성할 때  녹색조 적용된 함수를 사용 한다.

# cv에서 사용되는  BT.601 공식이 적용된 속성
import cv2 as cv
# 읽어 올 때 grayscale로
im_gray_read = cv.imread("../img/apple.jpg",cv.IMREAD_GRAYSCALE) # os 코덱에 따라 화소가 다르다
print(type(im_gray_read))
print(im_gray_read.shape)  # 행, 열, 색상  =  높이 , 폭, 채널
print(im_gray_read.dtype)

# 이미지 읽어온 후에  회색조 변경
im = cv.imread("../img/apple.jpg") # os 코덱에 따라 화소가 다르다
im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY) # BT.601 적용  _ 정적연산 : 녹색계수 알고리즘 601로 적용한 것
print(type(im_gray))
print(im_gray.shape)  # 행, 열, 색상  =  높이 , 폭, 채널
print(im_gray.dtype)

# 판별
im_diff = im_gray.astype(int) - im_gray_read.astype(int)
print(im_diff.max())  # 6
print(im_diff.min())  # -15
# 차이가 난다.

# 읽어올 때 grayscale로 일반 채널을 단일채널로만 녹색계수 적용 X
# BT.601 녹색계수 적용 - 회사에서는 cvtColor로 쓴다.