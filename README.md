# unWrap
Unwrap allsky (fisheye) images into rectilinear in Python

Simple to use python script to unwrap an allsky or 360 deg RGB fisheye image into a panoramic rectilinear image.

Dependencies:
imageio
numpy
opencv

Tested:
Raspberry pi 3/4

# installation
sudo apt-get install python3-scipy<br>
sudo apt-get install python-opencv<br>
sudo pip3 install imageio<br>

# usage
	from unWrap import unwrap
 	import imageio

 	image = imageio.imread('rgb.jpg')
 	result = unwrap(image, 40)
 	imageio.imwrite('test.jpg', result)

