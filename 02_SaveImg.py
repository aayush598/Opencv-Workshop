import cv2

img = cv2.imread("car.jpg")

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )

cv2.imwrite('gray_car.jpg', img2)

