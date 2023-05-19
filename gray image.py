import cv2

img = cv2.imread('C:\\Users\\ghant\\OneDrive\\Desktop\\shin.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray_image.jpg', gray_img)
