'''
Author: QIN Shuo
Date: 2015/12/18
Description:
    This file demonstrate how to manipulate position/size/direction
    of a image.

Matrix Operation:
    1. create a matrix
    2. Matrix initialization
    3. Change matrix elements value
    4. Get element value

'''



import vtk

# create a matrix instance
matrix = vtk.vtkMatrix4x4()


value = [1,2,3,4]

# initialization
matrix.DeepCopy((1,2,3,4,
                 5,6,7,8,
                 9,10,11,12,
                 0,0,0,1))




# change element value
index_x = 0 #
index_y = 0 #
v = 100
matrix.SetElement(index_x,index_y,v)


# Get element value
new_value = matrix.GetElement(index_x,index_y)
print(new_value)
