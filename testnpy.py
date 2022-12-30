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
import matplotlib.pyplot as plt

x = np.load("1671875163_onefile.npy").view(np.uint16)
print(x.shape)

def convert_rggb_to_rgb(rggb):  # RGGB (x,y) --> RGB = (x/2,y/2,3)

    ret_arr = np.zeros((3, rggb.shape[0] // 2, rggb.shape[1] // 2)).astype(np.uint16)
    blue = rggb[1::2, 1::2]  # blue
    green1 = rggb[0::2, 1::2]  # green
    green2 = rggb[1::2, 0::2]  # green
    red = rggb[0::2, 0::2]  # red

    ret_arr[0] = ret_arr[0] + red
    ret_arr[1] = ret_arr[1] + (green1 + green2) / 2
    ret_arr[2] = ret_arr[2] + blue

    return ret_arr  # RGB = (x/2,y/2,3)

y = convert_rggb_to_rgb(x[0])
print(y.shape)

# method to assign only matric entries of the sky area (static circle)

def get_sky_area(radius, centre, img):

    cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR).astype(np.uint16)  # OpenCV uses BGR color space

    sky = cv2_img.copy()
    # create a black image with the same size as our
    # image that contains the moon, we then create
    # a white circle on the black image
    mask = np.zeros(sky.shape[:2], dtype="uint16")
    cv2.circle(mask, centre, radius, 255, -1)
    # apply the mask to our image
    masked = cv2.bitwise_and(sky, sky, mask=mask)
    avgR = np.mean(masked[:, :, 0])
    avgG = np.mean(masked[:, :, 1])
    avgB = np.mean(masked[:, :, 2])
    print("Mean of channel R: ", avgR)
    print("Mean of channel G: ", avgG)
    print("MEan of channel B: ", avgB)

    # cv2.imshow("sky", sky)
    # cv2.imshow("mask", mask)
    # cv2.imwrite('sky_image.png', masked[:,:,2])
    print("Saved Sky image as sky_image")
    # cv2.imshow("Mask applied to image", masked)
    # cv2.waitKey()
    return avgR, avgG, avgB

CENTRE = (512, 404)
RADIUS = 535

avgR, avgG, avgB = get_sky_area(radius=RADIUS, centre=CENTRE, img=y)

print(avgR)
print(avgG)
print(avgB)