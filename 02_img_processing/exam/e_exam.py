# apple.jpg 이미지에서 h, s, v만 각각 추출해서 h.txt, s.txt, v.txt로 저장해 보자.
import cv2 as cv
import numpy as np

# 읽기
apple=cv.imread('../../img/apple.jpg') # imread는 멀 해도 hsv를 읽어가지고 올 수 없다.

# 변환
hsv_img = cv.cvtColor(apple, cv.COLOR_BGR2HSV)

# H, S, V 채널 분리
H, S, V = cv.split(hsv_img) # Mat는 무조건 배열 객체를 가지고 와야 한다.
# print('H[0]',H[10,0:10])

# 각 채널을 파일로 저장하자.
np.savetxt('../img_res/e_h.txt', H, fmt='%d')
np.savetxt('../img_res/e_s.txt', S, fmt='%d')
np.savetxt('../img_res/e_v.txt', V, fmt='%d')

# 색상 범위 조정할 때, RGB보다 좀 더 사람한테 보여주게 직관적으로 보여준다.
# h는 색상채널인데 8 8 8 인데 범위 자체가 쉽게 접근할 수 있다. max=255