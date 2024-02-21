# 사과를 로드해서 밝기 조정을 해본다. + -
import cv2
import numpy as np
# 8bit = 0 ~ 255 = 어둡고 ~ 밝고
img=cv2.imread('../../img/apple.jpg')
value=np.ones_like(img)*50 # 밝기 조정할 픽셀값 50 증가할 값 | max 255까지 | 0 : 어둡다 , 1: 밝다
# print(value)

# 증가
img_add=cv2.add(img,value)

# 감소
img_sub=cv2.subtract(img,value)

# 보기
cv2.imshow('original',img)
cv2.imshow('add',img_add)
cv2.imshow('sub',img_sub)
cv2.waitKey(0)  # 아무 키나 받을때 까지 대기해라
cv2.destroyAllWindows()  # 모든 리소스 해제

