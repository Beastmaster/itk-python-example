
'''
test file
Author: QIN Shuo
Date: 2015/12/17

Description:
    This file demonstrate how to change image visilization propties.

(to be continued)
'''

#!/bin/python
import sys
import os
import vtk
import itk


source = vtk.vtkImageEllipsoidSource()

source.SetWholeExtent(0,20,0,20,0,20)

source .SetCenter(10,10,0)
