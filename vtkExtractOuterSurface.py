
'''
Author:
    pass QIN Shuo
Date:
    pass 2016/5/30
Description:
    Extract outer layer of surface
    Using marchingcube
    shift original image to binary image first

'''



import vtk
import sys


def vtkExtractOuterSurface(filename):

    reader = vtk.vtkNIFTIImageReader()
    reader.SetFileName(filename)
    reader.Update()
    image1 = reader.GetOutput()
    
    dim = image1.GetDimensions()
    print dim

    for x in [0,dim[0]-1]:
        for y in [0,dim[1]-1]:
            image1.SetScalarComponentFromFloat(x,y,dim[2]-1,0,0.0)
            image1.SetScalarComponentFromFloat(x,y,dim[2]-2,0,0.0)
            image1.SetScalarComponentFromFloat(x,y,dim[2]-3,0,0.0)
            image1.SetScalarComponentFromFloat(x,y,dim[2]-4,0,0.0)
            image1.SetScalarComponentFromFloat(x,y,0,0,0.0)
            image1.SetScalarComponentFromFloat(x,y,1,0,0.0)
            image1.SetScalarComponentFromFloat(x,y,2,0,0.0)
            image1.SetScalarComponentFromFloat(x,y,3,0,0.0)
            

    for y in [0,dim[1]-1]:
        for z in [0,dim[2]-1]:
            image1.SetScalarComponentFromFloat(dim[0]-1,y,z,0,0.0)
            image1.SetScalarComponentFromFloat(dim[0]-2,y,z,0,0.0)
            image1.SetScalarComponentFromFloat(dim[0]-3,y,z,0,0.0)
            image1.SetScalarComponentFromFloat(dim[0]-4,y,z,0,0.0)
            image1.SetScalarComponentFromFloat(dim[0]-5,y,z,0,0.0)
            image1.SetScalarComponentFromFloat(0,y,z,0,0.0)
            image1.SetScalarComponentFromFloat(1,y,z,0,0.0)
            image1.SetScalarComponentFromFloat(2,y,z,0,0.0)
            image1.SetScalarComponentFromFloat(3,y,z,0,0.0)


    for x in [0,dim[0]-1]:
        for z in [0,dim[2]-1]:
            image1.SetScalarComponentFromFloat(x,0,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,1,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,2,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,3,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,4,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,5,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,dim[1]-1,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,dim[1]-2,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,dim[1]-3,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,dim[1]-4,z,0,0.0)
            image1.SetScalarComponentFromFloat(x,dim[1]-5,z,0,0.0)

    # threshold
    threshold = vtk.vtkImageThreshold()
    threshold.SetInputData(image1)
    threshold.ThresholdBetween(15,1000)
    threshold.ReplaceInOn()
    threshold.SetInValue(200)
    threshold.ReplaceOutOn()
    threshold.SetOutValue(0)
    threshold.Update()
    image = threshold.GetOutput()
    



    #write to image
    writer = vtk.vtkNIFTIImageWriter()
    writer.SetFileName("C:/Users/QIN Shuo/Desktop/test.nii")
    writer.SetInputData(image)
    writer.Update()

    #marching here
    marching = vtk.vtkMarchingCubes()
    marching.SetInputData(image)
    marching.SetValue(0,8)
    marching.Update()
    skin = marching.GetOutput()

    connector = vtk.vtkConnectivityFilter()
    connector.SetInputData(skin)
    connector.SetExtractionModeToLargestRegion()
    connector.Update()
    
    geo = vtk.vtkGeometryFilter()
    geo.SetInputData(connector.GetOutput())
    geo.Update()
    area = geo.GetOutput()


    ## fill holes
    #filler = vtk.vtkFillHolesFilter()
    #filler.SetInputData(area)
    #filler.SetHoleSize(1E6)
    #filler.Update()
    #area = filler.GetOutput()

    #filter = vtk.vtkPolyDataConnectivityFilter()
    #filter.SetInputData(area)
    #filter.SetExtractionModeToSpecifiedRegions()
    #filter.AddSpecifiedRegion(0)
    #filter.Update()
    #area = filter.GetOutput()


    # visualization
    print "visualizing..."
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputData(area)
    #mapper.ScalarVisibilityOn()
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    #actor.GetProperty().SetOpacity(0.7)

    renderer = vtk.vtkRenderer()
    renderer.AddActor(actor)
    window = vtk.vtkRenderWindow()
    window.AddRenderer(renderer)
    interactor = vtk.vtkRenderWindowInteractor()
    window.SetInteractor(interactor)
    
    window.Render()
    interactor.Start()


if __name__ == '__main__':
    #file_name = sys.argv[1]
    file_name = "C:/Users/QIN Shuo/Desktop/TMS_nav/configFile/Atlas/reference_brain_res.nii"
    vtkExtractOuterSurface(file_name)

