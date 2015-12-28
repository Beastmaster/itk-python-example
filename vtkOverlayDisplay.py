
'''
Author: QIN Shuo
Date: 2015/12/18
Description:


Function:
    Overlay display of 2 images using 2 layered renderers

'''



import vtk





dir1 = '/home/qinshuo/Data/Data1'
dir2 = '/home/qinshuo/Data/Data2'


reader1 = vtk.vtkDICOMImageReader()
reader1.SetDirectoryName(dir1)
reader1.Update()
img1 = reader1.GetOutput()

reader2 = vtk.vtkDICOMImageReader()
reader2.SetDirectoryName(dir2)
reader2.Update()
img2 = reader2.GetOutput()

# reslice direction
dir_X = [0,0,0]
dir_Y = [0,0,0]
dir_Z = [0,0,0]

# reslice center
extent1 = img1.GetExtent()
print extent1
extent2 = img2.GetExtent()
print extent2
center_X = extent1[1] if extent2[1]>extent1[1] else extent2[1]
center_X = center_X/2
center_Y = extent1[3] if extent2[3]>extent1[3] else extent2[3]
center_Y = center_Y/2
center_Z = extent1[5] if extent2[5]>extent1[5] else extent2[5]
center_Z = center_Z/2

# reslicer instance
slicer1 = vtk.vtkImageReslice()
slicer1.SetInputData(img1)
slicer1.SetOutputDimensionality(2)
slicer1.SetResliceAxesOrigin(center_X,center_Y,center_Z)
slicer1.SetResliceAxesDirectionCosines(dir_X,dir_Y,dir_Z)


slicer2 = vtk.vtkImageReslice()
slicer2.SetInputData(img2)
slicer2.SetOutputDimensionality(2)
slicer2.SetResliceAxesOrigin(center_X,center_Y,center_Z)
slicer2.SetResliceAxesDirectionCosines(dir_X,dir_Y,dir_Z)

# lookup table
'''
table = vtk.vtkWindowLevelLookupTable()
range_l = img1.GetOutput().GetScalarRange[0]
range_h = img1.GetOutput().GetScalarRange[1]
print range_h
print range_l
'''
colorSeries = vtk.vtkColorSeries()
colorSeriesEnum = colorSeries.BREWER_QUALITATIVE_SET3
colorSeries.SetColorScheme(colorSeriesEnum)
lut = vtk.vtkLookupTable()
colorSeries.BuildLookupTable(lut)
lut.SetNanColor(1,0,0,1)
#
lut = vtk.vtkWindowLevelLookupTable()
lut.SetWindow(1000)
lut.SetLevel(500)


mapper1 = vtk.vtkDataSetMapper()
mapper1.SetInputData(slicer1.GetOutput())
mapper1.SetLookupTable(lut)

mapper2 = vtk.vtkDataSetMapper()
mapper2.SetInputData(slicer2.GetOutput())
mapper2.SetLookupTable(lut)

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)


renderer = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
interactor = vtk.vtkRenderWindowInteractor()

style = vtk.vtkInteractorStyleImage()
style.SetInteractionModeToImageSlicing()
interactor.SetInteractorStyle(style)

renderer.AddActor(actor1)
renderer.AddActor(actor2)

renWin.AddRenderer(renderer)
interactor.SetRenderWindow(renWin)

def MouseWheelForwardCallback(obj,event):
    global slicer1
    global slicer2
    global renWin
    global center_Z,center_Y,center_X

    center_Z = center_Z+1

    slicer1.SetResliceAxesOrigin(center_X,center_Y,center_Z)
    slicer2.SetResliceAxesOrigin(center_X,center_Y,center_Z)
    slicer1.Update()
    slicer2.Update()
    renWin.Render()

def MouseWheelBackwardCallback(obj,event):
    global slicer1
    global slicer2
    global renWin
    global center_Z,center_Y,center_X
    center_Z = center_Z-1
    slicer1.SetResliceAxesOrigin(center_X,center_Y,center_Z)
    slicer2.SetResliceAxesOrigin(center_X,center_Y,center_Z)
    slicer1.Update()
    slicer2.Update()
    renWin.Render()


#interactor.AddObserver('MouseWheelForwardEvent',MouseWheelForwardCallback)
#interactor.AddObserver('MouseWheelBackwardEvent',MouseWheelBackwardCallback)
renWin.Render()
interactor.Start()


