import numpy as np
from gamera.core import *
from pil_io import *
init_gamera()
################################


##########LOAD IMAGE############
## load image and create copy
pilimage = Im.open(sys.argv[1])
print sys.argv[1]
img = from_pil(pilimage).image_copy()
################################


##########IMAGE PREPROCESSING##############
# Run thresholding on the page to binarize the file
bin_image = img.djvu_threshold(0.2, 512, 64, 2)
# ############################################


##########SAVE OFF IMAGE#####################
bin_image.save_image(sys.argv[2])
"binary_trans.py" [readonly][noeol] 28L, 652C 