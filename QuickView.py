# Author: QIN Shuo
# Date:   2015/10/27
# This file implement a quick view class for ITK
# The native quick view in ITK seems not to be exported to python
# This script is transformed strictly depend on ITK C++ source file


#import itk
import vtk
import sys

class QuickView:
    def __init__(self,ImageType):
        self.m_ImageType = ImageType
        self.m_ShareCamera = True
        self.m_Interpolate = True
        self.m_Counter = 0
        self.m_Snapshot = False
        self.m_SnapshotPath = ""
        self.m_SnapshotPrefix = "snapshot_"
        self.m_SnapshotExtension = "png"
        self.i2vConnector = itk.ImageToVTKImageFilter[self.m_ImageType]

    def AddImage(self,image):
        #rescal image
        UC_Type = itk.Image[itk.UC,2]
        rescalType = itk.RescaleIntensityImageFilter[self.m_ImageType,UC_Type]
        rescaler = rescalType.New()
        rescaler.SetOutputMinimum(0)
        rescaler.SetOutputMaximum(255)
        rescaler.SetInput(image)
        #flip verticle
        flipper = itk.FlipImageFilter[self.m_ImageType].New()
        flipAxes = itk.FixedArray[itk.B,2]()
        flipAxes.SetElement(0,False)
        flipAxes.SetElement(1,True)
        #flipAxes.SetElement(2,False)
        flipper.SetFlipAxes(flipAxes)
        flipper.SetInput(image)
        flipper.Update()
        self.m_Image = flipper.GetOutput()


    def Visualize(self):
        renderSize = 300;
        numberOfImages = 1;   #implement only one image visulization

        # Setup the render window and interactor
        renderWindow = vtk.vtkRenderWindow()
        renderWindow.SetSize(renderSize * numberOfImages, renderSize)

        interactor = vtk.vtkRenderWindowInteractor()
        interactor.SetRenderWindow(renderWindow)

        style = vtk.vtkInteractorStyleImage()
        interactor.SetInteractorStyle(style)

        # Render all of the images
        background = [0.4,0.5,0.6]

        sharedCamera = vtk.vtkCamera()
        actor = vtk.vtkImageActor()

        #connect itk image to vtk image
        connector = self.i2vConnector.New()
        connector.SetInput(self.m_Image)

        actor.SetInput(connector.GetOutput())

        renderer = vtk.vtkRenderer()
        renderWindow.AddRenderer(renderer)
        #renderer.SetViewpint()
        renderer.SetBackground(background)


        # start visualization
        renderer.AddActor(actor)
        renderer.ResetCamera()

        renderWindow.Render()

        # start interactor
        interactor.Start()

    # implement with vtkImageViewer2
    # vtkImageViewer2 provide no slice change when scroll mouse
    # implement callback function or use vtkResliceImageViewer
    def Visualize2(self):
        #connect itk image to vtk image
        connector = self.i2vConnector.New()
        connector.SetInput(self.m_Image)

        viewer2 = vtk.vtkImageViewer2()
        viewer2.SetInput(connector.GetOutput())

        interactor = vtk.vtkRenderWindowInteractor()
        viewer2.SetupInteractor(interactor)
        viewer2.Render()
        viewer2.GetRenderer().ResetCamera()
        viewer2.Render()

        interactor.Start()
        


def visualize_poly(*poly):
    def create_actor(poly):
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(poly)
        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        return actor

    actor_list = []
    for pp in poly:
        actor_list.append(create_actor(pp))


    renderer = vtk.vtkRenderer()
    for actor in actor_list:
        renderer.AddActor(actor)

    renWin = vtk.vtkRenderWindow()
    renWin.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    renWin.SetInteractor(interactor)
    interactor.Start()
