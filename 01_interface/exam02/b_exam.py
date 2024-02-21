'''
1 apple.jpg 이미지를 컬러로 로드
2 이미지를 HSV 색 공간으로 변환하고 hsv_apple.png로 저장 cv2.color로
3. 이미지의 크기를 300x300으로 조정하고 resized_apple.png로 저장
4. 트랙바를 사용하여 이미지의 채도(Saturation)를 조정한다.
'''
import cv2


def adjust_saturation(x):
    saturation = cv2.getTrackbarPos('Saturation','image')
    hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # 트랙바로 가져온 채도값을 더하겠다.
    hsv_img[:,:,1] = cv2.add(hsv_img[:,:,1],saturation)
    adjusted_img=cv2.cvtColor(hsv_img,cv2.COLOR_HSV2BGR)

    cv2.imshow('image',adjusted_img)

cv2.imshow('image',img)
cv2.createTrackbar('Saturation','image',0,255,adjust_saturation)