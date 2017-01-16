'''
Author: QIN Shuo
Date: 2015/12/17

Description: 
    Create shadows of an object

Problems:
    vtkRenderer(valid in vtk5) && vtkOpenglRender(only solution in vtk6)


'''



import sys
import os
import vtk
import time


def AddLightActor (r):
    if (r!=0):
        print('pre: r_exits')
    
    lights = r.GetLIghts()

    lights.InitTraversal()
    
    l = lights.GetNextItem()

    while(l!=0):
        angle = l.GetConeAngle()
        if(l.LIghtTypeIsSceneLight() and l.GetPositional() and angle<180. ):
            la = vtk.vtkLightActor()
            la.SetLight(l)
            r.AddViewProp(la)
            la.Delete

        l = lights .GetNextItem()




interactor = vtk.vtkRenderWindowInteractor()
renderWindow = vtk.vtkRenderWindow()

renderWindow.SetSize(400,400)
renderWindow   .SetMultiSamples(0)
renderWindow.SetAlphaBitPlanes(1)
interactor.SetRenderWindow(renderWindow)

renderer = vtk.vtkRenderer()

renderWindow.AddRenderer(renderer)

supported = vtk.vtkFrameBufferObject.IsSupported(renderWindow)

if (not supported):
    print "returning"
    time.sleep(5)


cameraP = vtk.vtkCameraPass()
opaque = vtk.vtkOpaquePass()

peeling = vtk.vtkDepthPeelingPass()
peeling.SetMaximumNumberOfPeels(200)
peeling.SetOcclusionRatio(0.1)


translucent = vtk.vtkTranslucentPass()
peeling.SetTranslucentPass(translucent)


volume = vtk.vtkVolumetricPass()
overlay = vtk.vtkOverlayPass()
lights = vtk.vtkLightsPass()
opaqueSequence = vtk.vtkSequencePass()
pass2 = vtk.vtkRenderPassCollection()

pass2.AddItem(lights)
pass2.AddItem(opaque)
opaqueSequence.SetPasses(pass2)

opaqueCameraPass = vtk.vtkCameraPass()
opaqueCameraPass.SetDelegatePass(opaqueSequence)

shadowBaker = vtk.vtkShadowMapBakerPass()
shadowBaker.SetOpaquePass(opaqueCameraPass)
shadowBaker.SetResolution(1024)
# to cancel self->shadowing
shadowBaker.SetPolygonOffsetFactor(3.1)
shadowBaker.SetPolygonOffsetUnits(10.0)

shadows = vtk.vtkShadowMapPass()
shadows.SetShadowMapBakerPass(shadowBaker)
shadows.SetOpaquePass(opaqueSequence)

seq = vtk.vtkSequencePass()
passes = vtk.vtkRenderPassCollection()
passes.AddItem(shadowBaker)
passes.AddItem(shadows)
passes.AddItem(lights)
passes.AddItem(peeling)
passes.AddItem(volume)
passes.AddItem(overlay)
seq.SetPasses(passes)
cameraP.SetDelegatePass(seq)

renderer.SetPass(cameraP)

rectangleSource = vtk.vtkPlaneSource()
rectangleSource.SetOrigin(-5.0,0.0,5.0)
rectangleSource.SetPoint1(5.0,0.0,5.0)
rectangleSource.SetPoint2(-5.0,0.0,-5.0)
rectangleSource.SetResolution(100,100)

rectMapper = vtk.vtkPolyDataMapper()
rectMapper.SetInputData(rectangleSource.GetOutput())
rectMapper.SetScalarVisibility(0)

rectActor = vtk.vtkActor()
rectKeyProperty = vtk.vtkInformation()
rectKeyProperty.Set(vtk.vtkShadowMapBakerPass.OCCLUDER(),0)
rectKeyProperty.Set(vtk.vtkShadowMapBakerPass.RECEIVER(),0)
rectActor.SetPropertyKeys(rectKeyProperty)

rectActor.SetMapper(rectMapper)
rectActor.SetVisibility(1);
rectActor.GetProperty().SetColor(1,1,1);

boxSource = vtk.vtkCubeSource()
boxSource.SetXLength(2)

