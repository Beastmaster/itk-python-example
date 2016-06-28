'''
Author: QIN Shuo
Date: 2016/6/24
Organization: RC-MIC (CUHK)

Description:
    Mouse pick a position
    Press a key to get the position information
    Add a ball in the selected position

'''




import vtk
import sys



# Input: a vtkSTL object
class vtkMousePickAddBall():
    def __init__(self,model):
        print "Put the mouse to desired position and press \"h\" to add a ball"
        print "Press \"s\" to save the scene as a picture"

        self.renderer = vtk.vtkRenderer()
        self.renWin = vtk.vtkRenderWindow()
        self.interactor = vtk.vtkRenderWindowInteractor()


        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(model)
        self.modelActor = vtk.vtkActor()
        self.modelActor.SetMapper(mapper)
        self.modelActor.GetProperty().SetColor(1,0,0)

        ball = vtk.vtkSphereSource()
        ball.SetCenter(0.0,0.0,0.0)
        ball.SetRadius(5.0)
        ball.Update()
        ballMapper = vtk.vtkPolyDataMapper()
        ballMapper.SetInputData(ball.GetOutput())
        self.ballActor = vtk.vtkActor()
        self.ballActor.SetMapper(ballMapper)

        self.renderer.AddActor(self.ballActor)
        self.renderer.AddActor(self.modelActor)

        self.renWin.AddRenderer(self.renderer)
        self.interactor.SetRenderWindow(renWin)

        pass


    def registerCallbacks(self,obj,event):
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
            transform = vtk.vtkTransform()
            transform.Translate(picked)
            self.ballActor.SetUserTransform(transform)

            # add text
            text = str(coor)
            self.vtkAddText(text)
            self.renWin.Render()
        elif key=="s":
            self.vtkSavePicture("aaa.png")
            
        else:
            pass 
        
        pass


    # Input:
    #   text: a string to be add to view
    def vtkAddText(self, text):
        self.txtActor = vtk.vtkTextActor()
        self.txtActor.SetInput(text)
        self.txtActor.SetPosition2(10,40);
        self.txtActor.GetTextProperty().SetFontSize ( 24 );  
        self.txtActor.GetTextProperty().SetColor ( 1.0, 0.0, 0.0 );
        self.renderer.AddActor(self.txtActor)
        self.renWin.Render()
        pass

    # Input:
    #   filename: a string, filename
    def vtkSavePicture(self,filename):
        renderWindow = self.renWin
        shot = vtk.vtkWindowToImageFilter()
        shot.SetInputData(renderWindow)
        shot.SetMagnification(3)
        shot.SetInputBufferTypeToRGBA()
        shot.ReadFrontBufferOff()
        shot.Update()

        # write
        writer = vtk.vtkPNGWriter()
        writer.SetFileName(filename)
        writer.SetInputData(shot.GetOutput())
        writer.Update()
        pass

pass






if __name__ == '__main__':
    if len(sys.argv)<2:
        print "Please Specify input and output file"
        file_name = "E:/test/coil__2_s.stl"
    else:
        file_name = sys.argv[1]
    
    reader = vtk.vtkSTLReader()
    reader.SetFileName(file_name)
    reader.Update()

    vtkMousePickAddBall(reader.GetOutput())
