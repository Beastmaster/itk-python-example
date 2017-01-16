'''
Author: QIN Shuo
Date: 2017/1/16

Description:
    Demo to connect vtk with numpy
'''



import vtk
from vtk.util import numpy_support
import numpy as np



def vtkimage2numpy(vtk_img):
    dim = vtk_img.GetDimensions()
    spacing = vtk_img.GetSpacing()
    origin = vtk_img.GetOrigin()

    ########## Key line  ##########
    # 1. convert vtkImagedata to a vtkArray
    vtk_img = vtk_img.GetPointData().GetScalars()  
    # 2. call vtk.util to convert to a numpy array
    npdata = numpy_support.vtk_to_numpy(vtk_img)
    # 3. reshape the array
    npdata = npdata.reshape(dim)
    ########## Key line  ##########

    print 'shape is {}'.format(npdata.shape)
    print 'origin is {}'.format(origin)
    print 'spacing is {}'.format(spacing)

    return npdata


def numpy2vtkimage(npdata,origin,spacing,dim):
    npdata_shape = npdata.shape
    #### flaten the data to 1 dim  ####
    #VTK_data = numpy_support.numpy_to_vtk(num_array=npdata.ravel(), deep=True, array_type=vtk.VTK_FLOAT)
    VTK_data = numpy_support.numpy_to_vtk(num_array=np.reshape(npdata,(-1)), deep=True, array_type=vtk.VTK_FLOAT)

    out_img = vtk.vtkImageData()
    out_img.SetOrigin(origin)
    out_img.SetSpacing(spacing)
    out_img.SetDimensions(dim)
    out_img.GetPointData().SetScalars(VTK_data)

    print 'shape is {}'.format(out_img.GetDimensions())
    print 'origin is {}'.format(out_img.GetOrigin())
    print 'spacing is {}'.format(out_img.GetSpacing())

    return out_img


if __name__ == '__main__':
    
    nii_file = 'D:/data/test.nii'

    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(nii_file)
    reader.Update()
    vtk_img = reader.GetOutput()
    
    dim = vtk_img.GetDimensions()
    spacing = vtk_img.GetSpacing()
    origin = vtk_img.GetOrigin()


    npdata = vtkimage2numpy(vtk_img)
    out_img = numpy2vtkimage(npdata,origin,spacing,dim)

    writer = vtk.vtkNIFTIImageWriter()
    writer.SetFileName('test2.nii')
    writer.SetInputData(out_img)
    writer.Update()
    print "Done"









