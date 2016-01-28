'''
 Author: QIN Shuo
 Date:   2016/01/28

 How to threshold Points and Cell in poly data

'''

import vtk




points = vtk.vtkPoints()

points.InsertNextPoint(0,0,0);
points.InsertNextPoint(1,1,1);
points.InsertNextPoint(2,2,2);
points.InsertNextPoint(3,3,3);
points.InsertNextPoint(4,4,4);

index = vtk.vtkIntArray();
index.SetNumberOfComponents(1);
index.SetName("index");
index.InsertNextValue(0);
index.InsertNextValue(1);
index.InsertNextValue(2);
index.InsertNextValue(3);
index.InsertNextValue(4);


polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.GetPointData().AddArray(index)


threshold = vtk.vtkThresholdPoints()
threshold.SetInputData(polydata)

threshold.ThresholdByLower(2)
threshold.SetInputArrayToProcess(0, 0, 0, vtk.vtkDataObject.FIELD_ASSOCIATION_POINTS, "index")
threshold.Update()



polyMapper = vtk.vtkPolyDataMapper()
polyMapper.SetInputData(threshold.GetOutput())

actor = vtk.vtkActor()
actor.SetMapper(polyMapper)

renderer = vtk.vtkRenderer()
win = vtk.vtkRenderWindow()
intact = vtk.vtkRenderWindowInteractor()
style = vtk.vtkInteractorStyleTrackballCamera()

win.AddRenderer(renderer)
renderer.AddActor(actor)
intact.SetInteractorStyle(style)
intact.SetRenderWindow(win)
win.Render()
intact.Start()

