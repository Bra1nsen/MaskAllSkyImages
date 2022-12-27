 ## Fisheye All Sky Images ##
 
#1 original1 with shape = (1014,760) sky_circle1: -r 393 -c 574 335

#2 original2 with shape = (2032,1520) sky_circle2: -r 1070 -c 1024 804
----------------------
Idea:  Only Calculate with Sky Area Pixels (Solarpoweranalysis)

Measured Fisheye:


x=2032
y=1520
Megapixel = x*y
rggb = np.zeros(Megapixel).reshape(2032,1520) 

#method to assign only matric entries of the sky area (static circle)

def circled(radius=1070 ,center=(1024,804)):


rggb_sky=circled(r,c)

avg = np.average(rggb_sky)
print(avg)

How to express the masking of a circle for numpy calculations ?

[example_image][1]


  [1]: https://i.stack.imgur.com/ecDTI.png
