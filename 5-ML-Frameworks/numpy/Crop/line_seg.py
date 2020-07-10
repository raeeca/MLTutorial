## Inputs: python [script path] [image path]
## Outputs: PNG images of each line in a document. All within 1 directory

##############################   IMPORTS  ####################
import sys
from PIL import Image as  Im
import numpy as np
from gamera.core import *
from pil_io import *

init_gamera()
from collections import deque
##############################################################

######################      LOAD IMAGE    ######################
##                          opens and loads the image file

pilimage = Im.open(sys.argv[1]) #  sys-call
img = load_image(sys.argv[1])   # function call??
################################################################

##################################################################################
(width, height) = pilimage.size # height and width of the image on pixels
\cf7 \cb8 print\cf0 \cb1  \cf6 "height is "\cf0  , height\
\cf7 \cb8 print\cf0 \cb1  \cf6 "width is "\cf0  , width\
projectionRows = img.projection_rows()  \cf2 # Compute the horizontal projections of an image.  This computes the number of pixels in each row.  #returns an integer vector(intVector)\cf0 \
\cf2 # (gives bunch of integers, each represents number of pixels in a row)\cf0 \
projectionCols = img.projection_cols()\
rowHisto = \cf5 list\cf0 (projectionRows) \cf2 # creates a "list" data structure from the integers that keep count of row pixels (saved in rowHisto)\cf0 \
colHisto = \cf5 list\cf0 (projectionCols)\
##################################################################################
\
\cf0 rowBlackPixelCount = \cf6 0\cf0 \
blackRatio = \cf6 0.67\cf0  * width\
\cf4 for\cf0  rowBlackPixels \cf4 in\cf0  \cf5 iter\cf0 (rowHisto):\
    \cf4 if\cf0  rowBlackPixels > blackRatio:\
        rowBlackPixelCount = rowBlackPixelCount + \cf6 1\cf0 \
    \cf4 else\cf0 :\
        pilimage.crop((\cf6 0\cf0 , rowBlackPixelCount, width, height)).save(\cf6 "test_segment_.png"\cf0 )\
        pilimage = Im.\cf5 open\cf0 (\cf6 "test_segment_.png"\cf0 ) \cf2 #  sys-call\cf0 \
        img = load_image(\cf6 "test_segment_.png"\cf0 )   \cf2 # function call??\cf0 \
        projectionRows = img.projection_rows()\
        rowHisto = \cf5 list\cf0 (projectionRows)\
        projectionCols = img.projection_cols()\
        colHisto = \cf5 list\cf0 (projectionCols)\
        (width, height) = pilimage.size\
        \cf4 break\cf0 \
\cf7 \cb8 print\cf0 \cb1  \cf6 "height is "\cf0  , height\
\cf7 \cb8 print\cf0 \cb1  \cf6 "width is "\cf0  , width\
\cf2 #############################################\cf0 \
colHistoReverse = \cf5 reversed\cf0 (colHisto)\
colBlackPixelCount = \cf6 0\cf0 \
blackRatio = \cf6 .98\cf0  * height\
\cf4 for\cf0  colBlackPixels \cf4 in\cf0  colHistoReverse:\
    \cf4 if\cf0  colBlackPixels >  blackRatio:\
        colBlackPixelCount = colBlackPixelCount + \cf6 1\cf0 \
pilimage.crop((\cf6 0\cf0 ,\cf6 0\cf0 , width - colBlackPixelCount, height)).save(\cf6 "test_segment_.png"\cf0 )\
pilimage = Im.\cf5 open\cf0 (\cf6 "test_segment_.png"\cf0 ) \cf2 #  sys-call\cf0 \
img = load_image(\cf6 "test_segment_.png"\cf0 )   \cf2 #  load into memory\cf0 \
projectionRows = img.projection_rows()\
rowHisto = \cf5 list\cf0 (projectionRows)\
projectionCols = img.projection_cols()\
colHisto = \cf5 list\cf0 (projectionCols)\
(width, height) = pilimage.size\
\cf7 \cb8 print\cf0 \cb1  \cf6 "height is "\cf0  , height\
\cf7 \cb8 print\cf0 \cb1  \cf6 "width is "\cf0  , width\
\cf2 #############################################\cf0 \
 \cf2 #############################################\cf0 \
rowBlackPixelCount = \cf6 0\cf0 \
blackRatio = \cf6 0.7\cf0  * width\
rowHistoReverse = \cf5 reversed\cf0 (rowHisto)\
\cf4 for\cf0  rowBlackPixels \cf4 in\cf0  rowHistoReverse:\
    \cf4 if\cf0  rowBlackPixels >  blackRatio:\
        rowBlackPixelCount = rowBlackPixelCount + \cf6 1\cf0 \
