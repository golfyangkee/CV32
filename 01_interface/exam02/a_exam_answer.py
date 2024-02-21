#1.레나이미지를  컬러로 로드 한다  def load_image():
#2.그레이스케일로 색 공간을 변경 후  g_lenna.png로 저장한다.  def convert_to_grayscale():
#3.cv2의 resize()를 활용해서 200*200 으로 변경 후  r_lenna.png로  저장한다. def resize_and_save():
#4.트랙바를 사용해서 밝기를 조정한다.  def adjust_brightness(x):
import cv2
import numpy as np

# 이미지 로드 함수
def load_image(image_file):
    img = cv2.imread(image_file,-1)  # 레나 이미지 로드
    return img

# 그레이스케일로 변경 및 저장 함수
def convert_to_grayscale(img):
    r_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return r_img

# 이미지 리사이즈 및 저장 함수
# 	cv.resize(	src, dsize[, dst[, fx[, fy[, interpolation]]]]	) ->	dst
def resize_and_save(img):
   resize_img=cv2.resize(img, (500, 500))
   return resize_img

# 밝기 조정 콜백 함수
def adjust_brightness(img, x):
    value = np.ones_like(img) * 50
    img_add = cv2.add(img, value)
    img_sub = cv2.subtract(img, value)
    if x=='+':
        return img_add
    elif x=='-':
        return img_sub


if __name__ == '__main__':
    image_file='../../img/Lenna.png'
    img=load_image(image_file)

    con_img = convert_to_grayscale(img)

    resize_img=resize_and_save(con_img)

    cv2.namedWindow('image')
    # create trackbars for color change
    cv2.createTrackbar('R','image',0,255,adjust_brightness)
    cv2.createTrackbar('G','image',0,255,adjust_brightness)
    cv2.createTrackbar('B','image',0,255,adjust_brightness)
    # create switch for ON/OFF functionality
    # switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar('Brightness', 'image',50,100,adjust_brightness)
    while(1):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        # get current positions of four trackbars
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G','image')
        b = cv2.getTrackbarPos('B','image')
        s = cv2.getTrackbarPos('Brightness','image')
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]
    cv2.destroyAllWindows()