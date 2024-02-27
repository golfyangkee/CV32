# 3. Object detection을 위해 라벨링을 하는 과정에서 각 객체의 윤곽선이나 경계 상자
# (bounding box) 정보를 사용하게 됩니다. 이 정보를 이용해서 객체별로 특징점을 추
# 출하고 라벨링할 수 있습니다. 아래 키워드 힌트를 사용해서 코드를 완성하세요
# 이미지 파일은 그림판에서 0~ 9 까지 무순위로 작성한 그림을 사용합니다.
# [키워드 힌트]c_od.py
import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread('image.jpg')

# 그레이스케일로 변환s
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이진화
_, binary_img = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# 윤곽선 찾기
contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# SIFT 객체 생성
sift = cv2.xfeatures2d.SIFT_create()

# 객체를 탐지하고 라벨링
for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    roi = gray[y : y+h, x : x+w]

    # 특징점 추출
    keypoints, descriptors = sift.detectAndCompute(roi, None)

    # 원래 이미지에 특징점 표시 (라벨링을 위한 예)
    for point in keypoints:
        transformed_x, transformed_y = int(x + point.pt[0]), int(y + point.pt[1])
        cv2.circle(image, (transformed_x, transformed_y), 3, (0, 255, 0), -1)

    # 라벨 표시 (여기서는 i를 라벨로 사용)
    cv2.putText(image, str(i), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# 결과 이미지 표시
cv2.imshow('Labeled Objects with Keypoints', image)
cv2.waitKey(0)
cv2.destroyAllWindows()