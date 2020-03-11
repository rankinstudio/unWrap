import cv2
import numpy as np

def unwrap(imgIn, Cb):

    img = imgIn

    #MAPPING
    def buildMap(Wd, Hd, R2, Cx, Cy):
        map_x = np.zeros((Hd, Wd), np.float32)
        map_y = np.zeros((Hd, Wd), np.float32)
        for y in range(0, int(Hd - 1)):
            for x in range(0, int(Wd - 1)):
                r = (float(y) / float(Hd)) * R2
                theta = (float(x) / float(Wd)) * 2.0 * np.pi
                xS = Cx + r * np.sin(theta)
                yS = Cy + r * np.cos(theta)
                map_x.itemset((y, x), int(xS))
                map_y.itemset((y, x), int(yS))

        return map_x, map_y

    #UNWARP
    def unwarp(img, xmap, ymap):
        output = cv2.remap(img, xmap, ymap, cv2.INTER_LINEAR)
        return output

    #IMAGE CENTER
    Cx = img.shape[0]/2
    Cy = img.shape[1]/2

    #RADIUS OUTER
    Rx = Cb
    R = Rx - Cx

    #DESTINATION IMAGE SIZE
    Wd = int(abs(2.0 * (R / 2) * np.pi))
    Hd = int(abs(R))

    #BUILD MAP
    xmap, ymap = buildMap(Wd, Hd, R, Cx, Cy)

    #UNWARP
    result = unwarp(img, xmap, ymap)

    return result

