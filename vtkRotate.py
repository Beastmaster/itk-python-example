'''
Author: QIN Shuo
Date: 2015/12/17
Description:
    This file demonstrate how to manipulate position/size/direction 
    of a image.
Tips:
    There are 2 ways to achieve this goal.
    1. Manipulate actor. This method would not change properties of
        a image object, it only change view of the actor
    2. Apply transform image. This way will change properties of the
        image and more unlities have not been tested

Bugs:
    This version of demo seem to exists some problems

'''

import vtk
import sys
import time

class MyStyle(vtk.vtkInteractorStyleTrackballActor):
    def OnLeftButtonDown(self):
        print("pressed left mouse button",time.gmtime())
        m = vtk.vtkMatrix4x4
        self.Actor.GetMatrix(m)
        print("matrix:\n",m)
        vtk.vtkInteractorStyleTrackballActor.OnLeftButtonDown()

    def OnLeftButtonUp(self):
        print("released left mouse button")
        m = vtk.vtkMatrix4x4()
        self.Actor.GetMatrix(m)
        print("matrix",m)
        vtk.vtkInteractorStyleTrackballActor.OnLeftButtonUp()
    def SetActor(self,actor):
        self.Actor = actor


coneSource = vtk.vtkConeSource()
coneSource.Update()
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(coneSource.GetOutput())

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.RotateY(45)

renderer = vtk.vtkRenderer()
renderWin = vtk.vtkRenderWindow()
interactor = vtk.vtkRenderWindowInteractor()

renderWin.AddRenderer(renderer)
interactor.SetRenderWindow(renderWin)

style = MyStyle()
style.SetActor(actor)

interactor.SetInteractorStyle(style)

renderer.AddActor(actor)
renderer.SetBackground(1,1,1)

renderWin.Render()
interactor.Start()










