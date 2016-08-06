import cv2
import sys
import numpy as np

if len(sys.argv)!=2:                 
  print "Usage : python display_image.py <image_file>"
else: 
  img = cv2.imread(sys.argv[1], cv2.CV_LOAD_IMAGE_COLOR)

#img = cv2.imread('graf1.png')

(h, w) = img.shape[:2]
clone_img = cv2.resize(img, (w/2, h/2), interpolation=cv2.INTER_NEAREST)

#Filter2D
kernel = np.array([ [0,-1,0],
                    [-1,5,-1],
                    [0,-1,0] ],np.float32)  # kernel should be floating point type.

new_img = cv2.filter2D(clone_img,-1,kernel) # ddepth = -1, means destination image has depth same as input image.

cv2.imshow('Img',clone_img)
cv2.imshow('Filter',new_img)

#Histogram
h = np.zeros((256,256,3)) 
       
bins = np.arange(256).reshape(256,1) 
color = [ (255,0,0),(0,255,0),(0,0,255) ]


for ch, col in enumerate(color):  
    originHist = cv2.calcHist([clone_img],[ch],None,[256],[0,256])  
    cv2.normalize(originHist, originHist,0,255*0.9,cv2.NORM_MINMAX)  
    hist=np.int32(np.around(originHist))  
    pts = np.column_stack((bins,hist))  
    cv2.polylines(h,[pts],False,col)  
       
h=np.flipud(h)  
cv2.imshow('ColorHistogram',h)  


cv2.waitKey(0)
cv2.destroyAllWindows()
