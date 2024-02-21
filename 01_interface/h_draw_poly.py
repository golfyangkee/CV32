import cv2
import numpy as np                          # 좌표 표현을 위한 numpy 모듈
# cv.polylines(	img, pts, isClosed, color[, thickness[, lineType[, shift]]]	) ->	img

img = cv2.imread('../img/bg.jpg')

# Numpy array로 좌표 생성
# 번개 모양 선 좌표
pts1 = np.array([[50,50], [150,150], [100,140],[200,240]], dtype=np.int32) 
# 삼각형 좌표
pts2 = np.array([[350,50], [250,200], [450,200]], dtype=np.int32) 
# 삼각형 좌표
pts3 = np.array([[150,300], [50,450], [250,450]], dtype=np.int32) 
# 5각형 좌표
pts4 = np.array([[350,250], [450,350], [400,450], [300,450], [250,350]],\
                 dtype=np.int32) 

# 다각형 그리기
cv2.polylines(img, [pts1], False, (255,0,0))       # 번개 모양 선 그리기
cv2.polylines(img, [pts2], False, (0,0,0), 10)     # 3각형 열린 선 그리기
cv2.polylines(img, [pts3], True, (0,0,255), 10)    # 3각형 닫힌 도형 그리기
cv2.polylines(img, [pts4], True, (0,0,0))          # 5각형 닫힌 도형 그리기
# isClosed를 False 주면 열린거가 되고 True를 되면 닫힌거로 된다. False의 경우 좌표가 맞물려도 닫아지지 않는다.

cv2.imshow('polyline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()