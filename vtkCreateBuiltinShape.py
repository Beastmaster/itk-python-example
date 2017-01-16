#python for vtk test
#Created by QinShuo
#Date    2015.8.18
# This Demo demonstrate how to create a cylinder and display

'test module'
__author__ = 'Qin Shuo'


import vtk
from QuickView import visualize_poly
from vtk.util.colors import tomato


def vtk_cylinder():
    #create a polygonal cylinder model
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetResolution(8)
    cylinder.Update()
    return cylinder.GetOutput()


def vtk_sphere():
    sphereSrc = vtk.vtkSphereSource()
    sphereSrc.SetRadius(10.0)
    sphereSrc.SetCenter(0.0,0.0,0.0)
    sphereSrc.SetThetaResolution(20)
    sphereSrc.Update()
    return sphereSrc.GetOutput()


