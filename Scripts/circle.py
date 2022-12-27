import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# path
#path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'

# Reading an image in default mode
image = cv2.imread('0376_sky.jpg')

# Window name in which image is displayed
window_name = 'Image'

# Center coordinates
center_coordinates = (2028, 2028)

# Radius of circle
radius = 50

# Blue color in BGR
color = (255, 0, 0)

# Line thickness of 2 px
thickness = 2

# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness)

# Displaying the image
#cv2.imshow(window_name, image)
#cv2.waitKey(5000)

array = np.arange(0, image.size, 1, np.uint8)
array = np.reshape(array, (3040, 3040))

im = image.fromarray(array)
im.save("0376c.jpeg")














#array = np.arange(0, 49353408, 1, np.uint8)
#array = np.reshape(array, (4056, 4056))

#cv2.imwrite('filename.jpeg', array)
#plt.imsave('0376c.jpg', image)
#print(type(image))
#print(image.size)

#array = np.reshape(image, (312,312))
#data = Image.fromarray(array)
#data.save('segmented.png')


#cv2.imwrite(image, '376circ.jpg')

