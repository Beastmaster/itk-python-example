'''
Author: QIN Shuo
Date: 2015/12/17
Description:
    This file demonstrate how to manipulate position/size/direction 
    of a image.
Tips:
    Method to get element of vtkMatrix4x4 is using GetElement(i,j)

    You must re-render the window to apply the rotate transform

    There are 2 ways to achieve this goal.
    1. Manipulate actor. This method would not change properties of
        a image object, it only change view of the actor
    2. Apply transform image. This way will change properties of the
        image and more unlities have not been tested



'''

import vtk
import sys
import time

class MyStyle(vtk.vtkInteractorStyleImage):
    def __init__(self):
        self.AddObserver("LeftButtonPressEvent",self.OnLeftButtonDown)
        self.AddObserver("LeftButtonReleaseEvent",self.OnLeftButtonUp)
        self.AddObserver("MouseWheelForwardEvent",self.OnMouseWheelForward)
        self.AddObserver("MouseWheelBackwardEvent",self.OnMouseWheelBackward)
    def OnLeftButtonDown(self,obj,event):
        print("pressed left mouse button",time.gmtime())
        m = vtk.vtkMatrix4x4()
        self.Actor.GetMatrix(m)
        print "matrix is :"
        for i in range(0,2):
            for j in range(0,2):
                print (m.GetElement(i,j))
    def OnLeftButtonUp(self,obj,event):
        print("released left mouse button")
        m = vtk.vtkMatrix4x4()
        print "matrix is :"
        for i in range(0,2):
            for j in range(0,2):
                print (m.GetElement(i,j))
    def OnMouseWheelForward(self,obj,event):
        print("mouse wheel forward")
        self.Actor.RotateY(10)
        self.win.Render()
    def OnMouseWheelBackward(self,obj,event):
        print ("mouse wheel backward")
        self.Actor.RotateY(-10)
        self.win.Render()

    def SetActor(self,actor):
        self.Actor = actor
    def SetWindow(self,win):
        self.win = win


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
style.SetWindow(renderWin)

interactor.SetInteractorStyle(style)

renderer.AddActor(actor)
renderer.SetBackground(1,1,1)

renderWin.Render()
interactor.Start()










