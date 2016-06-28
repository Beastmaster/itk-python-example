'''
Author: Qin Shuo
Date:   2016/03/22
Description:
    Demo: how to manipulate the poly data
    1. xml poly data, .vtp format

    Main:  vtk.vtkTransformFilter()
'''

import string
import vtk
import sys

def ReadPolyFile(filename):
    list = filename.split(".")
    surfix = list.pop()
    if surfix=="vtp":
        print "vtp file"

        #read vtp file here
        reader = vtk.vtkXMLPolyDataWriter()
        reader.SetFileName(filename)
        reader.Update()
        return reader.GetOutput()

    elif surfix == "stl":
        print "stl file"

        #read stl file here
        reader = vtk.vtkSTLReader()
        reader.SetFileName(filename)
        reader.Update()
        return reader.GetOutput()
    else:
        return 0
    

def WriteSTL(obj,filname):
    writer = vtk.vtkSTLWriter()
    writer.SetFileName(filename)
    writer.SetInputData(obj)
    writer.Update()




    

def vtkManipulatePolyData(filename):

    poly = ReadPolyFile(filename)
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(poly)
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)


    # visualization
    print "visualizing..."

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    
    global pos_X
    global pos_Y
    global pos_Z
    global translate

    pos_X = 0
    pos_Y = 0
    pos_Z = 0
    translate = vtk.vtkTransform()

    # Main function to manipulate transform
    def KeyPressEvent(obj,event):
        global pos_X
        global pos_Y
        global pos_Z

        print("key pressed")
        key = obj.GetKeySym()
        if key == "Up":
            pos_Y = pos_Y+1
            print pos_Y
            pass
        elif key == "Down":
            pos_Y = pos_Y-1
            print pos_Y
            pass
        elif key == "Left":
            pos_X = pos_X+1
            print pos_X
            pass
        elif key == "Right":
            pos_X = pos_X-1
            print pos_X
            pass
        elif key == "1":
            pos_Z = pos_Z-1
            print pos_X
            pass
        elif key == "2":
            pos_Z = pos_Z-1
            print pos_Z
            pass
        elif key=="s":
            trans = vtk.vtkTransformFilter()
            trans.SetTransform(translate)
            trans.SetInputData(poly)
            trans.Update()
            # write
            writer = vtk.vtkSTLWriter()
            writer.SetInputData(trans.GetOutput())
            pos = filename.rfind("/")
            new_name = filename[:pos+1]+"new_"+filename[pos+1:]
            print new_name
            writer.SetFileName(new_name)
            writer.Update()
        else:
            pass
        translate.Translate(pos_X,pos_Y,pos_Z)
        actor.SetUserTransform(translate)
        window.Render()


    interactor.AddObserver(vtk.vtkCommand.KeyPressEvent,KeyPressEvent)
    window.SetInteractor(interactor)

    window.Render()
    interactor.Start()






if __name__ == '__main__':
    #file_name = sys.argv[1]
    #if len(sys.argv)<2:
    file_name = "E:/test/coil__2_s.stl"
    vtkManipulatePolyData(file_name)
