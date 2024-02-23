'''
문제 2: 엣지 검출을 통한 객체 윤곽 추출
1) 사과 이미지에서 객체의 윤곽(엣지)을 검출한다.
2) 사과 이미지를 불러와서 엣지 검출을 수행한다.
3) cv2.Canny 함수를 사용하여 엣지를 검출하고, 검출된 엣지만을 포함하는 새 이미지를 생성한다.
   결과 이미지는 apple_edges.jpg로 저장한다.
'''

# 이미지를 불러온 후 Canny 엣지 검출 알고리즘을 사용하여 엣지를 검출합니다.

import cv2 as cv

apple_image=cv.imread('apples.jpg')

edges = cv.Canny(apple_image,100,200)

# 결과 출력
cv.imshow('Original', apple_image)
cv.imshow('Canny', edges)
cv.waitKey(0)
cv.destroyAllWindows()
