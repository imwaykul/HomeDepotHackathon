import cv2



img = cv2.imread('image_0001.png')

scale = 1.5

imgSmaller = cv2.resize(img,(0,0),fx=scale,fy=scale)
cv2.circle(imgSmaller,(int(115*scale),int(229*scale)), 3, (0,255,0), -1)
cv2.circle(imgSmaller,(int(116*scale),int(245*scale)), 3, (0,255,0), -1)
cv2.circle(imgSmaller,(int(120*scale),int(270*scale)), 3, (0,255,0), -1)
cv2.imshow("face1Small",imgSmaller)


cv2.circle(img,(115,229), 3, (255,0,0), -1)
cv2.circle(img,(116,245), 3, (255,0,0), -1)
cv2.circle(img,(120,270), 3, (255,0,0), -1)

cv2.imshow("face1",img)

print (img.shape)
print (imgSmaller.shape)
cv2.waitKey(0)


