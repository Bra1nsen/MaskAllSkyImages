import numpy as np
import cv2

#height, width = 4056, 4056
#img = np.zeros((height, width, 3), np.uint8)
#img[:, :] = [255, 255, 255]


hoehe = 2500
pixelwidth= 0.00268308 * hoehe
imagewidth: 5.49495 * hoehe


numberpixel1km = 1000/pixelwidth



image = cv2.imread('4_sky.jpg')
# Pixel position to draw at
row, col = 1024, 1024

cv2.circle(image, (col, row), 0, (0,0,0), 13)
cv2.circle(image,(col, row), 150, (0,0,0), 2)
cv2.circle(image,(col, row), 300, (0,0,0), 2)
cv2.circle(image,(col, row), 450, (0,0,0), 2)
cv2.circle(image,(col, row), 600, (0,0,0), 2)
cv2.circle(image,(col, row), 750, (0,0,0), 2)
cv2.circle(image,(col, row), 900, (0,0,0), 2)

#kreuz
cv2.line(image,(0,1024),(2048,1024),(0,0,0),3)
cv2.line(image,(1024,0),(1024,2048),(0,0,0),3)
#diagonale
cv2.line(image,(0,2048),(2048,0),(0,0,0),3)
cv2.line(image,(0,0),(2048,2048),(0,0,0),3)

#text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'140 deg',(50,100), font, 3,( 255,255,255),2)
#cv2.putText(image,'Pixel width:',(1950,75), font, 2.5,( 255,255,255),2)
#cv2.putText(image,'0.00268308 * H',(2000,100), font, 2.5,( 255,255,255),2)
cv2.putText(image,'0',(990,1024), font, 1.5,( 0,0,0),2)
cv2.putText(image,'0,4*H',(950,868), font, 1.5,( 0,0,0),2)
cv2.putText(image,'0,8*H',(950,720), font, 1.5,( 0,0,0),2)
cv2.putText(image,'1,2*H',(950,570), font, 1.5,( 0,0,0),2)
cv2.putText(image,'1,6*H',(950,420), font, 1.5,( 0,0,0),2)
cv2.putText(image,'2,0*H',(950,270), font, 1.5,( 0,0,0),2)
cv2.putText(image,'2,4*H',(950,123), font, 1.5,( 0,0,0),2)

cv2.putText(image,'NORD 0',(880,50), font, 1.5,( 0,0,0),2)
cv2.putText(image,'WEST 270',(10,1015), font, 1.5,( 0,0,0),2)
cv2.putText(image,'EAST 90',(1850,1015), font, 1.5,( 0,0,0),2)
cv2.putText(image,'SOUTH 180',(850,2010), font, 1.5,( 0,0,0),2)

cv2.imwrite("4_sky_rot.jpg", image)
