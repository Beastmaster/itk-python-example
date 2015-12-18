'''
Author: QIN Shuo
Date: 2015/12/17

Description:
    This file demonstrate how to change properties ( direction /
    size/ transformation) of an image object. THis method is 
    different the method to change vtkActor

'''


import vtk

coneSource = vtk.vtkConeSource()
coneSource.Update()

# original source
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(coneSource.GetOutput())
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)

# apply a transform to a source
translation = vtk.vtkTransform()
translation.Translate(1,0,0)
#translation.Scale(1,2,2)
print("translation",translation.GetScale())

transformFilter = vtk.vtkTransformFilter()
transformFilter.SetInputData(coneSource.GetOutput())
transformFilter.SetTransform(translation)
transformFilter.Update()

#print("applying transform",transformFilter.GetScale())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(transformFilter.GetOutput())
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)




renderer = vtk.vtkRenderer()
renderWin = vtk.vtkRenderWindow()
interactor = vtk.vtkRenderWindowInteractor()
renderWin.AddRenderer(renderer)
interactor.SetRenderWindow(renderWin)
interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballActor())

#
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.SetBackground(1,1,1)

renderWin.Render()
interactor.Start()




