import numpy as np
import cv2

imageFilePath = "./blox.jpg"
SlidingWindowSize = 0
searchBufferSize = 0

originalImage = np.array(cv2.imread(imageFilePath, 0), dtype=np.uint8)

flattenedImage = np.reshape(originalImage, (1, originalImage.size))

for index in range(flattenedImage.size):
    print(flattenedImage[0][index])

