'''
MarchingCubes

Add ball

mouse click 

'''

import vtk
import sys

def MarchingCube(image,threshold):
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


if __name__ == '__main__':
    from QuickView import visualize_poly
    ff = 'D:/data/skull.nii'
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(ff)
    reader.Update()
    im = reader.GetOutput()
    poly = MarchingCube(im,5)
    visualize_poly(poly)

