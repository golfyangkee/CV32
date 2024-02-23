import cv2
import numpy as np

# img = cv2.imread("../img/apple.jpg")
img = cv2.imread("../img/Lenna.png")

# Laplacian은 필더링 중 하나 : 이미지에 이차 미분(노이즈와 관련 있다.) 연산하는 엣지 검출 중 하나
# 밝기 변화가 급격한 객체의 윤곽을 재확인할 때 사용한다. <전처리 확인>
# 방향성을 가지고 있찌 않은 연산을 하기 때문에 모든 방향에서 엣지를 동시에 검출 가능하다.

edge = cv2.Laplacian(img, -1)

merged = np.hstack((img, edge))
cv2.imshow('Laplacian', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()