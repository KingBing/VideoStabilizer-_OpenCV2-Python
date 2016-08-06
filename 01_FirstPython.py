import cv2
import sys
import numpy as np

if len(sys.argv)!=2:                 
  print "Usage : python display_image.py <image_file>"
else: 
  img = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_COLOR)
  
(h, w) = img.shape[:2]
emptyImg = cv2.resize(img, (w/2, h/2), interpolation=cv2.INTER_NEAREST)

(rh, rw) = emptyImg.shape[:2] 
center = (rw/2, rh/2)
M = cv2.getRotationMatrix2D(center, 180, 1.0)
emptyImg2 = cv2.warpAffine(emptyImg, M, (rw, rh))

emptyImg3 = cv2.cvtColor(emptyImg, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img)

cv2.imshow("EmptyImg", emptyImg)
cv2.imshow("EmptyImg2", emptyImg2)
cv2.imshow("EmptyImg3", emptyImg3)

#cv2.imwrite("./jpg_q5.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
#cv2.imwrite("./jpg_q10.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

#cv2.imwrite("./png_c0.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
#cv2.imwrite("./phg_c9.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

cv2.waitKey (0)

cv2.destroyAllWindows()
