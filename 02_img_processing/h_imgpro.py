'''
 << 폭이다른 이미지를 세로로 연결해보자.(단, 폭이 적은 데이터를 기준으로 조정하자.) >>
'''
# 함수 선언  resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
# 함수 선언  resize(이미지, 결과 영상크기(w,h)[ 결과영상[, fx[, fy[, interpolation =  보간법]]]])
#   fx  = factor
#  interpolation  =  cv2.INTER_LINEAR  (2*2)  /   CV2.INTER_CUBIC (4*4)  / CV2.INTER_AREA (영상대상 축소 )
# 늘리면 뭘로 채워야 하는데 뭘로 채울거야? linear로연산해서 cubic으로 연산해서, 너가 주는거로

import cv2 as cv
import numpy as np

im1 = cv.imread('../img/apple.jpg')
im2 = cv.imread('../img/Lenna.png')


# im.shape [0]는 높이 ,  [1] 폭
def my_resize(im_list, interpolation=cv.INTER_CUBIC):  # 2) 매개인자로 이미지를 받는다.

    # 1. 폭이 가장 작은 값을 리턴 받자.   : 폭의 기준
    w_min = min(im.shape[1] for im in im_list)

    # 2.폭의 사이즈를   재조정
    im_list_resize = [cv.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])),
                                interpolation=interpolation) for im in im_list]
    # << 이미지 재조정 후 속성값 추출 >>
    for i, im in enumerate(im_list_resize):
        print(f"Image {i}: dims = {im.ndim}, shape = {im.shape}, dtype = {im.dtype}")
        # Image
        # 0: dims = 3, shape = (210, 174, 3), dtype = uint8
        # Image
        # 1: dims = 3, shape = (174, 174, 3), dtype = uint8
        # Image
        # 2: dims = 3, shape = (210, 174, 3), dtype = uint8
        # 높이는 달라도 174로 맞춤

    return cv.vconcat(im_list_resize)  # 결합해서 리턴


im_v = my_resize([im1, im2, im1])  # 1) . 서로 다른  이미지를 함수로 대입 # 사과 레나 사과

cv.imwrite("img_res/v_img_resize.jpg", im_v)