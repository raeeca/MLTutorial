rowBlackPixelCount = 0
blackRatio = 0.67 * width
for rowBlackPixels in iter(rowHisto):
    if rowBlackPixels > blackRatio:
        rowBlackPixelCount = rowBlackPixelCount + 1
    else:
        pilimage.crop((0, rowBlackPixelCount, width, height)).save("test_segment_.png")
        pilimage = Im.open("test_segment_.png") #  sys-call
        img = load_image("test_segment_.png")   # function call??
        projectionRows = img.projection_rows()
        rowHisto = list(projectionRows)
        projectionCols = img.projection_cols()
        colHisto = list(projectionCols)
        (width, height) = pilimage.size
        break
print "height is " , height
print "width is " , width
####################
colHistoReverse = reversed(colHisto)
colBlackPixelCount = 0
blackRatio = .98 * height
for colBlackPixels in colHistoReverse:
    if colBlackPixels >  blackRatio:
        colBlackPixelCount = colBlackPixelCount + 1
pilimage.crop((0,0, width - colBlackPixelCount, height)).save("test_segment_.png")
pilimage = Im.open("test_segment_.png") #  sys-call
img = load_image("test_segment_.png")   #  load into memory
projectionRows = img.projection_rows()
rowHisto = list(projectionRows)
projectionCols = img.projection_cols()
colHisto = list(projectionCols)
(width, height) = pilimage.size
print "height is " , height
print "width is " , width
#############################################
rowBlackPixelCount = 0
blackRatio = 0.7 * width
rowHistoReverse = reversed(rowHisto)
for rowBlackPixels in rowHistoReverse:
    if rowBlackPixels >  blackRatio:
        rowBlackPixelCount = rowBlackPixelCount + 1

pilimage.crop((0, 0 , width, height-rowBlackPixelCount)).save("test_segment_.png")
pilimage = Im.open("test_segment_.png") #  sys-call
img = load_image("test_segment_.png")   # load into memory
projectionRows = img.projection_rows()
rowHisto = list(projectionRows)
projectionCols = img.projection_cols()
colHisto = list(projectionCols)
(width, height) = pilimage.size
print "height is " , height
print "width is " , width
#############################################
pilimage.crop((230, 200 ,width-300, height-190)).save("test_segment_.png")
pilimage = Im.open("test_segment_.png") #  sys-call
img = load_image("test_segment_.png")   # load into memory
projectionRows = img.projection_rows()
rowHisto = list(projectionRows)
projectionCols = img.projection_cols()
colHisto = list(projectionCols)
(width, height) = pilimage.size
print "height is " , height
print "width is " , width