\
pilimage.crop((\cf6 0\cf0 , \cf6 0\cf0  , width, height-rowBlackPixelCount)).save(\cf6 "test_segment_.png"\cf0 )\
pilimage = Im.\cf5 open\cf0 (\cf6 "test_segment_.png"\cf0 ) \cf2 #  sys-call\cf0 \
img = load_image(\cf6 "test_segment_.png"\cf0 )   \cf2 # load into memory\cf0 \
projectionRows = img.projection_rows()\
rowHisto = \cf5 list\cf0 (projectionRows)\
projectionCols = img.projection_cols()\
colHisto = \cf5 list\cf0 (projectionCols)\
(width, height) = pilimage.size\
\cf7 \cb8 print\cf0 \cb1  \cf6 "height is "\cf0  , height\
\cf7 \cb8 print\cf0 \cb1  \cf6 "width is "\cf0  , width\
\cf2 #############################################\cf0 \
pilimage.crop((\cf6 230\cf0 , \cf6 200\cf0  ,width-\cf6 50\cf0 , height-\cf6 200\cf0 )).save(\cf6 "test_segment_.png"\cf0 )\
pilimage = Im.\cf5 open\cf0 (\cf6 "test_segment_.png"\cf0 ) \cf2 #  sys-call\cf0 \
img = load_image(\cf6 "test_segment_.png"\cf0 )   \cf2 # load into memory\cf0 \
projectionRows = img.projection_rows()\
rowHisto = \cf5 list\cf0 (projectionRows)\
projectionCols = img.projection_cols()\
colHisto = \cf5 list\cf0 (projectionCols)\
(width, height) = pilimage.size\
\cf7 \cb8 print\cf0 \cb1  \cf6 "height is "\cf0  , height\
\cf7 \cb8 print\cf0 \cb1  \cf6 "width is "\cf0  , width\
\cf2 #############################################\cf0 \
\cf2 #[Window size] we compare [window size] to black pixels of projection_rows() and try to give a number that is small enough because we are searching for a row with minimum number of black pixels.\cf0 \
\cf2 #[min distance] the minimum distance between two lines with minimum number of black pixels should not be less than minimum distance\cf0 \
\cf2 #############################################\
\
\cf7 \cb8 print\cf0 \cb1  pilimage.getpixel((\cf6 0\cf0 ,\cf6 0\cf0 ))\
index_list = \cf5 list\cf0 ()\
minimum_pixel_list = \cf5 list\cf0 ()\
flag = \cf6 0\cf0 \
rowHistoIndex = \cf6 0\cf0 \
\cf4 for\cf0  integer \cf4 in\cf0  rowHisto:\
    \cf4 if\cf0  integer < \cf6 100\cf0  \cf4 and\cf0  rowHisto[rowHistoIndex - \cf6 1\cf0 ] > \cf6 100\cf0 :\
        minimum_pixel_list.append(integer)\
        index_list.append(rowHistoIndex)\
    \cf4 elif\cf0  integer < \cf6 100\cf0 :\
        \cf4 if\cf0  integer < minimum_pixel_list[-\cf6 1\cf0 ]:\
           minimum_pixel_list[-\cf6 1\cf0 ] = integer\
           index_list[-\cf6 1\cf0 ] = rowHistoIndex\
    rowHistoIndex = rowHistoIndex + \cf6 1\cf0 \
\
\cf2 # minima_list(x,y,z,w)\cf0 \
\cf2 # x : index of the white-line in rowHisto\cf0 \
\cf2 # y : quantity of the black pixels in the white-line\cf0 \
\cf2 # z : distance of the white line from the black-line above\cf0 \
\cf2 # w : distance of the white line from the black line below\cf0 \
minima_list = \cf5 zip\cf0 (index_list, minimum_pixel_list)\
\
index = \cf6 0\cf0 \
\cf2 #for element in minima_list:\cf0 \
 \cf2 #   if index == 0:\cf0 \
  \cf2 #      nextElement = minima_list[index+1]\cf0 \
   \cf2 #    pilimage.crop((0, element[0], width, nextElement[0])).save("test_segment_" + str(index) + ".png")\cf0 \
    \cf2 #elif index != len(minima_list) - 1:\cf0 \
     \cf2 #   nextElement = minima_list[index+1]\cf0 \
      \cf2 #  pilimage.crop((0, element[0], width, nextElement[0])).save("test_segment_" + str(index) + ".png")\cf0 \
   \cf2 # else:\cf0 \
\cf2 #       pilimage.crop((0, element[0], width, height)).save("test_segment_" + str(index) + ".png")\cf0 \
 \cf2 #   index = index + 1\cf0 \
}
