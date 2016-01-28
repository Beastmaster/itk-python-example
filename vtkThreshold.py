'''
 Author: QIN Shuo
 Date:   2016/01/28

 This is a example to threshold a CT image 

 Add plane widget

 Key interact to adjust the threshold

 MarchingCube to visiualize 3D model
'''


import os
import vtk


# load data block
def LoadNifti( name ):
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(name);
    reader.Update()
    return reader.GetOutput()

def CreateSlider():
    #build a slide bar
    slideBar = vtk.vtkSliderRepresentation2D()

    slideBar.SetMinimumValue(3.0)
    slideBar.SetMaximumValue(20.0)
    slideBar.SetTitleText("sphere")

    slideBar.GetSliderProperty().SetColor(1,0,0)
    slideBar.GetTitleProperty().SetColor(1,0,0)
    slideBar.GetLabelProperty().SetColor(1,0,0)
    slideBar.GetSelectedProperty().SetColor(1,0,0)
    slideBar.GetTubeProperty().SetColor(0,1,0)
    slideBar.GetCapProperty().SetColor(1,1,0)

    slideBar.GetPoint1Coordinate().SetCoordinateSystemToDisplay()
    slideBar.GetPoint1Coordinate().SetValue(40,40)
    slideBar.GetPoint2Coordinate().SetCoordinateSystemToDisplay()
    slideBar.GetPoint2Coordinate().SetValue(200,40)

    sliderWidget = vtk.vtkSliderWidget()
    sliderWidget.SetInteractor(renWinInteractor)
    sliderWidget.SetRepresentation(slideBar)
    sliderWidget.EnabledOn()

    def myCallback(obj,event):
        print obj.__class__.__name__," called"
        value = int (obj.GetRepresentation().GetValue())
        




#create visulization component
def DisplayPoly(source):
    polyMapper = vtk.vtkPolyDataMapper()
    polyMapper.SetInputData(source)

    actor = vtk.vtkActor()
    actor.SetMapper(polyMapper)

    renderer = vtk.vtkRenderer()
    win = vtk.vtkRenderWindow()
    intact = vtk.vtkRenderWindowInteractor()
    style = vtk.vtkInteractorStyleImage()

    win.AddRenderer(renderer)
    renderer.AddActor(actor)
    intact.SetInteractorStyle(style)
    intact.SetRenderWindow(win)
    win.Render()
    intact.Start()


def DisplayComponent(source):
    win = vtk.vtkRenderWindow()
    intact = vtk.vtkRenderWindowInteractor()
    intact.SetRenderWindow(win)
    planeX = vtk.vtkImagePlaneWidget()
    planeY = vtk.vtkImagePlaneWidget()
    planeZ = vtk.vtkImagePlaneWidget()

    planeX.SetInteractor(intact)
    planeY.SetInteractor(intact)
    planeZ.SetInteractor(intact)

    planeX.SetInputData(source)
    planeY.SetInputData(source)
    planeZ.SetInputData(source)

    planeX.SetPlaneOrientationToXAxes()
	planeY.SetPlaneOrientationToXAxes()
	planeZ.SetPlaneOrientationToXAxes()

    planeX.On()
    planeY.On()
    planeZ.On()


# start main function

name = "E:/test/spine.nii"

if os.path.isfile(name):
    img = LoadNifti(name)
else:
    print name, "is not a file"

    

# convert vtkImageData to vtkPolyData
geometryFilter = vtk.vtkImageDataGeometryFilter()
geometryFilter.SetInputData(img)
#geometryFilter.Update()

DisplayComponent(img)
intact.Start()



