'''
MarchingCubes

Add ball

mouse click 

'''

import vtk
import sys

def MarchingCubes(image,threshold):
    '''
    http://www.vtk.org/Wiki/VTK/Examples/Cxx/Modelling/ExtractLargestIsosurface 
    '''
    mc = vtk.vtkMarchingCubes()
    mc.SetInputData(image)
    mc.ComputeNormalsOn()
    mc.ComputeGradientsOn()
    mc.SetValue(0, threshold)
    mc.Update()
    
    # To remain largest region
    confilter =vtk.vtkPolyDataConnectivityFilter()
    confilter.SetInputData(mc.GetOutput())
    confilter.SetExtractionModeToLargestRegion()
    confilter.Update()

    return confilter.GetOutput()


def Smooth_stl(stl):
    smoothFilter = vtk.vtkSmoothPolyDataFilter()
    smoothFilter.SetInputConnection(stl)
    smoothFilter.SetNumberOfIterations(15)
    smoothFilter.SetRelaxationFactor(0.1)
    smoothFilter.FeatureEdgeSmoothingOff()
    smoothFilter.BoundarySmoothingOn()
    smoothFilter.Update()

if __name__ == '__main__':
    #from QuickView import visualize_poly
    ff = '1-L1_th.nii'
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(ff)
    reader.Update()
    im = reader.GetOutput()
    poly = MarchingCubes(im,1)
    #visualize_poly(poly)
    writer = vtk.vtkSTLWriter()
    writer.SetInputData(poly)
    writer.SetFileName('xx.stl')
    writer.Update()

