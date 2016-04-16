'''
Author: QIN Shuo
Date: 2016/4/15
Organization: RC-MIC (CUHK)

Description: 
    Function: Visualize the orientation of the model,
              Save the oriented model to file

    Filters:  Combine 2 poly data   // vtkAppendPolyData vtkCleanPolyData
              Create a poly source
              Compute normal
              Mouse select a position (mouse click callback)
              Transform a polydata(the focus line)
'''


import vtk
import sys

# read stl function
def ReadSTL(filename):
    reader = vtk.vtkSTLReader()
    reader.SetFileName(filename)
    reader.Update()
    return reader.GetOutput()


class QIN_Style(vtk.vtkInteractorStyleImage):
    def __init__(self,parent  = None):
        self.AddObserver("KeyPressEvent",self.keyPressEvent)

    def keyPressEvent(self,obj,event):
        key = self.GetInteractor().GetKeySym()
        print key
        self.OnKeyPress()
        return 

    pass



# modify orientation
def vtkModifySTLOrientation():
    global pos_X
    global pos_Y
    global pos_Z
    global ori_X
    global ori_Y
    global ori_Z

    pos_X = 0.0
    pos_Y = 0.0
    pos_Z = 0.0
    ori_X = 0.0
    ori_Y = 0.0
    ori_Z = 0.0

    # Main function to manipulate transform
    def KeyPressEvent(obj,event):
        global pos_X
        global pos_Y
        global pos_Z
        global ori_X
        global ori_Y
        global ori_Z

        

        print("key pressed")
        key = obj.GetKeySym()


    pass


# view orientation
def Visualize_Orientation(model):
    # create coordinate actor
    axes_actor = vtk.vtkAxesActor()
    axes_actor.SetTotalLength(500.0,500.0,500.0)

    # create model actor
    model_mapper = vtk.vtkPolyDataMapper()
    model_mapper.SetInputData(model)
    model_actor = vtk.vtkActor()
    model_actor.SetMapper(model_mapper)


    global renderer
    global interactor

    renderer = vtk.vtkRenderer()
    renderer.AddActor(model_actor)
    renderer.AddActor(axes_actor)
    win = vtk.vtkRenderWindow()
    win.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    
    interactor_style = QIN_Style()
    interactor.SetInteractorStyle(interactor_style)

    win.SetInteractor(interactor)
    win.Render()
    interactor.Start()
    pass



if __name__ == '__main__':
    if len(sys.argv)<3:
        print "Input Error: you must input 2 parameters"
        print "Para1: Source model file name, a .stl file"
        print "Para2: Output model file name, a .stl file"
        if len(sys.argv)<2:
            in_file = "E:/WorkPlace/Cpp/vtk_solutions/TMS/configFile/Model/coil__2_s_oriented.stl"
            out_file = "E:/test/newQinShuoTShapeM.stl"
        else:
            in_file = sys.argv[1]
    else:
        in_file = sys.argv[1]
        out_file = sys.argv[2]


    model = ReadSTL(in_file)
    
    Visualize_Orientation(model)

