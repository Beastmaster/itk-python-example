'''
Author: QIN Shuo
Date: 2016/2/26

Description:
	Read from a plain text of pionts and triangles
	And construct a poly data 
	And save to .stl file
	
	In this example: .msh file
'''



import sys
import vtk


def ConvertMSH(file_name):
	out_name = file_name.split('.')[0]+'.stl'
	print 'Out file:'+out_name
	# read file head
	file = open(file_name,'r')
	line = file.readline().split('=')
	while(line[0].strip() != 'Points'):
		line = file.readline().split('=')
		print 'Processing ', line[0]
		if(line[0].strip() == 'NPoints'):
			num_Points = int(line[1].strip())
			print 'Number of Points is ' + str(num_Points)
			
	# put in to vtkPoints
	print 'Writing Points'
	points = vtk.vtkPoints()
	points.SetNumberOfPoints(num_Points)
	for i in range(0,num_Points):
		line = file.readline()
		nums = line.split( )
		x = float(nums[1])
		y = float(nums[2])
		z = float(nums[3])
		points.SetPoint(i,x,y,z)

	# create cells
	print 'Writing Cells'
	line = file.readline().split('=')
	while(line[0].strip() != 'Cells'):
		line = file.readline().split('=')
		print 'Processing ', line[0]
		if(line[0].strip() == 'NCells'):
			num_Triangles = int(line[1].strip())
			print 'Number of num_Triangles: '+str(num_Triangles)
		
	polys = vtk.vtkCellArray()
	for i in range(1,num_Triangles):
		line = file.readline()
		nums = line.split( )
		a = int(nums[1])
		b = int(nums[2])
		c = int(nums[3])
		polys.InsertNextCell(3)
		polys.InsertCellPoint(a)
		polys.InsertCellPoint(b)
		polys.InsertCellPoint(c)
	
	polyData = vtk.vtkPolyData()
	polyData.SetPoints(points)
	polyData.SetPolys(polys)
	
	print 'Writing to STL file'
	writer = vtk.vtkSTLWriter()
	writer.SetFileName(out_name)
	writer.SetInputData(polyData)
	writer.Update()
	

if __name__ == '__main__':
	try:
		name= sys.argv[1]
	except ValueError:
		print "Input error"
		exit()

	ConvertMSH(name)

