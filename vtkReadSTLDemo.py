#Author:  QinShuo
#Date:  2015/10/27
#Description:
#  This module demonstrate how to use vtk in python
#  python + vtk
#  Read a .stl file and display


import vtk
from vtk import * 

#vtk STL data reader
reader = vtk.vtkSTLReader()
reader.SetFileName('C:/Users/qinsh/Desktop/pika.stl/bamax.stl')
reader.Update()

#vtk mapper
mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(reader.GetOutput())
else:
    mapper.SetInputConnection(reader.GetOutputPort())

# actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
 
# create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
 

# assign actor to the renderer
ren.AddActor(actor)
 
# enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()

