'''
Author: Qin Shuo
Date:   2017/1/16
Description:
    This file demo some vtk Readers 
    Return a vtkImageData format
Support format ():
1. dicom
2. nii / nii.gz
3. mha/mhd
'''


import vtk


def MetaReader(ff):
    '''
    http://www.vtk.org/Wiki/VTK/Examples/Cxx/IO/MetaImageReader
    '''
    reader = vtk.vtkMetaImageReader()
    reader.SetFileName(ff)
    reader.Update()
    return reader.GetOutput()


def NiftiReader(ff):
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(ff)
    reader.Update()
    return reader.GetOutput()
    



def DicomReader(ff):
    reader = vtk.vtkDICOMImageReader()
    reader.SetFileName(ff)
    reader.Update()
    return reader.GetOutput()


def DiconSeriesReader(path):
    '''
    http://www.vtk.org/Wiki/VTK/Examples/Cxx/IO/ReadDICOMSeries
    '''
    reader = vtk.vtkDICOMImageReader()
    reader.SetDirectoryName(ff)
    reader.Update()
    return reader.GetOutput()


