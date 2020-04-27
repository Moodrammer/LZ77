# ............................
# Date: 27/4/2020
# author: Mahmoud Amr Mohamed
# ............................

import numpy as np
from numpy import save


def encode(flattenedImage, SearchBufferSize, lookAheadBufferSize, singlefileMode):
    currentCursorPosition = 0
    SearchBufferCurrentIndex = 0
    SearchBufferStartIndex = 0
    LookAheadBufferCurrentIndex = 0
    LookAheadBufferEndIndex = 0
    temporaryMatchingOffset = 0
    temporaryMatchingLength = 0
    # For single file mode
    encodedImage = []
    # For two files mode
    encodedImagecodes = []
    encodedImageoffsets = []

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

                # return the searchBufferCurrentIndex to the begining of the current found match to continue searching
                # from that point for longer matches
                SearchBufferCurrentIndex = (currentCursorPosition - 1) - temporaryMatchingOffset
                LookAheadBufferCurrentIndex = currentCursorPosition

                if temporaryMatchingLength > finalMatchingLength:
                    finalMatchingLength = temporaryMatchingLength
                    finalMatchingOffset = temporaryMatchingOffset

            SearchBufferCurrentIndex -= 1

        # Store the current sliding window triplet (longest match found)
        nextCharacterCodeIndex = currentCursorPosition + finalMatchingLength
        if nextCharacterCodeIndex >= flattenedImage.size:
            nextCharacterCodeIndex = flattenedImage.size - 1
        # if in single file mode store all in one file
        if singlefileMode == 1:
            encodedImage.append([finalMatchingOffset, finalMatchingLength, flattenedImage[0][nextCharacterCodeIndex]])
        # else store in two files
        else:
            encodedImagecodes.append(flattenedImage[0][nextCharacterCodeIndex])
            encodedImageoffsets.append([finalMatchingOffset, finalMatchingLength])
        currentCursorPosition += (finalMatchingLength + 1)


    if singlefileMode == 1:
        encodedImageArray = np.array(encodedImage, dtype=np.uint8)
        save("encoded", encodedImageArray)
    else:
        encodedImagecodesArray = np.array(encodedImagecodes, dtype=np.uint8)
        encodedImageoffsetsArray = np.array(encodedImageoffsets, dtype=np.uint16)
        save("encodedcodes", encodedImagecodesArray)
        save("encodedoffsets", encodedImageoffsetsArray)





