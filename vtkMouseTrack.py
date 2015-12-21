'''
 Author: QIN Shuo
 Date:   2015/11/10
 This is a example file for vtk

Description:
    This file demonstrate how to move actors in a scene view

    1. move the actor in 2 degree of freedom
    2. move the actor in 4 degree of freedom (with button)

'''

import vtk


def CreateActor(source):
    sourceMapper = vtk.vtkPolyDataMapper()
    sourceActor = vtk.vtkActor()
    sourceMapper.SetInputData(source)
    sourceActor.SetMapper(sourceMapper)
    print("create a actor",source.__class__.__name__)
    return sourceActor

def MouseMoveEvent(obj,event):
    global interactor
    global renderer
    global coneActor
    global renWin
    global origin_i
    coor_i = coneActor.GetPosition()
    coor = interactor.GetEventPosition()
    coneActor.SetPosition(coor[0]-origin_i[0]/2,coor[1]-origin_i[1]/2,0)
    print ("mouse position",coor)
    print ("actor position",coor_i)
    renWin.Render()
    pass

# create 2 actors
sphere = vtk.vtkSphereSource()
sphere.Update()
sphereActor = CreateActor(sphere.GetOutput())


cone   = vtk.vtkConeSource()
cone.Update()
coneActor = CreateActor(cone.GetOutput())



renderer = vtk.vtkRenderer()
renWin   = vtk.vtkRenderWindow()
renWin.SetSize(200,200)
interactor = vtk.vtkRenderWindowInteractor()

# get the size of the window and calculate the center
origin_i = renWin.GetSize()
print ("window size",origin_i)

renWin.AddRenderer(renderer)
interactor.SetRenderWindow(renWin)

renderer.AddActor(sphereActor)
renderer.AddActor(coneActor)
renderer.SetBackground(1,1,1)

interactor.AddObserver(vtk.vtkCommand.MouseMoveEvent,MouseMoveEvent)

renWin.Render()
interactor.Start()

