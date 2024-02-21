# 200*200 사이즈의 빨간색 채운 이미지를 생성하자.
# np.zeros() - 모든 값을 0 으로 채운다.

import numpy as np
import cv2 as cv

red_img=np.zeros((200,200,3), dtype=np.uint8)

# 빨간색으로 인덱스에 데이터를 저장하자. [0,0,255] = [Blue, Green, Red]
red_img[:,:]=[0,0,255]

cv.imwrite('../img_res/red_img.jpg', red_img)

cv.imshow('red', red_img)
cv.waitKey(0)
cv.destroyAllWindows()
