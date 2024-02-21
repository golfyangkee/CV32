import cv2
# cv::circle (InputOutputArray img, Point center, int radius, const Scalar &color, int thickness=1, int lineType=LINE_8, int shift=0)
img = cv2.imread('../img/bg.jpg')

# 원점(150,150), 반지름 100
cv2.circle(img, (150, 150), 100, (255,0,0))     

# 원점(300,150), 반지름 70
cv2.circle(img, (300, 150), 70, (0,0,255))

# 원점(50,300), 반지름 50, 회전 0, 각도 360
# cv::ellipse (InputOutputArray img, Point center, Size axes, double angle, double startAngle, double endAngle, const Scalar &color, int thickness=1, int lineType=LINE_8, int shift=0)
# cv.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]]	) ->	img
cv2.ellipse(img, (50, 300), (50,50), 0,0,360, (0,255,0))

# 아래 반원 그려보자
cv2.ellipse(img, (150, 300), (50,50), 0,0,180, (0,255,0))

# 윗 반원 그려보자
cv2.ellipse(img, (250, 300), (50,50), 90,181,360, (0,255,0))

# 원점 (200,400) 반지름 (50,100), 회전각도 15도
cv2.ellipse(img, (200, 400), (50,100), 15,0,180, (100,100,100))

cv2.imshow('circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()