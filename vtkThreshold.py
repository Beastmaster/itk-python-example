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

def CreateSlider(renWinInteractor,plane,y):
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
    slideBar.GetPoint1Coordinate().SetValue(40 ,40+y)
    slideBar.GetPoint2Coordinate().SetCoordinateSystemToDisplay()
    slideBar.GetPoint2Coordinate().SetValue(200,40+y)

    sliderWidget = vtk.vtkSliderWidget()
    sliderWidget.SetInteractor(renWinInteractor)
    sliderWidget.SetRepresentation(slideBar)
    sliderWidget.EnabledOn()

    def myCallback(obj,event):
        print obj.__class__.__name__," called"
        value = int (obj.GetRepresentation().GetValue())
        plane.SetSliceIndex(value)

    sliderWidget.AddObserver("InteractionEvent",myCallback)

win = vtk.vtkRenderWindow()

#create visulization component
def DisplayPoly(source,callback):
    global win
    
    polyMapper = vtk.vtkPolyDataMapper()
    polyMapper.SetInputData(source)

    actor = vtk.vtkActor()
    actor.SetMapper(polyMapper)

    renderer = vtk.vtkRenderer()
    intact = vtk.vtkRenderWindowInteractor()
    style = vtk.vtkInteractorStyleTrackballCamera()

    intact.AddObserver(vtk.vtkCommand.KeyPressEvent,callback)

    win.AddRenderer(renderer)
    renderer.AddActor(actor)
    intact.SetInteractorStyle(style)
    intact.SetRenderWindow(win)
    win.Render()
    intact.Start()


def DisplayComponent(source):
    renderer = vtk.vtkRenderer()
    win = vtk.vtkRenderWindow()
    win.AddRenderer(renderer)
    style = vtk.vtkInteractorStyleImage()
    intact = vtk.vtkRenderWindowInteractor()
    intact.SetInteractorStyle(style)
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
    planeY.SetPlaneOrientationToYAxes()
    planeZ.SetPlaneOrientationToZAxes()

    planeX.On()
    planeY.On()
    planeZ.On()

    def myCallback(obj,event):
        print obj.__class__.__name__," called"
        key = obj.GetKeySym() 
        if key=="Up":
            planeX.SetSliceIndex(50)
        else:
            pass
    intact.AddObserver(vtk.vtkCommand.KeyPressEvent,myCallback)

    intact.Start()


# start main function

name = "E:/test/spine.nii"

if os.path.isfile(name):
    img = LoadNifti(name)
else:
    print name, "is not a file"



#threshold imagedata

#threshold = vtk.vtkImageThreshold()
#threshold.SetInputData(img)
#lower = 500
#upper = 1000
#threshold.ThresholdBetween(lower,upper)
#threshold.ReplaceOutOn()
#threshold.SetOutValue(0)
#threshold.Update()

march = vtk.vtkMarchingCubes()
march.SetInputData(img)
march.GenerateValues(1,1200,1500)
march.Update()

value_u = 1500
value_l = 1200
def callback(obj,event):
    global value_l
    global value_u
    global win
    key = obj.GetKeySym() 
    if key == "Up":
        value_l = value_l+50
        march.GenerateValues(1,value_l,value_u)
        march.Update()
        print (value_l)
    elif key == "Down":
        value_u = value_u-50
        march.GenerateValues(1,value_l,value_u)
        march.Update()
        print (value_u)
    else:
        pass
    win.Render()

print "threshold"

img_dis = march.GetOutput()

# convert vtkImageData to vtkPolyData
geometryFilter = vtk.vtkImageDataGeometryFilter()
#geometryFilter.SetInputData(img_dis)
#geometryFilter.Update()

print "converted"

DisplayPoly(img_dis,callback)





