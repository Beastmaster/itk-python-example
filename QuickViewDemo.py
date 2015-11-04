# Author: QIN Shuo
# Date:   2015/10/26
# This is a test file for itk
# This example demonstrates simple visualization capabilities provided by the QuickView class. 
# Reference: http://farsight-toolkit.org/wiki/FARSIGHT_Tutorials/Quick_Start

import itk
import QuickView

#definition for creation function
def CreateImage(image):
    ImageType = itk.Image[itk.UC,2]
    corner = [0,0]
    NumRows = 200
    NumCols = 300
    size = [NumRows,NumCols]

    region = itk.ImageRegion._2(corner,size)

    image.SetRegions(region)
    image.Allocate()

    # make a square
    for r in range(40,100):
        for c in range(40,100):
            pixelIndex = [r,c]
            image.SetPixel(pixelIndex,15)

    return image



###  start main function here  ###
# type defines for Image Type
ImageType = itk.Image[itk.UC,2]
# construct a image pointer
image = ImageType.New()
# invoke function defined previously
CreateImage(image)
# type defines for RescalIntensityImageFilter
RescalFilterType = itk.RescaleIntensityImageFilter[ImageType,ImageType]
rescaleFilter = RescalFilterType.New()
rescaleFilter.SetInput(image)
rescaleFilter.SetOutputMinimum(0)
rescaleFilter.SetOutputMaximum(255)
rescaleFilter.Update()

#image = rescaleFilter.GetOutput()

view = QuickView.QuickView(ImageType)
view.AddImage(rescaleFilter.GetOutput())
view.Visualize2()


