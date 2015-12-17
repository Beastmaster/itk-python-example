

__author__ = 'Qin Shuo'

import vtk
import string

class PyMeshReader(object):
    def __init__(self):
        print('PyMeshReader constructed')
        self.polyData = vtk.vtkPolyData()
        self.Property = {}
        pass

    def ReadFile(self,filename):
        self.filename = filename
        if  self.filename == '':
            print('file name is null')
            return
        print('reading file ', filename)
        self.Points = vtk.vtkPoints()
        self.Cells  = vtk.vtkCellArray()

        #begin to read plain text file
        fp = open(self.filename,'r+')

        #iterate through lines in file
        line = fp.readline()
        while line != '':
            #split string
            line = line.strip('\n')
            lis = line.split('=')
            #condition1: points
            if lis[0].strip() == 'Points':
                #set number of points
                self.NPoints = int(self.Property['NPoints'])
                self.Points.SetNumberOfPoints(self.NPoints)
                #read points data
                for cnt in range(1,self.NPoints+1):
                    #exclude space and new line
                    point_list = fp.readline().strip()
                    #split array
                    point_list = point_list.split(' ')
                    #add data to points
                    self.Points.SetPoint(int(point_list[0]),float(point_list[1]),float(point_list[2]),float(point_list[3]))

            #condition2: cells
            elif lis[0].strip() == 'Cells':
                self.NCells = int(self.Property['NCells'])
                for cnt in range(1,self.NCells+1):
                    #exclude space and new line
                    cell_list = fp.readline().strip()
                    #split list
                    cell_list = cell_list.split(' ')
                    #add data to cells
                    self.Cells.InsertNextCell(3)
                    self.Cells.InsertCellPoint(int(cell_list[1]))
                    self.Cells.InsertCellPoint(int(cell_list[2]))
                    self.Cells.InsertCellPoint(int(cell_list[3]))

            #condition3: properties
            else:
                self.Property[lis[0].strip()] = lis[1].strip()

            #read next line and back into the loolp
            line = fp.readline()


        fp.close()    #close file
        print('reading done ...')
        #construct poly data
        self.polyData.SetPoints(self.Points)
        self.polyData.SetPolys(self.Cells)

    def GetObject(self):
        print('Get mesh object')
        return self.polyData

