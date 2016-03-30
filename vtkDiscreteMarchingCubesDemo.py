'''
Author: Qin Shuo
Date:   2016/03/22
Description:
    This script is used to generate a 
    multiple scalar surface to visiualize 
    different brain area from a templete and atlas
'''



import vtk
import sys
import string

filename = "C:/Users/QIN Shuo/Desktop/MRIcron/templates/aal.nii"
color_map = "C:/Users/QIN Shuo/Desktop/MRIcron/templates/aal.nii.txt"
nifti_reader = vtk.vtkNIFTIImageReader()
nifti_reader.SetFileName(filename)
nifti_reader.Update()
image = nifti_reader.GetOutput()


def CreateLookUpTable(file_name):
    
    file = open(file_name,"r")
    list = []
    for line in file:
        cln_line = line.strip()
        tup = cln_line.split(' ')
        if len(tup)>2:
            tuple = (string.atoi(tup[0]),tup[1],string.atoi(tup[2]))
            list.append(tuple)
    
    lut = vtk.vtkLookupTable()
    lut.SetNumberOfTableValues(len(list)+1)
    lut.Build()
    lut.SetTableValue(0,1,1,1,1)
    for var in range(1,len(list)):
        if var<40:
            lut.SetTableValue(var,float(var)/40,0,0,1)
        elif var<80:
            lut.SetTableValue(var,0,float(var-40)/40,0,1)
        else:
            lut.SetTableValue(var,0,0,float(var-80)/40,1)

    return lut



def DiscreteMarchingCubes(image):
    
    # Main part of discretemarchingcubes
    discreteCubes = vtk.vtkDiscreteMarchingCubes()
    discreteCubes.SetInputData(image)
    discreteCubes.GenerateValues( 116, 1-50,116-50);
    discreteCubes.Update()
    for i in range(0,116):
        print discreteCubes.GetValue(i)


    lut = CreateLookUpTable(color_map);

    # visualization
    print "visualizing..."
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(discreteCubes.GetOutput())
    mapper.ScalarVisibilityOn()
    mapper.SetScalarRange(0,4)
    mapper.SetLookupTable(lut)
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




DiscreteMarchingCubes(image)






'''
if __name__ == '__main__':
    file_name = sys.argv[1]
    MarchingCube(file_name)
'''

