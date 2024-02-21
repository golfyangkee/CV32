# 임의의 이미지를 생성해 보자.
# numpy.zeros(크기, 타입)를 사용해서 값 대입을 해보자.
import cv2
import numpy as np  # 배열 객체 관리 (Create, Read, Update, Delete)

red_img = np.zeros((100,100,3), dtype=np.uint8) # 3차원 곽괄호 3개 면, 행, 열
# 위 쉐입으로 그려놓고 나면 red_img[행(높이), 열(너비), 색상채널] 3개의 인덱스를 가질 수 있다.
# print(red_img)

# #### 모든 행, 모든 열에 빨간색을 넣어라  a_red_img1.png
red_img [:,:] = [0,0,255]  # B, G, R로 관리   # 모든 행 , 모든 열에 0,0,255 를 넣어라
cv2.imwrite('../res/a_red_img1.png', red_img,)



# #### (0,0)에만 빨간색을 넣어라  a_red_img2.png
red_img[0,0]=[0,0,255] # B, G, R
# #### (0,1)에만 파란색을 넣어라  a_red_img2.png
red_img[0,1]=[255,0,0] # B, G, R
cv2.imwrite('../res/a_red_img2.png', red_img,)



# #### 전체 빨강에 중앙만 녹색을 넣어라  a_red_img3.png
red_img[:,:]=[0,0,255] # B, G, R -> 전체를 red
red_img[:,50]=[0,255,0]
cv2.imwrite('../res/a_red_img3.png', red_img,)



# #### 전체 빨강에 48~52라인(행)의 모든 컬럼과 세로 중앙(행)을 녹색으로 넣어라  a_red_img4.png
red_img[:,:]=[0,0,255] # B, G, R -> 전체를 red
red_img[48:53,:]=[0,255,0]  # start : end-1 : step
red_img[:,50]=[0,255,0]
cv2.imwrite('../res/a_red_img4.png', red_img,)
cv2.imwrite('../res/red_img.png', red_img,)
print(red_img)
print(red_img.shape)
print(red_img[50,50])







