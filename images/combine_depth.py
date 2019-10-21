#!/usr/bin/env python3

import cv2
import numpy as np

ref = cv2.imread("rs_back_example_2019-10-16-00-33-41_ref.png", -1)
render = cv2.imread("rs_back_example_2019-10-16-00-33-41_render.png", -1)

combined = np.zeros(ref.shape, dtype=ref.dtype)
rows, cols = ref.shape

for i in range(rows):
    for j in range(cols):
        rs = ref[i, j]
        lidar = render[i, j]
        combined[i, j] = lidar if (rs > 2500 or rs == 0) else rs

cv2.imshow("combined", combined)
cv2.imwrite("combined_depth.png", combined)
cv2.waitKey(0)
