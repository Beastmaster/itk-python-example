'''
Author: QIN Shuo
Date: 2012/12/17

Description:
    this file demonstrate how to find the version of VTK
'''


#!/bin/python


import vtk
import os
import sys



print vtk.VTK_MAJOR_VERSION     # Major version 
print vtk.ver_MINOR_VERSION     # Minor version

print vtk.VTK_VERSION           # full version of vtk
print vtk.VTK_SOURCE_VERSION    # same as VTK_VERSION
