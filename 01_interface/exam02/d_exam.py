# 1. 5*5  크기의 이미지를 만들자 . 모든 픽셀을 1로 채우자.  np.ones
# 2. 5*5 크기를 만들자, 마스크의 중앙에 1을 놓고 나머지는 0으로 채우자. np.zeros
#3. 생성된 이미지에 마스크를 적용하고 결과를 c.png로 저장 결과를 출력하자. cv2.filter2D

import cv2
import numpy as np

# 1. 이미지 생성
original_image=np.ones((5,5), dtype=np.uint8)*255 # 밝기 값 지정

# 2. 마스크 생성
mask=np.zeros((5,5),dtype=np.uint8)
mask[2,2]=1 # 중앙에 1를 지정
cv2.imwrite('d_mask.png', mask*255) # 마스크 중앙을 255로 설정

# 3. 마스크 적용 : 경계 검출 시 사용 -> 노이즈 제거, 특징(X) 패턴 검출
# 필터랑 비트연산이랑 많이 다르다.
result_image=cv2.filter2D(original_image,-1,mask)
cv2.imwrite('d_filter.png', result_image*255)

# 4. 비트 And 연산
bit_image=cv2.bitwise_and(original_image, result_image*255)
cv2.imwrite('d_bit_image.png', bit_image)