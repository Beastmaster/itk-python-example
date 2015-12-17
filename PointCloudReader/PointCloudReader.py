#file name: PointCloudReader.py
#Function: Read point cloud from plain text file.

__author__ = 'Qin Shuo'

import vtk
import sys

def ReadSimplePoint(filename):
    print 'Reading file: ', filename
    #read file
    reader = vtk.vtkSimplePointsReader()
    reader.SetFilename(filename)
    reader.Update()

    #visualize
    PolyVisualize(reader.GetOutputPort())


def ReadPointCloud(filename):
    print 'Reading file: ', filename
    #vtkPoints here:
    #method1: assign number of points, insert points by ID, ::SetPoint(ID, double[3])
    #method2: assign no size, insert one after anther,      ::InsertNextPoint(double[3])
    points = vtk.vtkPoints()
    poly   = vtk.vtkPolyData()
    glyphFilter = vtk.vtkVertexGlyphFilter()  # I don't know what is the purpose

    fp = open(filename,"rb+")
    line = fp.readline()
    while line!='':
        line = line.strip()
        if line == '':
            continue
        elif line.find('\t') < 0:
            line = line.split(' ')
        else:
            line = line.split('\t')

        points.InsertNextPoint(float(line[0]),float(line[1]),float(line[2]))
        #read next line and return to loop
        line = fp.readline()

    #add point to poly data
    poly.SetPoints(points)
    glyphFilter.SetInputData(poly)
    glyphFilter.Update()

    #visualize
    PolyVisualize(glyphFilter.GetOutputPort())


def PolyVisualize(inputConnection):
    print('visualizing...')
    PolyMapper = vtk.vtkPolyDataMapper()
    PolyMapper.SetInputConnection(inputConnection)

    actor = vtk.vtkActor()
    actor.SetMapper(PolyMapper)

    renderer = vtk.vtkRenderer()
    renderWin = vtk.vtkRenderWindow()
    interactor = vtk.vtkRenderWindowInteractor()

    renderWin.AddRenderer(renderer)
    interactor.SetRenderWindow(renderWin)

    renderer.AddActor(actor)
    renderer.SetBackground(0,0,0)
    renderWin.Render()
    interactor.Start()


if  __name__ == "__main__":
    ReadPointCloud(sys.argv[1])