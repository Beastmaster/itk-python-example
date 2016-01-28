'''
 Author: QIN Shuo
 Date:   2016/1/28
 This is a example file for vtk
 Description:
    Get scalar type of imagedata


    type list:

#define VTK_VOID            0
#define VTK_BIT             1
#define VTK_CHAR            2
#define VTK_SIGNED_CHAR    15
#define VTK_UNSIGNED_CHAR   3
#define VTK_SHORT           4
#define VTK_UNSIGNED_SHORT  5
#define VTK_INT             6
#define VTK_UNSIGNED_INT    7
#define VTK_LONG            8
#define VTK_UNSIGNED_LONG   9
#define VTK_FLOAT          10
#define VTK_DOUBLE         11
#define VTK_ID_TYPE        12




'''



import vtk
import os

folder_path = "E:/test/david/"

for i in os.listdir(folder_path): #(os.getcwd()):
    if (i.endswith(".nii") or i.endswith(".py")) and i.find("new") == -1: 
        name = folder_path + i
        print "file ",i
        reader = vtk.vtkNIFTIImageReader()
        reader.SetFileName(name)
        reader.Update()
        print "type is: ",reader.GetDataScalarType()
        matrix = reader.GetQFormMatrix()
        print "Ori QForm Matrix is",matrix


        caster = vtk.vtkImageCast()
        caster.SetInputData(reader.GetOutput())
        caster.SetOutputScalarTypeToInt()
        caster.Update()

        i2 = "new"+i
        print "writing to", i2
        writer = vtk.vtkNIFTIImageWriter()
        #writer.SetQFac(-1)
        writer.SetQFormMatrix(matrix)
        writer.SetFileName(folder_path+i2)
        writer.SetInputData(caster.GetOutput())
        writer.Update()
    else:
        pass


print "Done!!"





