'''
Author: QIN Shuo
Date: 2016/3/30

Description: 
    This demo demonstrate how to use vtkImagePlaneSource

    Implement 4 renderer in a window

'''


import vtk
import sys
import string


def ReadNii(filename):
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(filename)
    reader.Update()
    return reader.GetOutput()


def ImagePlaneDemo(img):

    # create a window
    window = vtk.vtkRenderWindow()
    
    # create interactor
    interactor = vtk.vtkRenderWindowInteractor()
    window.SetInteractor(interactor)


    # create 4 renderers
    xmins = [0,.5,0,.5]
    xmaxs = [0.5,1,0.5,1]
    ymins = [0,0,0.5,0.5]
    ymaxs = [0.5,0.5,1,1]
    render_list = []
    for i in range(4):
        renderer = vtk.vtkRenderer()
        render_list.append(renderer)

        window.AddRenderer(renderer)
        renderer.SetViewport(xmins[i],ymins[i],xmaxs[i],ymaxs[i])
    
    # create plane source here
    plane_X = vtk.vtkImagePlaneWidget()
    plane_Y = vtk.vtkImagePlaneWidget()
    plane_Z = vtk.vtkImagePlaneWidget()

    plane_X.SetInteractor(interactor)
    plane_Y.SetInteractor(interactor)
    plane_Z.SetInteractor(interactor)
    plane_X.SetDefaultRenderer(render_list[0])
    plane_Y.SetDefaultRenderer(render_list[1])
    plane_Z.SetDefaultRenderer(render_list[2])

    plane_X.SetCurrentRenderer(render_list[3])
    plane_Y.SetCurrentRenderer(render_list[3])
    plane_Z.SetCurrentRenderer(render_list[3])

    plane_X.SetInputData(img)
    plane_Y.SetInputData(img)
    plane_Z.SetInputData(img)

    plane_X.SetPlaneOrientationToXAxes()
    plane_Y.SetPlaneOrientationToYAxes()
    plane_Z.SetPlaneOrientationToZAxes()

    plane_X.On()
    plane_Y.On()
    plane_Z.On()

    window.Render()
    interactor.Start()




if __name__ == '__main__':
    #file_name = sys.argv[1]
    file_name = "E:/test/a1.nii"
    
    source = ReadNii(file_name)
    ImagePlaneDemo(source)


