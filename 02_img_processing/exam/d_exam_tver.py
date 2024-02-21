
import cv2 as cv
import numpy as np

im1 = cv.imread('../../img/apple.jpg')
im2 = cv.imread('../../img/Lenna.png')

#  사과,레나,레나    -> 가장 작은 폭과 넓이로  병합
def  S_concat() :   # s_concat.jpg
    # 1. 이미지  높이와 넓이를 찾아서 가장 적은 값을 구한다.
    min_height =min(im1.shape[0], im2.shape[0])
    min_width = min(im1.shape[1], im2.shape[1])

    #2. resize() 한다.
    resized_im1 = cv.resize(im1, (min_width, min_height))
    resized_im2 = cv.resize(im2, (min_width, min_height))

    #3. 가로로 병합 한다.
    s_concat_img = np.hstack((resized_im1, resized_im2, resized_im2))  # cv.vconcat(),  cv.hconcat()

    #4. 이미지 저장
    cv.imwrite('../img_res/s_concat.jpg', s_concat_img)

#  사과,사과,레나    -> 가장 큰 폭과 넓이로  병합
def  B_concat() :  # b_concat.jpg

    # 1. 이미지의 높이와 넓이를 찾아서 가장 큰 값을 구한다.
    max_height = max(im1.shape[0], im2.shape[0])
    max_width = max(im1.shape[1], im2.shape[1])

    #2. 이미지를 가장 큰 높이와 넓이로 조정
    resized_im1 = cv.resize(im1, (max_width, max_height))
    resized_im2 = cv.resize(im2, (max_width, max_height))

    #3.이미지를 가로로 병합
    b_concat_img = np.hstack((resized_im1, resized_im1, resized_im2))

    # 결과 이미지 저장
    cv.imwrite('../img_res/b_concat.jpg', b_concat_img)

S_concat()
B_concat()



