# red_img.png 이미지에서 b, g, r만 각각 추출해서 b.txt, g.txt, r.txt로 저장해 보자.
# 방법은 다양하나 이미지 읽어와서 찾는 거다.
# 인덱스 값으로 가지고 오는 방법 1
# bgr로 가지고 오는 방법 2
# x, y를 호출하면 채널(b,g,r)을 가지고 온다.
import cv2
import numpy as np

img=cv2.imread('../res/red_img.png')
print(img)

# B, G, R 채널 분리
B,G,R = cv2.split(img) # Mat는 무조건 배열 객체를 가지고 와야 한다.

# 각 채널을 파일로 저장하자.
np.savetxt('../res/b_b.txt',B,fmt='%d')
np.savetxt('../res/b_g.txt',G,fmt='%d')
np.savetxt('../res/b_r.txt',R,fmt='%d')