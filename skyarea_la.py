#method to assign only matric entries of the sky area (static circle)

import glob
import numpy as np
import pandas as pd
from PIL import Image
import numpy as np
import cv2
import numpy as np
from numpy import asarray, save
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def get_sky_area(radius, centre, image_name):
    img = Image.open(str(image_name))
    cv2_img = np.array(img)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_RGB2BGR)
    
    sky = cv2_img.copy()
    # create a black image with the same size as our 
    # image that contains the moon, we then create
    # a white circle on the black image
    mask = np.zeros(sky.shape[:2], dtype="uint8")
    cv2.circle(mask, centre, radius, 255, -1)
    # apply the mask to our image
    masked = cv2.bitwise_and(sky, sky, mask=mask)
    avgR = np.mean(masked[:,:,2])
    avgG = np.mean(masked[:,:,1])
    avgB = np.mean(masked[:,:,0])
    print("Mean of channel R: ", avgR)
    print("Mean of channel G: ", avgG)
    print("MEan of channel B: ", avgB)
    
    #cv2.imshow("sky", sky)
    #cv2.imshow("mask", mask)
    #cv2.imwrite('sky_image.png', masked[:,:,2])
    print("Saved Sky image as sky_image")
    #cv2.imshow("Mask applied to image", masked)
    #cv2.waitKey()
    return avgR, avgG, avgB
    
    
CENTRE= (574, 335)
RADIUS = 353   
IMAGE_NAME = "1669190042_1700.tga"
avgR, avgG, avgB = get_sky_area(radius = RADIUS, centre = CENTRE, image_name=IMAGE_NAME)


rggb_sky=circled(r,c)

avg = np.average(rggb_sky)
print(avg)

How to express the masking of a circle for numpy calculations ?

[example_image][1]


  [1]: https://i.stack.imgur.com/ecDTI.png

