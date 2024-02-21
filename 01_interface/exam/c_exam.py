# apple.jpg 이미지에서 b, g, r만 각각 추출해서 b.txt, g.txt, r.txt로 저장해 보자.
import cv2
import numpy as np

# 읽기
img=cv2.imread('../../img/apple.jpg')
print(img)

# B, G, R 채널 분리
B,G,R = cv2.split(img) # Mat는 무조건 배열 객체를 가지고 와야 한다.

# 각 채널을 파일로 저장하자.
np.savetxt('../res/c_b.txt',B,fmt='%d')
np.savetxt('../res/c_g.txt',G,fmt='%d')
np.savetxt('../res/c_r.txt',R,fmt='%d')