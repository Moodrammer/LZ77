# ............................
# Date: 27/4/2020
# author: Mahmoud Amr Mohamed
# ............................
import cv2
import os
import numpy as np
import encode
import decode

imageFilePath = input("Enter the image file path without quotes: ")
file_name, file_ext = os.path.splitext(imageFilePath)

SlidingWindowSize = int(input("Enter the Sliding window size: "))
lookAheadBufferSize = int(input("Enter the lookAheadBuffer size: "))
SearchBufferSize = SlidingWindowSize - lookAheadBufferSize

# Selecting the mode of saving the encoded image either in one or two files according to the sliding window
singlefileMode = 0
if SlidingWindowSize < 256:
    singlefileMode = 1

originalImage = np.array(cv2.imread(imageFilePath, 0), dtype=np.uint8)
numberOfRows = originalImage.shape[0]
numberOfColumns = originalImage.shape[1]

flattenedImage = np.reshape(originalImage, (1, originalImage.size))
print("1. flattened image vector")
print(flattenedImage)

# encoding the image
print("2. encoding ..")
encode.encode(flattenedImage, SearchBufferSize, lookAheadBufferSize, singlefileMode)

# decoding
print("3. decoding ..")
decode.decode(numberOfRows,numberOfColumns, singlefileMode, file_ext)

