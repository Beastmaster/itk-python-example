'''
Author: Qin Shuo
Date:   2016/03/22
Description:
    Not complete

    To be continued...
'''



import vtk
import sys
import string



file_name = 'C:/Users/QIN Shuo/Desktop/MRIcron/templates/aal.nii'







# visualization
print "visualizing..."
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(discreteCubes.GetOutput())
mapper.ScalarVisibilityOn()
mapper.SetScalarRange(0,4)
mapper.SetLookupTable(lut)
actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)
interactor = vtk.vtkRenderWindowInteractor()
window.SetInteractor(interactor)

window.Render()
interactor.Start()




'''
if __name__ == '__main__':
    file_name = sys.argv[1]
    MarchingCube(file_name)
'''