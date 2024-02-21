# 같은 이미지를 세로로 연결 해보자.
import cv2 as cv
import numpy as np

im1 = cv.imread("../img/apple.jpg")
im2 = cv.imread("../img/Lenna.png")

print(f'apple.jpg shape ={im1.shape}  Lenna.png shape ={ im2.shape}'  )
# apple.jpg shape =(270, 223, 3)  Lenna.png shape =(174, 174, 3)

im_v  = cv.vconcat([im1, im1])
cv.imwrite("img_res/v_img.jpg" ,im_v)
'''
im_v02=np.tile(im1,(2,1,1)) 해석:
해당 코드는 NumPy의 tile 함수를 사용하여 이미지를 복제하는 것으로 보입니다. 
여기서 im1은 이미지를 나타내는 NumPy 배열입니다.

np.tile(im1, (2, 1, 1)): 이 부분은 im1이라는 이미지를 타일 형태로 복제하는 역할을 합니다. 
np.tile 함수는 배열을 복사하여 원하는 형태로 쌓는 데 사용됩니다. 
여기서 첫 번째 인자는 복제할 배열이고, 두 번째 인자는 각 차원별로 몇 번 복제할지를 나타내는 튜플입니다.
(2, 1, 1)은 첫 번째 차원을 따라서 2번 복제하고, 두 번째와 세 번째 차원을 따라서는 1번씩만 복제하라는 의미입니다.
따라서 결과적으로는 이미지를 첫 번째 차원(행)을 따라서 2번 반복하여 쌓은 것과 같은 결과를 얻게 됩니다.
결과적으로, im_v02에는 im1을 첫 번째 차원을 따라 2번 반복하여 쌓은 이미지가 저장됩니다. 
이를 통해 이미지를 확장하거나 반복하여 사용할 수 있습니다.
'''
im_v02=np.tile(im1,(2,1,1))
cv.imwrite("img_res/v_img02.jpg",im_v02)


im_v03=np.tile(im2,(2,1,1))
cv.imwrite("img_res/v_img03.jpg",im_v03)