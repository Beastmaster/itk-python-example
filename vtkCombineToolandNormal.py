'''
Author: QIN Shuo
Date: 2016/3/31
Organization: RC-MIC (CUHK)

Description: 
    Function: Combine a coil model with a line (focus, normal)

    Filters:  Combine 2 poly data   // vtkAppendPolyData vtkCleanPolyData
              Create a poly source
              Compute normal
              Mouse select a position (mouse click callback)
              Transform a polydata(the focus line)


SubSystem:
    TMS Navigation

'''




import vtk
import sys
import string

# read stl function
def ReadSTL(filename):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(filename)
    reader.Update()
    return reader.GetOutput()

# write stl function
def WriteSTL(filename,stl):
    writer = vtk.vtkSTLWriter()
    writer.SetFileName(filename)
    writer.SetInputData(stl)
    writer.Update()
    

# create a line source, format: vtkPolyData
def CreateLine():
    cylinder = vtk.vtkCylinderSource()
    cylinder.SetCenter(0,0,0)
    cylinder.SetRadius(1.0)
    cylinder.SetHeight(200)
    cylinder.SetResolution(100)
    cylinder.Update()
    source = cylinder.GetOutput()
    return source
    

def TransformSTL(src,transform):
    trans = vtk.vtkTransformFilter()
    trans.SetTransform(transform)
    trans.SetInputData(src)
    trans.Update()
    return trans.GetOutput()
    

def ConbineSource(coil,line):
    # combine 2 source
    appendFilter = vtk.vtkAppendPolyData()
    appendFilter.AddInputData(coil)
    appendFilter.AddInputData(line)
    appendFilter.Update()
    # remove duplicate points
    poly_clean = vtk.vtkCleanPolyData()
    poly_clean.SetInputData(appendFilter.GetOutput())
    poly_clean.Update()

    tri = vtk.vtkTriangleFilter()
    tri.SetInputData(poly_clean.GetOutput())
    tri.Update()

    geometryFilter = vtk.vtkGeometryFilter()
    geometryFilter.SetInputData(tri.GetOutput())
    geometryFilter.Update()

    return geometryFilter.GetOutput()
    
def Visualize(coil):
    line = CreateLine()
    line_mapper = vtk.vtkPolyDataMapper()
    line_mapper.SetInputData(line)
    global line_actor
    line_actor = vtk.vtkActor()
    line_actor.SetMapper(line_mapper)


    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(coil)

    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    global renderer
    global interactor

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    renderer.AddActor(line_actor)
    win = vtk.vtkRenderWindow()
    win.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    win.SetInteractor(interactor)

    def LeftButtonPressEvent(obj,event):
        global line_actor
        global interactor
        global renderer
        coor = interactor.GetEventPosition()
        print "coordinate is ", coor
        interactor.GetPicker().Pick(interactor.GetEventPosition()[0],interactor.GetEventPosition()[1],0,renderer)
        picked = interactor.GetPicker().GetPickPosition()
        print "position is ",picked
        point = interactor.GetPicker().GetSelectionPoint()
        print "point is", point

        # translation
        global transform
        transform = vtk.vtkTransform()
        transform.Translate(picked)
        line_actor.SetUserTransform(transform)
    
        
    def keyPressEvent(obj,event):
        global line_actor
        global interactor
        global renderer
        #key = .GetInteractor().GetKeySym()
        key = obj.GetKeySym()
        print key
        # translation
        if key == "h":
            print "key is ",key
            coor = interactor.GetEventPosition()
            print "coordinate is ", coor
            interactor.GetPicker().Pick(interactor.GetEventPosition()[0],interactor.GetEventPosition()[1],0,renderer)
            picked = interactor.GetPicker().GetPickPosition()
            print "position is ",picked
            point = interactor.GetPicker().GetSelectionPoint()
            print "point is", point
            
            # translation
            global transform
            transform = vtk.vtkTransform()
            transform.Translate(picked)
            line_actor.SetUserTransform(transform)
            win.Render()
        else:
            pass

    #interactor.AddObserver(vtk.vtkCommand.LeftButtonPressEvent,LeftButtonPressEvent)
    interactor.AddObserver(vtk.vtkCommand.KeyPressEvent,keyPressEvent)

    win.Render()
    interactor.Start()
    pass



if __name__ == '__main__':
    if len(sys.argv)<2:
        print "Input Error: you must input 2 parameters"
        print "Para1: Source model file name, a .stl file"
        print "Para2: Output model file name, a .stl file"
        in_file = "E:/test/QinShuoTShapeM.stl"
        out_file = "E:/test/newQinShuoTShapeM.stl"
    else:
        in_file = sys.argv[1]
        out_file = sys.argv[2]
    
    print "Press \"h\" to append the line"

    print "Reading STL"
    coil = ReadSTL(in_file)

    print "Visulizing"
    Visualize(coil)

    print "Create a line source"
    line = CreateLine()

    print "Transforming the line source"
    t_line = TransformSTL(line,transform)

    print "Combing the coil and line"
    res = ConbineSource(coil,t_line)

    print "Writing to file:  "+ out_file
    WriteSTL(out_file,res)
 

