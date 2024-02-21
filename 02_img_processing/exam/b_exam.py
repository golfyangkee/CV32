# 1. 200*200 사이즈의 전체 파란색에 빨간색 사각형으로 채운 이미지를 생성하자.
# 2. 빨간색을 추출해보자. (마스크를 생서해서 마스크 값에 해당되면 추출하자)
import numpy as np
import cv2 as cv

# np.zeros() - 모든 값을 0 으로 채운다.
blue_img=np.zeros((200,200,3), dtype=np.uint8)
# blue_img=np.ones((200,200,3), dtype=np.uint8)*[255,0,0]

# 1. 파란색으로 인덱스에 데이터를 저장하자. [255,0,0] = [Blue, Green, Red]
blue_img[:, :] = [255, 0, 0]

# 2. 빨간색 사각형으로 채운 이미지
blue_img[50:150, 50:150] = [0, 0, 255] # BGR로 red 부분

# 3. 빨간색 범위를 BGR 형식으로 정의
lower_red = np.array([0, 0, 150])
upper_red = np.array([50, 50, 255])

# 4. 범위에 해당하는 마스크 설정
mask = cv.inRange(blue_img, lower_red, upper_red)
print(mask)

# 5. 마스크를 사용해서 원본이미지에서 빨간색 부분만 추출해보자.
red_part = cv.bitwise_and(blue_img, blue_img, mask=mask) # (원본이미지, 대상이미지, 기준)

# 저장
cv.imwrite('../img_res/blue_img.jpg', blue_img)

# 보여주기
cv.imshow('red_part', red_part)
cv.imshow('blue', blue_img)
cv.waitKey(0)
cv.destroyAllWindows()
