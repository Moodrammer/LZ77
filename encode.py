# ............................
# Date: 22/4/2020
# author: Mahmoud Amr Mohamed
# ............................

import numpy as np
from numpy import save
import cv2

imageFilePath = "./images/blox.jpg"
SlidingWindowSize = 512
lookAheadBufferSize = 256
SearchBufferSize = SlidingWindowSize - lookAheadBufferSize

originalImage = np.array(cv2.imread(imageFilePath, 0), dtype=np.uint8)
numberOfRows = originalImage.shape[0]
numberOfColumns = originalImage.shape[1]

flattenedImage = np.reshape(originalImage, (1, originalImage.size))
print(flattenedImage)

encodedImage = []


def encode():
    currentCursorPosition = 0
    SearchBufferCurrentIndex = 0
    SearchBufferStartIndex = 0
    LookAheadBufferCurrentIndex = 0
    LookAheadBufferEndIndex = 0
    temporaryMatchingOffset = 0
    temporaryMatchingLength = 0

    while currentCursorPosition < flattenedImage.size:
        # adjust the sliding window around the current cursor position
        SearchBufferCurrentIndex = currentCursorPosition - 1
        SearchBufferStartIndex = currentCursorPosition - SearchBufferSize
        LookAheadBufferCurrentIndex = currentCursorPosition
        LookAheadBufferEndIndex = currentCursorPosition + (lookAheadBufferSize - 1)
        if LookAheadBufferEndIndex >= flattenedImage.size:
            LookAheadBufferEndIndex = flattenedImage.size - 1
        finalMatchingOffset = 0
        finalMatchingLength = 0

        while SearchBufferCurrentIndex != -1 and SearchBufferCurrentIndex >= SearchBufferStartIndex:
            if flattenedImage[0][LookAheadBufferCurrentIndex] == flattenedImage[0][SearchBufferCurrentIndex]:
                temporaryMatchingOffset = (currentCursorPosition - 1) - SearchBufferCurrentIndex
                temporaryMatchingLength = 1
                SearchBufferCurrentIndex += 1
                LookAheadBufferCurrentIndex += 1
                # corner case : if we reached the last element
                if LookAheadBufferCurrentIndex >= flattenedImage.size:
                    break
                # Find the matching length
                while flattenedImage[0][LookAheadBufferCurrentIndex] == flattenedImage[0][SearchBufferCurrentIndex]:
                    temporaryMatchingLength += 1
                    # print(temporaryMatchingLength)
                    if LookAheadBufferCurrentIndex < LookAheadBufferEndIndex:
                        LookAheadBufferCurrentIndex += 1
                        SearchBufferCurrentIndex += 1
                    else:
                        break

                SearchBufferCurrentIndex = (currentCursorPosition - 1) - temporaryMatchingOffset
                LookAheadBufferCurrentIndex = currentCursorPosition

                if temporaryMatchingLength > finalMatchingLength:
                    finalMatchingLength = temporaryMatchingLength
                    finalMatchingOffset = temporaryMatchingOffset

            SearchBufferCurrentIndex -= 1

        # Store the current sliding window triplet
        nextCharacterCodeIndex = currentCursorPosition + finalMatchingLength
        if nextCharacterCodeIndex >= flattenedImage.size:
            nextCharacterCodeIndex = flattenedImage.size - 1
        encodedImage.append([finalMatchingOffset, finalMatchingLength, flattenedImage[0][nextCharacterCodeIndex]])
        currentCursorPosition += (finalMatchingLength + 1)


encode()

encodedImageArray = np.array(encodedImage, dtype=np.uint16)
# print(encodedImageArray.shape)
# for i in range(encodedImageArray.shape[0]):
#     print(encodedImageArray[i])

save("encoded", encodedImageArray)



