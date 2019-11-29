#!/usr/bin/env python3

"""Normalizes multiple depth images to the same scale and saves new ones"""

import pathlib
import sys
import cv2
import numpy as np

filenames = sys.argv[1:]
print(filenames)

highest = 0
for name in filenames:
    im = cv2.imread(name, -1)
    highest = max(highest, im.max())
    print(name, im.min(), im.max())

for name in filenames:
    im = cv2.imread(name, -1)
    im_scaled = ((im * ((2 ** 16 - 1) / highest)) / 255).astype(np.uint8)
    #  im *= 255 / highest
    #  im_scaled = cv2.normalize(im, dst=None, alpha=0, beta=highest, norm_type =
    #          cv2.NORM_MINMAX)

    print(name, im_scaled.min(), im_scaled.max())
    mapped = cv2.applyColorMap(im_scaled, cv2.COLORMAP_HOT)
    #  cv2.imshow("mapped" + name, mapped)
    #  cv2.waitKey(0)

    p = pathlib.Path(name)
    output = p.parent / ("%s_colormapped.png" % p.stem)
    cv2.imwrite(str(output), mapped)

    #  maps = [d for d in dir(cv2) if d.startswith("COLORMAP")]
    #  for m in maps:
    #      mapped = cv2.applyColorMap(im_scaled, getattr(cv2, m))
    #      print(m)
    #      cv2.imshow("mapped" + name, mapped)
    #      cv2.waitKey(0)
