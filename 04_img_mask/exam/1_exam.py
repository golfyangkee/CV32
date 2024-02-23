'''
문제 1: 블러링을 이용한 배경 제거
1) 사과 이미지의 배경을 블러링 처리하여 객체(사과)를 더욱 돋보이게 만든다
2) 사과 이미지를 불러와서 배경을 블러링 처리한다.
3) cv2.GaussianBlur 함수를 사용하여 이미지에 가우시안 블러링을 적용하고, 사과 부분은 원본 그대로 유지한다.
   결과 이미지는 blurred_background_apple.jpg로 저장한다.
'''

# 가우시안 블러 적용
import cv2
import numpy as np

apple_image = cv2.imread('apples.jpg')

blurred_image = cv2.GaussianBlur(apple_image, (21, 21), 0)

'''
# 사과 부분을 위한 마스크 생성
mask = np.zeros(apple_image.shape[:2], np.uint8)
mask[100:300, 100:300] = 255

# 마스크를 이용하여 사과 부분만 원본에서 추출
apple_part = cv2.bitwise_and(apple_image, apple_image, mask=mask)

# 배경에 사과 부분을 합성
combined_image = cv2.bitwise_and(blurred_image, blurred_image, mask=cv2.bitwise_not(mask))
combined_image[mask == 255] = apple_part[mask == 255]
'''

# 결과 이미지 저장
cv2.imwrite('blurred_background_apple.jpg', blurred_image) # combined_image
