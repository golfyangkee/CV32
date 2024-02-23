#### bilateralFilter
import cv2
import numpy as np

# img = cv2.imread("../img/apple.jpg")
img = cv2.imread("../img/Lenna.png")

# 가우시안 필터 적용
blur1 = cv2.GaussianBlur(img, (5,5), 0)

# 바이레터럴 필터 적용 /  = 양방향 필터
blur2 = cv2.bilateralFilter(img, 5, 75, 75)
# 엣지를 보전하면서 하니까 블러를 해도 선명해 보인다.

# 결과 출력
merged = np.hstack((img, blur1, blur2))
cv2.imshow('bilateral', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
