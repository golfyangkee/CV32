import cv2      #  설치된 cv2 모듈을  참조하겠다.

img_file = "../img/apple.jpg"
img = cv2.imread(img_file,cv2.IMREAD_REDUCED_COLOR_4) # 컬러로 읽어서 해당 속성의 숫자 크기로 리턴

if img is not None:
    cv2.imshow('IMG', img)
    cv2.waitKey()
    # cv2.destroyAllWindows()
else:
    print('No image file.')
    