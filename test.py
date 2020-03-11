from unWrap import unwrap
import imageio
import numpy as np

'''
A test script showing how to unwrap an allsky jpg, then rotate N center.
'''

image = imageio.imread('startrails.jpg')
result = unwrap(image, 0)

#GET WIDTH, DIVIDE BY 2, MINUS 1
w = result.shape[1]
wh = int(w / 2)
w1 = w - 1

#CUT FIRST HALF
result1 = result[:, 0:wh]
#CUT SECOND HALF
result2 = result[:, wh:w1]
#STITCH BACK TOGETHER ON X AXIS
result = np.concatenate([result2, result1], 1)  # combine on x axis
#FLIP IMAGE
result = np.flip(result, 1)  # flip on x axiz
#CONVERT UINT8
result = np.uint8(result)  # Convt to uint8
#SAVE
imageio.imwrite('test.jpg', result)