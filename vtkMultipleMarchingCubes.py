'''
Author: Qin Shuo
Date:   2016/03/22
Description:
    This script is used to generate a 
    multiple scalar surface to visiualize 
    different brain area from a templete and atlas

    Refer to: Combine polydata example

    MarchingCubes
    vtkPolyData
    vtkAppendPolyData
    vtkCleanPolyData

Bugs:
    There is a bug:
    Cannot assign scalar to polydata cells or points

'''

import sys
import string
import vtk

color_map = "C:/Users/QIN Shuo/Desktop/MRIcron/templates/aal.nii.txt"
atlas = "C:/Users/QIN Shuo/Desktop/MRIcron/templates/aal.nii"

def vtkMultipleMarchingCubes(atlas,color_map):
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(atlas)
    reader.Update()

    image = reader.GetOutput()

    # read color map
    color_list = ReadColorMap(color_map)

    # create vtkAppendPolyData Filter
    poly_append = vtk.vtkAppendPolyData()

    # run marchingcubes for each label
    #for color in color_list:
    for i in range(0,5):
        color = color_list[i]
        print "Color: ",color[0]

        # threshold
        threshold = vtk.vtkImageThreshold()
        threshold.SetInputData(image)
        threshold.ThresholdBetween(color[0],color[0])
        threshold.ReplaceOutOn()
        threshold.SetOutValue(0)
        threshold.Update()
        image1 = threshold.GetOutput()
       
        marching = vtk.vtkMarchingCubes()
        marching.SetInputData(image1)
        marching.SetValue(0,color[0])
        marching.Update()
        area = marching.GetOutput()

        # create color table
        colors = vtk.vtkUnsignedCharArray()
        colors.SetNumberOfComponents(3)
        colors.SetName(color[1])
        colors.InsertNextTupleValue([color[0],1,1])
        area.GetCellData().Update()
        area.GetCellData().SetScalars(colors)
        #area.GetPointData().SetScalars(colors)
        poly_append.AddInputData(area)
    poly_append.Update()

    # clean
    print "Cleaning... "
    poly_clean = vtk.vtkCleanPolyData()
    poly_clean.SetInputData(poly_append.GetOutput())
    poly_clean.Update()

    # visualization
    print "visualizing..."
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(poly_append.GetOutput())
    #mapper.ScalarVisibilityOn()
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    window.SetInteractor(interactor)
    
    window.Render()
    interactor.Start()
    pass

# read color map function
def ReadColorMap(color_file):
    file = open(color_file,"r")
    list = []
    for line in file:
        cln_line = line.strip()
        tup = cln_line.split(' ')
        if len(tup)>2:
            tuple = (string.atoi(tup[0]),tup[1],string.atoi(tup[2]))
            list.append(tuple)
    return list

def TestMarching(atlas):
    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(atlas)
    reader.Update()
    image = reader.GetOutput()
    
    # threshold
    threshold = vtk.vtkImageThreshold()
    threshold.SetInputData(image)
    threshold.ThresholdBetween(60,60)
    threshold.ReplaceOutOn()
    threshold.SetOutValue(0)
    threshold.Update()
    image1 = threshold.GetOutput()

    marching = vtk.vtkMarchingCubes()
    marching.SetInputData(image1)
    marching.SetValue(0,60)
    marching.Update()
    area = marching.GetOutput()
    
    colors = vtk.vtkUnsignedCharArray()
    colors.SetNumberOfComponents(3)
    colors.SetName("test")
    colors.InsertNextTupleValue([0,1,1])
    area.GetCellData().SetScalars(colors)
    
    # visualization
    print "visualizing..."
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(area)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    window.SetInteractor(interactor)
    window.Render()
    interactor.Start()

#TestMarching(atlas)

vtkMultipleMarchingCubes(atlas,color_map)


'''
if __name__ == '__main__':
    file_name = sys.argv[1]
    MarchingCube(file_name)
'''