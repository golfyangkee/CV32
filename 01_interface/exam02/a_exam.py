#1.레나이미지를  컬러로 로드 한다  def load_image():
#2.그레이스케일로 색 공간을 변경 후  g_lenna.png로 저장한다.  def convert_to_grayscale():
#3.cv2의 resize()를 활용해서 200*200 으로 변경 후  r_lenna.png로  저장한다. def resize_and_save():
#4.트랙바를 사용해서 밝기를 조정한다.  def adjust_brightness(x):
import cv2
import numpy as np

# 이미지 로드 함수
def load_image():
    pass

# 그레이스케일로 변경 및 저장 함수
def convert_to_grayscale():
    pass

# 이미지 리사이즈 및 저장 함수
def resize_and_save():
   pass

# 밝기 조정 콜백 함수
def adjust_brightness(x):
   pass


if __name__ == '__main__':

    img = cv2.imread('../../img/Lenna.png')  # 레나 이미지 로드
    cv2.imshow('image', img)

    convert_to_grayscale()
    resize_and_save()

    # 트랙바 생성
    cv2.createTrackbar('Brightness', 'image', 50, 100, adjust_brightness)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
