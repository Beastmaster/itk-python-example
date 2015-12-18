
'''
Author:  QIN Shuo
Date:  2015/11/5
Description: 
     This example demonstrate how to use regionalmaximaimagefilter in itk-python

'''

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







