# LZ77 Image Compression
---
This is an eductional implementation of the LZ77 algorithm on 
grey scale images

---
## prerequisites:
`python 3.7.7`
`numpy 1.18.3`
`opencv-python 4.2.0.34`
## Steps to run: 
1. run the main.py file while the encode.py & decode.py are in the same directory
2. Enter the path for the image to be decoded without quotes
3. Enter the `sliding window size` & the `lookaheadBuffer size`
4. The image is encoded and a numpy file is generated in the same directory
according to the slidingwindow size
  * If the `Slidingwindow size` is smaller than `256` the encoded image will be
  produced in one file called `encoded.npy` with type `uint8`
  * else the  encoded image will be split into two files `encodedcodes.npy` for
  the codes with type `uint8` & `encodedoffsets.npy` for the offset and length with
  type `uint16`
5. The image is decoded and an imagefile called `DecodedImage` is generated in 
the project directory

Some test images are provided in `images` folder   
