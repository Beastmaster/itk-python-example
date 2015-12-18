'''
Author: QIN Shuo
Date: 2015/12/18
Description:


Function:
    Overlay display of 2 images using 2 layered renderers

'''

import vtk


class my_style(vtk.vtkInteractorStyleImage):
    def __init__(self):
        # index
        self.ori_index = [0,0,0]
        self.ori_direction = [1,1,1] #cosine
        self.cur_index = [0,0,0]
        self.cur_direction = [1,1,1] #cosine
        #define reslice fileter
        self.reslicer = vtk.vtkImageReslice()
        self.reslicer.SetOutputDimensionality(2) #output 2D resliced image
        self.reslicer.SetResliceAxesDirectionCosines([0,0,0,0,0,0,0,0,0])#(self.cur_direction[1],self.cur_direction[1],self.cur_direction[1])
        self.reslicer.SetResliceAxesOrigin(0,0,0)#(self.cur_index)
        self.reslicer.SetInterpolationModeToLinear()

    def SetImage(self,img):
        self.reslicer.SetInputData(img)

    def SetSlice(self,x,y,z):
        self.cur_direction = [x,y,z]

    def OnMouseWheelForward(self):
        print("Mouse Wheel Forward")
        self.reslicer.Update()
    def OnMouseWheelBackward(self):
        print("Mouse Wheel Backward")
        self.reslicer.Update()

sphere = vtk.vtkSphereSource()
sphere.Update()

sphereMpper = vtk.vtkPolyDataMapper()
sphereMpper.SetInputData(sphere.GetOutput())

sphereActor = vtk.vtkActor()
sphereActor.SetMapper(sphereMpper)

textSource = vtk.vtkVectorText()
textSource.SetText("TXT")
textSource.Update()

textMapper = vtk.vtkPolyDataMapper()
textMapper.SetInputData(textSource.GetOutput())

textActor = vtk.vtkActor()
textActor.SetMapper(textMapper)


renderer1 = vtk.vtkRenderer()
renderer2 = vtk.vtkRenderer()

#layer index
renderer1.SetLayer(0)
renderer2.SetLayer(1)

# apply identical camera to 2 renderers
renderer2.SetActiveCamera(renderer1.GetActiveCamera())

renderWin = vtk.vtkRenderWindow()
renderWin.AddRenderer(renderer1)
renderWin.AddRenderer(renderer2)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderWin)
#style = vtk.vtkInteractorStyleTrackballActor()
style = my_style()
interactor.SetInteractorStyle(style)

renderer1.AddActor(sphereActor)
renderer2.AddActor(textActor)

renderWin.SetNumberOfLayers(2)
renderer1.ResetCamera()
renderWin.Render()
interactor.Start()


