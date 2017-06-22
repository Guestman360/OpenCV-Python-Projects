import cv2

img = cv2.imread("seattle.jpg",-1)

print(type(img))
print(img.shape)

cv2.imshow("City",img)
cv2.waitKey(2000)
cv2.destroyAllWindows()
