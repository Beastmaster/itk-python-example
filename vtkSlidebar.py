'''
 Author: QIN Shuo
 Date:   2015/11/10
 This is a example file for vtk
 Function: Create a sphere and control its PhiResolution and ThetaResolution with vtk slide bar

 In C++ way, you can use call back function in 2 ways
 reference: http://www.vtk.org/Wiki/VTK/Tutorials/Callbacks

 When I tried creating a vtkCallbackCommand and reimplement it, python crushed.
 So the other way to add a callback function to interactor is used and work well
'''

import vtk

sphereSource = vtk.vtkSphereSource()
sphereSource.SetCenter(0.0,0.0,0.0)
sphereSource.SetRadius(4.0)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInput(sphereSource.GetOutput())


actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetInterpolationToFlat()

renderer = vtk.vtkRenderer()
renderWin = vtk.vtkRenderWindow()
renderWin.AddRenderer(renderer)

renWinInteractor = vtk.vtkRenderWindowInteractor()
renWinInteractor.SetRenderWindow(renderWin)

renderer.AddActor(actor)
renderWin.Render()

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
slideBar.GetPoint2Coordinate().SetValue(100,40)

sliderWidget = vtk.vtkSliderWidget()
sliderWidget.SetInteractor(renWinInteractor)
sliderWidget.SetRepresentation(slideBar)
sliderWidget.EnabledOn()


# callback function for slide bar
# this class is invalid and will cause crash
class vtkSliderCallback(vtk.vtkCommand):
    def __init__(self):
        pass
    def Execute(self,obj,event):
        slider = obj
        value1 = slider.GetRepresentation().GetValue()
        self.Sphere.SetPhiResolution(value1)
        self.Sphere.SetThetaResolution(value1)

#callback = vtkSliderCallback()
#callback.Sphere = sphereSource

def myCallback(obj,event):
    print "interaction called"
    value = obj.GetRepresentation().GetValue()
    global sphereSource
    sphereSource.SetPhiResolution(value)
    sphereSource.SetThetaResolution(value)

# please pay attention here:  interactionEvent type must be added.
#               and 2 ways to add it are listed below(by name or by vtk command)
#sliderWidget.AddObserver(vtk.vtkCommand.InteractionEvent,myCallback)
sliderWidget.AddObserver("InteractionEvent",myCallback)

renWinInteractor.Initialize()
renderWin.Render()


renWinInteractor.Start()



