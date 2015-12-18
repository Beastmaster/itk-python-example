'''
Author: QIN Shuo
Date: 2015/12/18
Description:
    This file demonstrate how to interact in vtk

    This file will employ 2 method (actually 2 similar
    mthod to achieve the goal):
    1. Re-load vtkInteractorStyleImage, add observer
       to this class.
    2. Define callback function and add observer to
       vtk window interactor.

    EventID are defined in vtkCommand class



    Tips:

     class MyStyle(vtk.vtkInteractorStyleImage):
        def __init__(self):
            pass
        def OnMouseWheelForward(self):
            pass

     the above method will not re-load the mouse wheel function
     the real functional method are applied by adding event observer

'''





import vtk













# define a interactor style that re-implement all event callback











