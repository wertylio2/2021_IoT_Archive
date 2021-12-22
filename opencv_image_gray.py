import cv2

img = cv2.imread('picture.jpg')
img2 = cv2.resize(img, (540,787))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('picture',img2)
cv2.imshow('picture_GRAY',gray)


while True:
    if cv2.waitKey() == ord('q'):
        break

cv2.imwrite('picture_gray.jpg',gray)
cv2.destroyAllWindows()
