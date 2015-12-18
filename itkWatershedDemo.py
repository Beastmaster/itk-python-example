#Author: Qin Shuo
#Date:   2015/11/2
#Description:
#  This example how to detect edge with
#  Canny Edge Detection Filter
#Reference:
#
#Fail to display:
#     unsupported type of itk data: unsigned long (watershed filters required)


import itk  #algorithm
import vtk  # for display
import QuickView

# typedef for pixel or image 
PixelType = itk.UC
ImageType = itk.Image[itk.UC,2]
ReaderType = itk.ImageFileReader[ImageType]

# read or create a image
reader = ReaderType.New()
fileName = 'C:/Users/qinsh/Desktop/test.dcm'
reader.SetFileName(fileName)
reader.Update()

# simple version from itk example
gradientMagnitudeImageFilter = itk.GradientMagnitudeImageFilter[ImageType,ImageType].New()
gradientMagnitudeImageFilter.SetInput(reader.GetOutput())
gradientMagnitudeImageFilter.Update()

threshold = 0.005
level = 0.5

watershedFilterType = itk.WatershedImageFilter[ImageType]
watershed = watershedFilterType.New()
watershed.SetInput(gradientMagnitudeImageFilter.GetOutput())
watershed.SetThreshold(threshold)
watershed.SetLevel(level)
watershed.Update()


image = watershed.GetOutput()

# threshold first and convert to binary image



# open to remove noise


# dilate to get background area


# distance transform to get foreground



# maker labelling



# run watershed algorithm




# display
viewer = QuickView.QuickView(itk.UL)
viewer.AddImage(image)
viewer.Visualize2()

i2vConnector = itk.ImageToVTKImageFilter[ImageType]
connector = i2vConnector.New()
connector.SetInput(image)

viewer2 = vtk.vtkImageViewer2()
viewer2.SetInput(connector.GetOutput())

interactor = vtk.vtkRenderWindowInteractor()
viewer2.SetupInteractor(interactor)
viewer2.Render()
viewer2.GetRenderer().ResetCamera()
viewer2.Render()

interactor.Start()
