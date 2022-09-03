import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (100,60), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))





cv2.putText(img, "Mercury", (120,180), cv2.FONT_HERSHEY_COMPLEX, 0.4, (204,255,255))





cv2.putText(img, "Venus", (180,260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (175,1,134))





cv2.putText(img, "Earth", (280,170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (208,224,64))






cv2.putText(img, "Mars", (380,260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (128,128,255))







cv2.putText(img, "Jupiter", (450,100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,255))








cv2.putText(img, "Saturn", (760,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,0))









cv2.putText(img, "Uranus", (960,130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (204,153,255))









cv2.putText(img, "Neptune", (1110,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,153,153))


cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("solar_system.jpg", img)


#Mars, Jupiter, Saturn, Uranus, Neptune