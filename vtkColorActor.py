'''
Author: Qin Shuo
Date:   2016/03/22
Description:
    Create a sphere (vtkpolydata type)
    Assign color and display
'''



import vtk
import sys
import string


def CreateSphere():
    # sphere source
    # Document: http://www.vtk.org/doc/nightly/html/classvtkSphereSource.html
    sphereSrc = vtk.vtkSphereSource()
    sphereSrc.SetRadius(10.0)
    sphereSrc.SetCenter(0.0,0.0,0.0)
    sphereSrc.SetThetaResolution(20)
    sphereSrc.Update()
    return sphereSrc.GetOutput()


def display_color_actor(poly):
    # visualization
    print "visualizing..."
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(poly)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(0.5,0.5,0.0)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    window.SetInteractor(interactor)

    window.Render()
    interactor.Start()




if __name__ == '__main__':
    
    sphere = CreateSphere()
    display_color_actor(sphere)
