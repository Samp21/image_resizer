import cv2

path = 'resources/tv01.jpg'
img = cv2.imread(path)

# print size of image - height, width, depth
print(img.shape)

width, height = 400, 400
imgResize = cv2.resize(img, (width, height))
print(imgResize.shape)

# imgCropped = img[]

# displays the image
# first param is the name on the title bar when the image opens
# second param is the filename
cv2.imshow('TV', img)
cv2.imshow('TV Resized', imgResize)

cv2.waitKey(0)
