
'''
 Author: QIN Shuo
 Date:   2015/11/10
 This is a example file for vtk

Description:
    This file demonstrate how to define a user event
    Different from the one that pre-defined in VTK
     like: MouseEvent, KeyPressEvent

Details:
    implement a new filter, use InvokeEvent() to trigger
    InvokeEvent base class: vtkObject
    user-event ID recommend to be vtkCommand::UserEvent + 1xx


Reference: vtk-example/Interaction/UserEvent
'''


import vtk


# inhert from vtkObject
class MyClass(vtk.vtkObject):
    def __init__(self):
        # this line is important: define event ID
        print "inited"
        self.MyEvent = vtk.vtkCommand.UserEvent+1

    def trigger(self):
        print "triggered"
        self.InvokeEvent(self.MyEvent)
        print self.MyEvent


def callbackFunc(caller,eventID,clientData,callData):
    print("call back called")

def callbackFunc2(obj,event):
    print("call back 2 called")

def KeyPressEvent(obj,event):
    print("key pressed")
    global test
    test.trigger()
    #obj.InvokeEvent(test.MyEvent)

renderer = vtk.vtkRenderer()
renderWin = vtk.vtkRenderWindow()
interactor = vtk.vtkRenderWindowInteractor()

renderWin.AddRenderer(renderer)
interactor.SetRenderWindow(renderWin)

test = MyClass()
test.AddObserver(test.MyEvent,callbackFunc2)
# this step is important: create a callback command instance
#interactor.AddObserver(test.MyEvent,callbackFunc2)
interactor.AddObserver("KeyPressEvent",KeyPressEvent)


renderWin.Render()
interactor.Start()
























































