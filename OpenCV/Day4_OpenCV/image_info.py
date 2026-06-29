import cv2

img = cv2.imread("images/test.jpg")

print("左上角像素:")
print(img[0,0])

print("中心像素:")
h,w,_ = img.shape

print(img[h//2,w//2])