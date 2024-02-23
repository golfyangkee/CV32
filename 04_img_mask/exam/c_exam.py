# 문제 2에서 생성된 엣지 이미지에 대해 모폴로지 연산을 적용하여 엣지를 정제합니다.
import cv2
import numpy as np

def  case01():
    image = cv2.imread('Apples.jpg')
    edges = cv2.Canny(image, 100, 200)

    # 모폴로지 연산을 위한 커널 정의
    kernel = np.ones((3,3), np.uint8)

    # 엣지 이미지를 팽창시킨 후 침식
    dilated_edges = cv2.dilate(edges, kernel, )
    eroded_edges = cv2.erode(dilated_edges, kernel)

    # 결과 이미지 저장
    cv2.imwrite('refined_edges_apple.jpg', eroded_edges)

def case02():
    image = cv2.imread('Apples.jpg' , cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(image, 100, 200)
    # 모폴로지 연산을 위한 커널 정의
    k = np.ones((3, 3), np.uint8)
    #k = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    # morphologyEx() 함수를 사용하여 열림 연산을 적용 후  닫힘연산 적용
    refined_edges_ex = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, k)
    cv2.imwrite('refined_edges_apple02.jpg', refined_edges_ex)

case01()
case02()