from unWrap import unwrap
import imageio
import numpy as np
import os
from time import sleep
from shutil import copyfile

'''
A test script using the  thomasjacquin / allsky project
Put unWrap.py and allsky-test.py in the allsky directory
Call process_img with two args. Your allsky image, and a rotateN boolean

Add to a cron job like so:

sudo crontab -e
*/1 * * * * cd /home/pi/allsky && sudo python3 allsky-test.py
'''

def check_size(image):
    statinfo = os.stat(image)
    size = statinfo.st_size
    return size

def process_img(image, rotateN):

    #ENSURE IMAGE IS NOT BEING WRITTEN TO
    size1 = check_size(image)
    sleep(0.5)
    size2 = check_size(image)

    #IF NOT WRITING, PROCEED
    if size1 == size2:

        #COPY TO TEMP IMAGE
        temp = 'temp.jpg'
        copyfile(image, temp)

        #OPEN TEMP IMAGE
        image = imageio.imread(temp)

        #UNWRAP IMAGE, 0 CROP AROUND EDGES
        result = unwrap(image, 0)

        if rotateN:
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
            imageio.imwrite('unwrap.jpg', result)

        else:
            imageio.imwrite('unwrap.jpg', result)

#THIS SHOULD BE YOUR ALLSKY IMAGE, True or False to ROTATE FINAL PANO N
process_img('image.jpg', True)
