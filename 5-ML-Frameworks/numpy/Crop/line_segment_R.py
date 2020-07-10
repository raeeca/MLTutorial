
## Inputs: python [script path] [image path]
## Outputs: PNG images of each line in a document. All within 1 directory



##########IMPORTS###############
import sys
from PIL import Image as Im
import numpy as np
from gamera.core import *
from pil_io import *
init_gamera()
from collections import deque
################################

##########LOAD IMAGE############
## opens and loads the image file

pilimage = Im.open(sys.argv[1]) #  sys-call
img = load_image(sys.argv[1])   # function call??
################################

###########################################

(width, height) = pilimage.size # height and width of the image on pixels

projectionRows = img.projection_rows()  # Compute the horizontal projections of an image.  This computes the number of pixels in each row.  #returns an integer vector(intVector)
# (gives bunch of integers, each represents number of pixels in a row)
rowHisto = list(projectionRows) # creates a "list" data structure from the integers that keep count of row pixels (saved in rowHisto)

############################################

#############################################
# this bitch calculates
#[Window size] we compare [window size] to black pixels of projection_rows() and try to give a number that is small enough because we are searching for a row with minimum number of black pixels.
#[min distance] the minimum distance between two lines with minimum number of black pixels should not be less than minimum distance
#############################################


print rowHisto