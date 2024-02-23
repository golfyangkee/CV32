import cv2
import numpy as np

# 엣지검출은 밝기 변화율에 따라 급격한 부분을 찾아내는 거다. 그걸 보고 경계라고 한다.
# 엣지의 원리를 가만히 정리해보면
# CV가 가지고 있는거는 채널값 밖에 없으니까
# tip: 엣지 검출 - 이미지의 밝기 변화율이 급격한 부분을 찾는 작업, 경계 또는 윤곽
# 소벨 = 이미지 + 미분
# scharr = 소벨 + 엣지 방향 + 강도
# canny = 가우시안 + 소벨

img = cv2.imread("../img/apple.jpg")
# img = cv2.imread("../img/Lenna.png")

gx_k = np.array([[ -3, 0,  3],
                 [-10, 0, 10],
                 [ -3, 0,  3]])

gy_k = np.array([[-3, -10, -3],
                 [ 0,   0,  0],
                 [ 3,  10,  3]])

edge_gx = cv2.filter2D(img, -1, gx_k) # 그레이스케일이 아니여서 색이 보인다.
edge_gy = cv2.filter2D(img, -1, gy_k) # ddepth = -1 type -1은 그대로 하겠다. CV64f, cv32f 이런거

# 소벨 연산의 확장형 (소벨에 미분을 더 더하자 이런 느낌)
scharrx = cv2.Scharr(img, -1, 1, 0) # dx dy x y축 미분하겠다 안 하겠다
scharry = cv2.Scharr(img, -1, 0, 1)

merged1 = np.hstack((img, edge_gx, edge_gy))
merged2 = np.hstack((img, scharrx, scharry))
merged = np.vstack((merged1, merged2))
cv2.imshow('Scharr', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

