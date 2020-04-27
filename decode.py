from encode import numberOfRows,numberOfColumns
from numpy import load
import cv2
import numpy as np

encodedFlattenedImage = load("encoded.npy")

decodedflattenedImage = []
currentCursorPosition = 0
currentCode = 0

for tripletIndex in range(encodedFlattenedImage.shape[0]):
    offset = encodedFlattenedImage[tripletIndex][0]
    matchingLength = encodedFlattenedImage[tripletIndex][1]
    code = encodedFlattenedImage[tripletIndex][2]

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
print(decodedflattenedImage)
# In encoding we add an extra character if the final lookahead buffer matches completely
originalImageSize = numberOfRows * numberOfColumns
if decodedflattenedImage.size > originalImageSize:
    # discard the last element
    decodedflattenedImage = decodedflattenedImage[0: originalImageSize]
print(decodedflattenedImage)
decodedImage = decodedflattenedImage.reshape((numberOfRows, numberOfColumns))
print(decodedImage)

cv2.imwrite("DecodedImage.jpg", decodedImage)

cv2.imshow("decoded", decodedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

