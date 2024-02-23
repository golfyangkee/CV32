'''
문제 3: 모폴로지 연산을 이용한 엣지 정제
1) 엣지 검출 결과를 정제하여 더욱 명확한 객체의 윤곽선을 얻는다.
2) 문제 2에서 생성된 엣지 이미지에 모폴로지 연산을 적용한다.
3) cv2.dilate와 cv2.erode 함수를 이용하여 엣지를 각각 팽창시킨 후 침식시켜서 정제된 엣지를 생성후
   결과 이미지는 refined_edges_apple.jpg로 저장한다.
4) morphologyEx()도 사용하여 refined_edges_apple02.jpg 로 저장하자.
'''
import cv2
import numpy as np

def case01():
    image = cv2.imread('apples.jpg')
    edges= cv2.Canny(image,100,200)

    # 모폴로지 연산을 위한 커널 정의
    kernel = np.ones((3,3), np.uint8)

    # 엣지 이미지를 팽창시킨 후 침식
    eroded_edges = cv2.erode(image, kernel)

    # 결과 이미지 저장
    cv2.imwrite('refined_edges_apple01.jpg', eroded_edges)
def case02():
    image = cv2.imread('apples.jpg', cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, 100, 200)

    # 모폴로지 연산을 위한 커널 정의
    k = np.ones((3, 3), np.uint8)

    # k=cv2.getStructuringElement(cv2.MORHP_RECT, (7,7))
    # morphologyEx() 함수를 사용하여 열림 연산을 적용 후 닫힘 연산 적용
    refined_edges_ex = cv2.morphologyEx(edges, cv2.MORPH_OPEN, k) # OPEN 말고 CLOSE를 줘보자.
    cv2.imwrite('refined_edges_apple02.jpg', refined_edges_ex)


case01()
case02()

