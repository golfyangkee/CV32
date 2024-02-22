# 사과이미지에  +50   -50 ,  *2 , /2
import cv2
import numpy as np
apple_image = cv2.imread('../img/apple.jpg')

#  + ,  -  = 밝기 조절
#  * , /  = 대비조절
add_img  =  cv2.add(apple_image, np.array([50.0]) )
sub_img  = cv2.subtract(apple_image, np.array([100.0])   )
mul_img  =cv2.multiply(apple_image, 2) # 픽셀의 강도를 증가 -> 대비를 강화
div_img = cv2.divide(apple_image, 2)  # 픽셀의 강도를 감소  -> 대비를  약하게

scaled_image = cv2.convertScaleAbs(mul_img, alpha=2, beta=0) # div_img를 절대값으로 스케일하고 [추가조정]
# mul_img, div_img 등 다양하게 넣어보자.
# 이미지의 선형 변환을 수행
# alpha: 스케일링 계수입니다. 입력 이미지의 픽셀 값에 이 값을 곱하여 밝기를 조절합니다. 이 값은 실수형입니다.
# beta (선택적): 오프셋입니다. 이 값을 입력 이미지의 모든 픽셀 값에 더하여 밝기를 조절합니다. 이 값은 정수형입니다.

cv2.imshow("add" , add_img)
cv2.imshow("sub" , sub_img)
cv2.imshow("mul" , mul_img)
cv2.imshow("div" , div_img)
cv2.imshow("scaled_image" , scaled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
