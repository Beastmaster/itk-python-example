'''
MarchingCubes

Add ball

mouse click 

'''

import vtk
import sys

def MarchingCube(file_name):

    coor1 = [ 128.463,208.477,51.7136]
    coor2 = [53.9797,208.47,53.3523]
    coor3 = [96.6807,121.699,168.477]
    coor4 = [4.55786,84.7877,51.6438]

    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(file_name)
    reader.Update()

    image = reader.GetOutput()

    surface = vtk.vtkMarchingCubes()
    surface.SetInputData(image)
    surface.SetValue(0,50)
    surface.Update()

    skin = surface.GetOutput()

    polyMapper = vtk.vtkPolyDataMapper()
    polyMapper.ScalarVisibilityOff()
    polyMapper.SetInputData(skin)

    actor = vtk.vtkActor()
    actor.SetMapper(polyMapper)
    actor.GetProperty().SetColor(0.8,0.9,0.9)


    # return vtkactor
    def CreateBall(coor):
        ball = vtk.vtkSphereSource()
        ball.SetCenter(0,0,0)
        ball.SetRadius(6.0)
        ball.SetThetaResolution(100)
        ball.Update()
        map = vtk.vtkPolyDataMapper()
        map.SetInputData(ball.GetOutput())
        actorx = vtk.vtkActor()
        actorx.SetMapper(map)
        actorx.GetProperty().SetColor(1,0,0)
        actorx.SetPosition(coor[0],coor[1],coor[2])
        return actorx

    ball1 = CreateBall(coor1)
    ball2 = CreateBall(coor2)
    ball3 = CreateBall(coor3)
    ball4 = CreateBall(coor4)

    win = vtk.vtkRenderWindow()
    renderer = vtk.vtkRenderer()
    intact = vtk.vtkRenderWindowInteractor()
    style = vtk.vtkInteractorStyleTrackballCamera()

    win.AddRenderer(renderer)
    renderer.AddActor(actor)
    #renderer.AddActor(ball1)
    #renderer.AddActor(ball2)
    #renderer.AddActor(ball3)
    renderer.AddActor(ball4)
    intact.SetInteractorStyle(style)
    intact.SetRenderWindow(win)

    
    win.Render()
    intact.Start()


if __name__ == '__main__':
    file_name = sys.argv[1]
    MarchingCube(file_name)


