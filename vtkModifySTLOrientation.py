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

# write stl function
def WriteSTL(filename,stl):
    writer = vtk.vtkSTLWriter()
    writer.SetFileName(filename)
    writer.SetInputData(stl)
    writer.Update()




class QIN_Style(vtk.vtkInteractorStyleTrackballCamera ):
    def __init__(self,parent  = None):
        #self.RemoveObserver("KeyPressEvent")
        self.RemoveObserver(vtk.vtkCommand.KeyPressEvent)
        #self.AddObserver("KeyPressEvent",self.keyPressEvent)
        self.AddObserver(vtk.vtkCommand.KeyPressEvent,self.keyPressEvent)
        self.pos_X = 0.0
        self.pos_Y = 0.0
        self.pos_Z = 0.0   
        self.rot_X = 0.0     # rotation
        self.rot_Y = 0.0     # rotation
        self.rot_Z = 0.0     # rotation
        self.transform = vtk.vtkTransform()        


    def SetActor(self,actor):
        self.Actor = actor

    def SetRenderer(self,renderer):
        self.Renderer = renderer

    def SetPolyData(self,poly):
        self.PolyData = poly

    def SetOutName(self,name):
        self.out_name = name

    def keyPressEvent(self,obj,event):
        key = self.GetInteractor().GetKeySym()
        # translation
        if key == "i":
            self.pos_Y = self.pos_Y+5
            print ("Y: ",self.pos_Y)
        elif key == "k":
            self.pos_Y = self.pos_Y-5
            print ("Y: ",self.pos_Y)
        elif key == "j":
            self.pos_X = self.pos_X+5
            print ("X: ",self.pos_X)
        elif key == "l":
            self.pos_X = self.pos_X-5
            print ("X: ",self.pos_X)
        elif key == "u":
            self.pos_Z = self.pos_Z+5
            print ("Z: ",self.pos_Z)
        elif key == "o":
            self.pos_Z = self.pos_Z-5
            print ("Z: ",self.pos_Z)
        ### rotation
        elif key == "z":
            self.rot_X = self.rot_X+5
            print ("rotation X: ",self.rot_X)
        elif key == "s":
            self.rot_X = self.rot_X-5
            print ("rotation X: ",self.rot_X)
        elif key == "a":
            self.rot_Y = self.rot_Y+5
            print ("rotation Y: ",self.rot_Y)
        elif key == "d":
            self.rot_Y = self.rot_Y-5
            print ("rotation Y: ",self.rot_Y)
        elif key == "c":
            self.rot_Z = self.rot_Z+5
            print ("rotation Z: ",self.rot_Z)
        elif key == "x":
            self.rot_Z = self.rot_Z-5
            print ("rotation Z: ",self.rot_Z)
        elif key == "Return":
            transformFilter = vtk.vtkTransformPolyDataFilter()
            transformFilter.SetInputData(self.PolyData)
            transformFilter.SetTransform(self.transform)
            transformFilter.Update()
            
            WriteSTL(self.out_name,transformFilter.GetOutput())

        else:
            pass

        if self.rot_X > 360.0:
            self.rot_X = 0.0
        if self.rot_Z > 360.0:
            self.rot_Z = 0.0
        if self.rot_Y > 360.0:
            self.rot_Y = 0.0
        
        self.transform = vtk.vtkTransform()
        self.transform.Translate(self.pos_X,self.pos_Y,self.pos_Z)
        self.transform.RotateX(self.rot_X)
        self.transform.RotateY(self.rot_Y)
        self.transform.RotateZ(self.rot_Z)
        self.transform.Update()
        self.Actor.SetUserTransform(self.transform)

        self.GetInteractor().GetRenderWindow().Render()

        self.OnKeyPress()
        return 

    pass



# modify orientation
def vtkModifySTLOrientation( poly, ori_X,ori_Y,ori_Z, pos_X,pos_Y,pos_Z):
    transform = vtk.vtkTransform()
    transform.RotateX(ori_X)
    transform.RotateY(ori_Y)
    transform.RotateZ(ori_Z)
    transform.Translate(pos_X,pos_Y,pos_Z)
    transform.Update()

    transformFilter = vtk.vtkTransformPolyDataFilter()
    transformFilter.SetInputData(poly)
    transformFilter.SetTransform(transform)
    transformFilter.Update()

    return transformFilter.GetOutput()


# view orientation
def Visualize_Orientation(model,out_file):
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
    interactor_style.SetRenderer(renderer)
    interactor_style.SetActor(model_actor)
    interactor_style.SetPolyData(model)
    interactor_style.SetOutName(out_file)
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
            in_file = "E:/WorkPlace/Cpp/vtk_solutions/TMS/configFile/Model/coil_2_s.stl"
            out_file = "E:/test/newQinShuoTShapeM.stl"
        else:
            in_file = sys.argv[1]
            out_file = ""
    else:
        in_file = sys.argv[1]
        out_file = sys.argv[2]


    model = ReadSTL(in_file)
    
    Visualize_Orientation(model,out_file)

