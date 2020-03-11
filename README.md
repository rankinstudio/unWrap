# unWrap
Unwrap allsky (fisheye) images into rectilinear in Python

![](test.jpg)

Simple to use python script to unwrap an allsky or 360 deg RGB fisheye image into a panoramic rectilinear image.

Dependencies:<br>
imageio<br>
numpy<br>
opencv<br>

Tested:
Raspberry Pi 3/4

# usage
	from unWrap import unwrap
 	import imageio

 	image = imageio.imread('rgb.jpg')
 	result = unwrap(image, 40) #Here we are cropping 40px from the bottom of final pano. Set to 0 for disable.
 	imageio.imwrite('test.jpg', result)

