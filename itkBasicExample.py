# Author: QIN Shuo
# Date:   2015/10/26
# This is a test file for itk
# In this file I implement some basic function in itk
# More function will be implemented further
# Function: Read a png file and display with vtk

import itk
import vtk
import sys

# set image file name
image_path = "C:/Users/qinsh/Desktop/test.png"

#####   itk is a templated system and we should define a lot of types first   ####

#define a pixel data type. UC means unsigned char
pixelType = itk.UC
#define image type to unsigned char and 3 dims
imageType = itk.Image[pixelType, 3]
#define reader type, you must include imageType to it
readerType = itk.ImageFileReader[imageType]

# init a reader instance
reader = readerType.New()
# set file name
reader.SetFileName( "C:/Users/qinsh/Desktop/test.png" )
# update and start reading process
reader.Update()
# get itk image
image1 = reader.GetOutput()

#define a itk image to vtk image connector type
#in c++ version i2v connector should define input&output image type
#in python version it seems to be one same image type
I2VConnectorType = itk.ImageToVTKImageFilter[imageType]

#new a I2V connector instance
connector = I2VConnectorType.New()
connector.SetInput(image1)
#pipline based structure need update to start process
connector.Update()


####   below is vtk visulation process  ####
# python version itk and vtk is a little different in consturct a instance
# the main difference is that: itk has a new() function

#visualization pipeline
#actor
actor = vtk.vtkImageActor()
actor.SetInput(connector.GetOutput())
#renderer
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
#render window
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(renderer)
#render window interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)
interactor.Initialize()
interactor.Start()




