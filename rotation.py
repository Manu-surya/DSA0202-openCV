#9
import cv2
img = cv2.imread("C:\\Users\\ghant\\OneDrive\\Desktop\\tpt.jpg")

rotated_img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

rotated_img = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("rotated image.jpg",rotated_img)