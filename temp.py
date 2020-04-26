# ............................
# Date: 22/4/2020
# author: Mahmoud Amr Mohamed
# ............................

import numpy as np
import cv2
from numpy import save

a = []
a.append([1,2,3])
a.append([4,5,6])
a.append([7,8,9])
print(a);

test = np.array(a, dtype=np.uint8)
print(test.shape)
print(test.ndim)
print(test.itemsize)
print(test)

# test2 = np.array([1, 2, 3, 4, 5, 6, 7, 256, 9], dtype=np.uint8)

test2 = np.zeros((1, ), dtype=np.uint8)
print(test2)
np.save("test", test)
np.save("test2", test2)


loadingTest = np.load("test.npy")
print(loadingTest)
print(loadingTest[0][2])