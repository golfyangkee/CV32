import cv2 as cv
import numpy as np

im1 = cv.imread('../../img/apple.jpg')
im2 = cv.imread('../../img/Lenna.png')

# 사과, 레나, 레나  -> 가장 작은 폭과 넓이로 병합
def S_concat():  # s_concat.jpg
    # 1. 이미지 높이와 넓이를 찾아서 가장 적은 값을 구한다.
    min_height=min(im1.shape[0],im2.shape[0])
    min_width = min(im1.shape[1], im2.shape[1])

    # 2. resize()한다.
    im1_resize = cv.resize(im1, (min_width, min_height))
    im2_resize = cv.resize(im2, (min_width, min_height))

    # 3. 가로로 병합한다.
    im=cv.vconcat([im1_resize,im2_resize,im2_resize])  # 매개인자 리스트 객체이다.
    # s_concat_img = np.hstack((resized_im1, resized_im2, resized_im2)) # 매개인자 ()이다.

    # 4. 이미지 저장
    cv.imwrite("../img_res/s_concat.jpg", im)

# 사과, 사과, 레나  -> 가장 큰 폭과 넓이로 병합
def B_concat():  # b_concat.jpg
    # 1. 이미지 높이와 넓이를 찾아서 가장 적은 값을 구한다.
    max_height = max(im1.shape[0],im2.shape[0])
    max_width = max(im1.shape[1], im2.shape[1])

    # 2. resize()한다.
    im1_resize = cv.resize(im1, (max_width, max_height))
    im2_resize = cv.resize(im2, (max_width, max_height))

    # 3. 가로로 병합한다.
    im=cv.vconcat([im1_resize,im1_resize,im2_resize])

    # 4. 이미지 저장
    cv.imwrite("../img_res/b_concat.jpg", im)

S_concat()  # 사과 레나 사과
B_concat()   # 사과 사과 레나

