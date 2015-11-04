#Author: Qin Shuo
#Date:   2015/10/29
#Description:
#  This example how to detect edge with
#  Canny Edge Detection Filter
#Reference:
#  http://itk.org/ITKExamples/src/Filtering/ImageFeature/DetectEdgesWithCannyFilter/Documentation.html
#



import sys
import itk
import QuickView

#define image type
pixelType = itk.F
dimension = 2
imageType = itk.Image[pixelType,dimension]
readerType = itk.ImageFileReader[imageType]

name = "C:/Users/qinsh/Desktop/test.dcm"
variance = 1.5
lowerThreshold = 20
upperThreshold = 40



reader = readerType.New()
reader.SetFileName(name)


sobelType = itk.SobelEdgeDetectionImageFilter[imageType,imageType]
sobelFilter = sobelType.New()
sobelFilter.SetInput(reader.GetOutput())


filterType = itk.CannyEdgeDetectionImageFilter[imageType,imageType]
cannyFilter = filterType.New()
cannyFilter.SetInput(reader.GetOutput())
cannyFilter.SetVariance(variance)
cannyFilter.SetLowerThreshold(lowerThreshold)
cannyFilter.SetUpperThreshold(upperThreshold)


# visualize
viewer = QuickView.QuickView(imageType)
viewer.AddImage(cannyFilter.GetOutput())
viewer.Visualize2()


