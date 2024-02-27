# 2. 아래의 코드에서 빈칸을 채워서 이미지에서 도형을 감지하고, 감지된 도형 주위에
# Bounding Box를 그리는 프로그램을 완성해보세요. b_od.py

# 필요한 라이브러리를 import합니다.
import cv2
import numpy as np

# 이미지 파일을 불러옵니다.
img = cv2.imread('shape.jpg')

# 이미지를 그레이스케일로 변환합니다.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny 알고리즘을 사용하여 엣지를 검출합니다.
edges = cv2.Canny(gray, 50, 150)

# 외곽선을 찾습니다.
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 찾은 외곽선을 화면에 그립니다.
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 결과를 화면에 출력합니다.
cv2.imshow('Shape Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()