boxNormals = vtk.vtkPolyDataNormals()
boxNormals.SetInputData(boxSource.GetOutput())
boxNormals.SetComputePointNormals(0)
boxNormals.SetComputeCellNormals(0)
boxNormals.Update();
boxNormals.GetOutput().GetPointData().SetNormals(boxNormals)

boxMapper = vtk.vtkPolyDataMapper()
boxMapper.SetInputData(boxNormals.GetOutput())
boxMapper.SetScalarVisibility(0)

boxActor = vtk.vtkActor()
boxKeyProperty = vtk.vtkInformation()
boxKeyProperty.Set(vtk.vtkShadowMapBakerPass.OCCLUDER(),0)
boxKeyProperty.Set(vtk.vtkShadowMapBakerPass.RECEIVER(),0)
boxActor.SetPropertyKeys(boxKeyProperty)

boxActor.SetMapper(boxMapper)
boxActor.SetVisibility(1)
boxActor.SetPosition(-2.0,2.0,0.0)
boxActor.GetProperty().SetColor(1.0,0.0,0.0)

coneSource = vtk.vtkConeSource()
coneSource.SetResolution(24)
coneSource.SetDirection(1.0,1.0,1.0)
coneMapper = vtk.vtkMapper()
coneMapper.SetInputData(coneSource.GetOutput())
coneMapper.SetScalarVisibility(0)

coneActor = vtk.vtkActor()
coneKeyProperty = vtk.vtkInformation()
coneKeyProperty.Set(vtk.vtkShadowMapBakerPass.OCCLUDER(),0)
coneKeyProperty.Set(vtk.vtkShadowMapBakerPass.RECEIVER(),0)
coneActor.SetPropertyKeys(coneKeyProperty)

coneActor.SetMapper(coneMapper)
coneActor.SetVisibility(1)
coneActor.SetPosition(0.0,1.0,1.0)
coneActor.GetProperty().SetColor(0,0,1);

sphereSource = vtk.vtkSphereSource()
sphereSource.SetThetaResolution(32)
sphereSource.SetPhiResolution(32)
sphereMapper = vtk.vtkMapper()
sphereMapper.SetInputData(sphereSource.GetOutput())
sphereMapper.SetScalarVisibility(0)

sphereActor = vtk.vtkActor()
sphereKeyProperty = vtk.vtkInformation()
sphereKeyProperty.Set(vtk.vtkShadowMapBakerPass.OCCLUDER(),0)
sphereKeyProperty.Set(vtk.vtkShadowMapBakerPass.RECEIVER(),0)
sphereActor.SetPropertyKeys(sphereKeyProperty)
sphereActor.SetMapper(sphereMapper)

sphereActor.SetVisibility(1)
sphereActor.SetPosition(2,2,-1)
sphereActor.GetProperty().SetColor(1,1,0)

renderer.AddViewPro(rectActor)
renderer.AddViewPro(boxActor)
renderer.AddViewPro(coneActor)
renderer.AddViewPro(sphereActor)

l1 = vtk.vtkLight()
l1.SetPosition(-4,4,-1)
l1.SetFocalPOint(boxActor.GetPosition())
l1.SetColor(1,1,1)
l1.SetPositional(1)
renderer.AddLight(l1)
l1.SetSwitch(1)

l2 = vtk.vtkLight()
l2.SetPosition(-4,5,1)
l2.SetFocalPOint(sphereActor.GetPosition())
l2.SetColor(1,0,1)
l2.SetPositional(1)
renderer.AddLight(l2)
l2.SetSwitch(1)


AddLightActor(renderer)

renderer.SetBackground(0.66,0.66,0.66)
renderer.SetBackground2(157.0/255.0*0.66,186/255.0*0.66,192.0/255.0*0.66)
renderer.SetGradientBackground(True)
renderer.Render()

if  peeling.GetLastRenderingUsedDepthPeeling():
    print "depth peeling was used"
else:
    print "depth peeling was not used"

renderer.ResetCamera()
camera = vtk.vtkCamera()
camera = renderer.GetActiveCamera()
camera.Azimuth(40)
camera.Elevation(10)

renderWindow.Render()
interactor.Start()





