# ............................
# Date: 27/4/2020
# author: Mahmoud Amr Mohamed
# ............................

from numpy import load
import cv2
import numpy as np


def decode(numberOfRows, numberOfColumns, singlefileMode, file_ext):
    if singlefileMode == 1:
        encodedFlattenedImage = load("encoded.npy")
        numberOfTriplets = encodedFlattenedImage.shape[0]
    else:
        encodedcodes = load("encodedcodes.npy")
        encodedoffsets = load("encodedoffsets.npy")
        numberOfTriplets = encodedoffsets.shape[0]

    decodedflattenedImage = []
    currentCursorPosition = 0
    currentCode = 0


    for tripletIndex in range(numberOfTriplets):
        if singlefileMode == 1:
            offset = encodedFlattenedImage[tripletIndex][0]
            matchingLength = encodedFlattenedImage[tripletIndex][1]
            code = encodedFlattenedImage[tripletIndex][2]
        else:
            offset = encodedoffsets[tripletIndex][0]
            matchingLength = encodedoffsets[tripletIndex][1]
            code = encodedcodes[tripletIndex]

        while offset != 0:
            currentCursorPosition -= 1
            offset -= 1

        while matchingLength != 0:
            currentCode = decodedflattenedImage[currentCursorPosition]
            decodedflattenedImage.append(currentCode)
            currentCursorPosition += 1
            matchingLength -= 1

        decodedflattenedImage.append(code)
        # return the cursor to the end of the list
        currentCursorPosition = len(decodedflattenedImage) - 1
        # print(currentCursorPosition)

    decodedflattenedImage = np.array(decodedflattenedImage)
    # In encoding we add an extra character if the final lookahead buffer matches completely
    # to handle the case when we match till the last element in the flattened image and there is no extra code after the
    # matching string to add
    originalImageSize = numberOfRows * numberOfColumns
    if decodedflattenedImage.size > originalImageSize:
        # discard the last element
        decodedflattenedImage = decodedflattenedImage[0: originalImageSize]
    decodedImage = decodedflattenedImage.reshape((numberOfRows, numberOfColumns))

    cv2.imwrite("DecodedImage" + file_ext, decodedImage)

