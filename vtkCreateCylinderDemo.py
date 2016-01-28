#python for vtk test
#Created by QinShuo
#Date    2015.8.18
# This Demo demonstrate how to create a cylinder and display

'test module'
__author__ = 'Qin Shuo'


import vtk
from vtk.util.colors import tomato


#create a polygonal cylinder model
cylinder = vtk.vtkCylinderSource()
cylinder.SetResolution(8)
cylinder.Update()


#create mapper
#function: pushing the geometry into the graphics library
#others:   color mapping
cylinderMapper = vtk.vtkPolyDataMapper()
cylinderMapper.SetInputData(cylinder.GetOutput())

#add an actor
#set transformation matrix / texture map
cylinderActor = vtk.vtkActor()
cylinderActor.SetMapper(cylinderMapper)
cylinderActor.GetProperty().SetColor(tomato)
cylinderActor.RotateX(30.0)
cylinderActor.RotateY(-45)


#Create Graphics structure. The renderer renders into the window
#The window interactor captures mouse events and will perform camera or actor manipulation
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renWin)

style = vtk.vtkInteractorStyleTrackballCamera()
interactor.SetInteractorStyle(style)

#add actors to renderer, set background and color
ren.AddActor(cylinderActor)
ren.SetBackground(0.1,0.2,0.4)
renWin.SetSize(200,200)

#start interactor (must be called before an event loop)
interactor.Initialize()

#access camera
ren.ResetCamera()
ren.GetActiveCamera().Zoom(1.5)
renWin.Render()

#Start event loop
interactor.Initialize()
interactor.Start()


#release 





