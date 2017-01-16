'''
Author: Qin Shuo
Date:   2016/03/22
Description:
    This file demo some vtk Readers 

Support format:
1. .msh
2. .stl

Format of .msh file
|==============================|
ObjectType = Scene
NDims = 3
NObjects = 1
ObjectType = Mesh
NDims = 3
BinaryData = False
TransformMatrix = 1 0 0 0 1 0 0 0 1
Offset = 0 0 0
CenterOfRotation = 0 0 0
ElementSpacing = 1 1 1
PointType = MET_FLOAT
PointDataType = MET_DOUBLE
CellDataType = MET_DOUBLE
NCellTypes = 1
PointDim = ID x y ...
NPoints = 1127
Points = 
0 234.284 -0.390708 5 
1 232.807 -0.651181 5 
2 234.386 -0.769545 5 
        ...
CellType = TRI
NCells = 2334
Cells = 
0 0 1 2 
1 2 1 3 
2 2 3 4 
        ...
EOF
|==============================|
'''


import vtk
from QuickView import visualize_poly

def Read_mesh(file_name):
    # read mesh file
    # suffix: .msh
    # msh file format:
	# read file head

    points = vtk.vtkPoints()
    polys = vtk.vtkCellArray()

    file = open(file_name,'r')
    while True: 
        line = file.readline()
        if not line:
            break
        if line.find('Points')>=0:
            num_Points = int(line.split()[2])
            print 'Number of points is {}'.format(num_Points)
            # put in to vtkPoints
            print 'Writing Points'
            points.SetNumberOfPoints(num_Points)
            file.readline()
            for i in range(0,num_Points):
                line = file.readline()
                if not line:
                    break
                idx = line.split( )
                x = float(idx[1])
                y = float(idx[2])
                z = float(idx[3])
                points.SetPoint(i,x,y,z)

        if line.find('NCells')>=0:
            num_Triangles = int(line.split()[2])
            print 'Number of Triangles is {}'.format(num_Triangles)
            # create cells
            print 'Writing Cells'
            file.readline()
            for i in range(0,num_Triangles):
                line = file.readline()
                if not line:
                    break
                idx = line.split( )
                a = int(idx[1])
                b = int(idx[2])
                c = int(idx[3])
                polys.InsertNextCell(3)
                polys.InsertCellPoint(a)
                polys.InsertCellPoint(b)
                polys.InsertCellPoint(c)

	
	polyData = vtk.vtkPolyData()
	polyData.SetPoints(points)
	polyData.SetPolys(polys)
    return polyData
	

def read_stl(filename):
    #vtk STL data reader
    # suffix: .stl
    reader = vtk.vtkSTLReader()
    reader.SetFileName(filename)
    reader.Update()
    return reader.GetOutput()




if __name__ == '__main__':
    
    poly = Read_mesh('C:/Users/qinsh/OneDrive/Project/Navigation/navigation_backup/DATA/TrackerToolRepresentationMeshes/sProbe.msh')
    visualize_poly(poly)

