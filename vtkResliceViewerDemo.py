#Author: Qin Shuo
#Date:   2015/10/27
#Description:
#  This example how to use vtkResliceImageViewer
#  vtkResliceImageViewer display a image along a 2 cross hairs for reslicing
#  Usefule functions: reslice mode


import vtk
import sys

directory = 'E:/test/ct_spine'

def DisplayImageData(data):
    viewer = vtk.vtkResliceImageViewer()
    interactor = vtk.vtkRenderWindowInteractor()
    interactor.SetRenderWindow(viewer.GetRenderWindow())
    
    viewer.SetupInteractor(interactor)
    viewer.SetInputData(data)
    
    # calculate index of middle slice in the dicom image
    midSlice = viewer.GetSliceMax()/2
    
    # set up reslice view properties
    viewer.SetSlice(midSlice)
    viewer.SetSliceOrientationToXY()
    viewer.GetRenderer().ResetCamera()
    viewer.Render()
    
    interactor.Start()

#vtk dicom reader, input dicom directory
def DisplayDicom(folder = directory):
    reader = vtk.vtkDICOMImageReader()
    reader.SetDirectoryName(directory)
    reader.Update()
    DisplayImageData(reader.GetOutput())


if __name__ == '__main__':
    DisplayDicom()

