'''
1 apple.jpg 이미지를 컬러로 로드
2 이미지를 HSV 색 공간으로 변환하고 hsv_apple.png로 저장
3. 이미지의 크기를 300x300으로 조정하고 resized_apple.png로 저장
4. 트랙바를 사용하여 이미지의 채도(Saturation)를 조정한다.
'''
import cv2
import numpy as np

img = cv2.imread('../../img/apple.jpg')

# HSV 색 공간으로 변환 및 저장
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imwrite('hsv_apple.png', hsv_img)

# 이미지 크기 조정 및 저장
resized_img = cv2.resize(img, (300, 300))
cv2.imwrite('resized_apple.png', resized_img)

# 채도 조정 콜백 함수
def adjust_saturation(x):
    saturation = cv2.getTrackbarPos('Saturation', 'image')
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 색상, 채도, 밝기

    #트랙바로 가져온 채도값을 더하겠다.
    hsv_img[:, :, 1] = cv2.add(hsv_img[:, :, 1], saturation)
    adjusted_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)

    cv2.imshow('image', adjusted_img)

# 이미지 표시 및 트랙바 생성
cv2.imshow('image', img)
cv2.createTrackbar('Saturation', 'image', 0, 255, adjust_saturation)
cv2.waitKey(0)
cv2.destroyAllWindows()
