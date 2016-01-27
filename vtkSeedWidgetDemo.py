# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:42:59 2016

@author: qinshuo
"""



import vtk


render = vtk.vtkRenderer()

win = vtk.vtkRenderWindow()
win.AddRenderer(render)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(win)


# create a representation
handleRep = vtk.vtkPointHandleRepresentation2D()
handleRep.GetProperty().SetColor(1,1,0)

widgetRep = vtk.vtkSeedRepresentation()
widgetRep.SetHandleRepresentation(handleRep)

# create a seedwidget here
seedWidget = vtk.vtkSeedWidget()

seedWidget.SetInteractor(interactor)
seedWidget.SetRepresentation(widgetRep)


seedWidget.On()
interactor.Start()


