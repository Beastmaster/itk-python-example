'''
Author: QIN Shuo
Date: 2017/6/15
Organization: RC-MIC (CUHK)

Description: 
    Smooth vtkPolyData
    Reference: http://www.vtk.org/Wiki/VTK/Examples/Cxx/PolyData/SmoothPolyDataFilter
'''

import vtk
import random


def create_poly():
    points = vtk.vtkPoints()
    GridSize = 20
    z=0.0

    for x in range(-GridSize,GridSize):
        for y in range(-GridSize,GridSize):
            z = 0.05*x*x+0.05*y*y+ random.uniform(-1,1)
            points.InsertNextPoint(x,y,z)
    
    # add the grid points to a polydata object
    inputPoly = vtk.vtkPolyData()
    inputPoly.SetPoints(points)
    delaunay = vtk.vtkDelaunay2D()
    delaunay.SetInputData(inputPoly)
    delaunay.Update()
    return delaunay.GetOutput()

# smooth fileter core
def smoothPoly(poly,num_iter = 15,rlx_factor=0.1):
    '''
    http://www.vtk.org/doc/nightly/html/classvtkSmoothPolyDataFilter.html
    '''
    smoothFilter = vtk.vtkSmoothPolyDataFilter()
    smoothFilter.SetInputData(poly)
    smoothFilter.SetNumberOfIterations(num_iter)
    smoothFilter.SetRelaxationFactor(rlx_factor)
    smoothFilter.FeatureEdgeSmoothingOff()
    #smoothFilter.FeatureEdgeSmoothingOn()
    smoothFilter.BoundarySmoothingOff()
    #smoothFilter.BoundarySmoothingOff()
    smoothFilter.Update()
    return smoothFilter.GetOutput()


def smoothPoly2(poly,iter = 15,feature_angle=120,pass_band=0.001):
    '''
    http://www.vtk.org/doc/nightly/html/classvtkWindowedSincPolyDataFilter.html#details
    '''
    smoother = vtk.vtkWindowedSincPolyDataFilter()
    smoother.SetInputData(poly)
    smoother.SetNumberOfIterations(iter)
    smoother.BoundarySmoothingOff()
    smoother.FeatureEdgeSmoothingOff()
    smoother.SetFeatureAngle(feature_angle)
    smoother.SetPassBand(pass_band)
    smoother.NonManifoldSmoothingOn()
    smoother.NormalizeCoordinatesOn()
    smoother.Update()
    return smoother.GetOutput()

def vis_poly(poly):
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(poly)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    win = vtk.vtkRenderWindow()
    win.AddRenderer(renderer)
    renderer.ResetCamera()
    interactor = vtk.vtkRenderWindowInteractor()
    win.SetInteractor(interactor)
    interactor.Start()

if __name__ == "__main__":
    poly = create_poly()
    polys = smoothPoly(poly)
    vis_poly(polys)


