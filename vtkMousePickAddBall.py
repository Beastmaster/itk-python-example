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

# Input:
#   view: a possible vtk object
#   text: a string to be add to view
def vtkAddText(view, text):
    pass

# Input:
#   view: a possible vtk object
#   filename: a string, filename
def vtkSavePicture(view,filename):
    pass

# Input: a vtkSTL object
def vtkMousePickAddBall(model):
    print "Put the mouse to desired position and press \"h\" to add a ball"
    print "Press \"s\" to save the scene as a picture"




    pass






if __name__ == '__main__':
    if len(sys.argv)<2:
        print "Please Specify input and output file"
        file_name = "E:/test/coil__2_s.stl"
    else:
        file_name = sys.argv[1]
    
    vtkMousePickAddBall(file_name)
