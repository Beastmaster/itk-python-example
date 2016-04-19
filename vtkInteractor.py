'''
Author:
    pass QIN Shuo
Date:
    pass 2015/12/18
Description:
    pass
This file demonstrate how to interact in vtk

This file will employ 2 method (actually 2 similar
mthod to achieve the goal):
    pass
1. Re-load vtkInteractorStyleImage, add observer
 to this class.
2. Define callback function and add observer to
 vtk window interactor.

EventID are defined in vtkCommand class



Tips:
    pass

 class MyStyle(vtk.vtkInteractorStyleImage):
    pass
def __init__(self):
    pass
    pass
def OnMouseWheelForward(self):
    pass
    pass

 the above method will not re-load the mouse wheel function
 the real functional method are applied by adding event observer


 Note:
    There is no vtkCallbackCommand in python
'''





import vtk


# define a interactor style that re-implement all event callback


'''
inhert class format

class new_style(vtk.vtkInteractorStyleImage):
    def __init__(self):
        self.AddObserver("NoEvent",self.e_new_NoEvent) # "OnEvent" is the name of vtkCommand   ;"new_NoEvent" is user defined name, and should be implemented in the class
                                                     # function name must different from that defined in vtkInteractorStyle
                                                     # vtkCommand class, command ID defined by vtk default
    def new_NoEvent(self,obj,event):
        obj.GetSomething # get objects function

        self.e_GetInteractor().GetXXX()  # functions found in vtkInteractorStyleUser class (refer to GetKeySym example)

        self.e_OnNoEvent()  # this line is important, and the function is listed in vtkInteractorStyle class
        return              # "return " is also badly needed
'''

class QIN_Style(vtk.vtkInteractorStyleImage):
    def __init__(self):
        self.AddObserver("NoEvent",self.e_NoEvent)
        self.AddObserver("AnyEvent",self.e_AnyEvent)
        self.AddObserver("DeleteEvent",self.e_DeleteEvent)
        self.AddObserver("StartEvent",self.e_StartEvent)
        self.AddObserver("EndEvent",self.e_EndEvent)
        self.AddObserver("RenderEvent",self.e_RenderEvent)
        self.AddObserver("ProgressEvent",self.e_ProgressEvent)
        self.AddObserver("PickEvent",self.e_PickEvent)
        self.AddObserver("StartPickEvent",self.e_StartPickEvent)
        self.AddObserver("EndPickEvent",self.e_EndPickEvent)
        self.AddObserver("AbortCheckEvent",self.e_AbortCheckEvent)
        self.AddObserver("ExitEvent",self.e_ExitEvent)
        self.AddObserver("LeftButtonPressEvent",self.e_LeftButtonPressEvent)
        self.AddObserver("LeftButtonReleaseEvent",self.e_LeftButtonReleaseEvent)
        self.AddObserver("MiddleButtonPressEvent",self.e_MiddleButtonPressEvent)
        self.AddObserver("MiddleButtonReleaseEvent",self.e_MiddleButtonReleaseEvent)
        self.AddObserver("RightButtonPressEvent",self.e_RightButtonPressEvent)
        self.AddObserver("RightButtonReleaseEvent",self.e_RightButtonReleaseEvent)
        self.AddObserver("EnterEvent",self.e_EnterEvent)
        self.AddObserver("LeaveEvent",self.e_LeaveEvent)
        self.AddObserver("KeyPressEvent",self.e_KeyPressEvent)
        self.AddObserver("KeyReleaseEvent",self.e_KeyReleaseEvent)
        self.AddObserver("CharEvent",self.e_CharEvent)
        self.AddObserver("ExposeEvent",self.e_ExposeEvent)
        self.AddObserver("ConfigureEvent",self.e_ConfigureEvent)
        self.AddObserver("TimerEvent",self.e_TimerEvent)
        self.AddObserver("MouseMoveEvent",self.e_MouseMoveEvent)
        self.AddObserver("MouseWheelForwardEvent",self.e_MouseWheelForwardEvent)
        self.AddObserver("MouseWheelBackwardEvent",self.e_MouseWheelBackwardEvent)
        self.AddObserver("ResetCameraEvent",self.e_ResetCameraEvent)
        self.AddObserver("ResetCameraClippingRangeEvent",self.e_ResetCameraClippingRangeEvent)
        self.AddObserver("ModifiedEvent",self.e_ModifiedEvent)
        self.AddObserver("WindowLevelEvent",self.e_WindowLevelEvent)
        self.AddObserver("StartWindowLevelEvent",self.e_StartWindowLevelEvent)
        self.AddObserver("EndWindowLevelEvent",self.e_EndWindowLevelEvent)
        self.AddObserver("ResetWindowLevelEvent",self.e_ResetWindowLevelEvent)
        self.AddObserver("SetOutputEvent",self.e_SetOutputEvent)
        self.AddObserver("ErrorEvent",self.e_ErrorEvent)
        self.AddObserver("WarningEvent",self.e_WarningEvent)
        self.AddObserver("StartInteractionEvent",self.e_StartInteractionEvent)
        self.AddObserver("InteractionEvent",self.e_InteractionEvent)
        self.AddObserver("EndInteractionEvent",self.e_EndInteractionEvent)
        self.AddObserver("EnableEvent",self.e_EnableEvent)
        self.AddObserver("DisableEvent",self.e_DisableEvent)
        self.AddObserver("CreateTimerEvent",self.e_CreateTimerEvent)
        self.AddObserver("DestroyTimerEvent",self.e_DestroyTimerEvent)
        self.AddObserver("PlacePointEvent",self.e_PlacePointEvent)
        self.AddObserver("PlaceWidgetEvent",self.e_PlaceWidgetEvent)
        self.AddObserver("CursorChangedEvent",self.e_CursorChangedEvent)
        self.AddObserver("ExecuteInformationEvent",self.e_ExecuteInformationEvent)
        self.AddObserver("RenderWindowMessageEvent",self.e_RenderWindowMessageEvent)
        self.AddObserver("WrongTagEvent",self.e_WrongTagEvent)
        self.AddObserver("StartAnimationCueEvent",self.e_StartAnimationCueEvent)
        self.AddObserver("AnimationCueTickEvent",self.e_AnimationCueTickEvent)
        self.AddObserver("EndAnimationCueEvent",self.e_EndAnimationCueEvent)
        self.AddObserver("VolumeMapperRenderProgressEvent",self.e_VolumeMapperRenderProgressEvent)
        self.AddObserver("VolumeMapperComputeGradientsEndEvent",self.e_VolumeMapperComputeGradientsEndEvent)
        self.AddObserver("VolumeMapperComputeGradientsProgressEvent",self.e_VolumeMapperComputeGradientsProgressEvent)
        self.AddObserver("VolumeMapperComputeGradientsStartEvent",self.e_VolumeMapperComputeGradientsStartEvent)
        self.AddObserver("WidgetModifiedEvent",self.e_WidgetModifiedEvent)
        self.AddObserver("WidgetValueChangedEvent",self.e_WidgetValueChangedEvent)
        self.AddObserver("WidgetActivateEvent",self.e_WidgetActivateEvent)
        self.AddObserver("UserEvent",self.e_UserEvent)

    def e_NoEvent(self,obj,event):
        pass
    def e_AnyEvent(self,obj,event):
        pass
    def e_DeleteEvent(self,obj,event):
        pass
    def e_StartEvent(self,obj,event):
        pass
    def e_EndEvent(self,obj,event):
        pass
    def e_RenderEvent(self,obj,event):
        pass
    def e_ProgressEvent(self,obj,event):
        pass
    def e_PickEvent(self,obj,event):
        pass
    def e_StartPickEvent(self,obj,event):
        pass
    def e_EndPickEvent(self,obj,event):
        pass
    def e_AbortCheckEvent(self,obj,event):
        pass
    def e_ExitEvent(self,obj,event):
        pass
    def e_LeftButtonPressEvent(self,obj,event):
        pass
    def e_LeftButtonReleaseEvent(self,obj,event):
        pass
    def e_MiddleButtonPressEvent(self,obj,event):
        pass
    def e_MiddleButtonReleaseEvent(self,obj,event):
        pass
    def e_RightButtonPressEvent(self,obj,event):
        pass
    def e_RightButtonReleaseEvent(self,obj,event):
        pass
    def e_EnterEvent(self,obj,event):
        pass
    def e_LeaveEvent(self,obj,event):
        pass
    def e_KeyPressEvent(self,obj,event):
        key = self.e_GetInteractor().GetKeySym()
        self.e_OnkeyRelease()    # reload function
        #self.e_OnKeyDown()
        #self.e_OnKeyUp()
        #self.e_OnKeyPress()
        return 
    def e_KeyReleaseEvent(self,obj,event):
        pass
    def e_CharEvent(self,obj,event):
        pass
    def e_ExposeEvent(self,obj,event):
        pass
    def e_ConfigureEvent(self,obj,event):
        pass
    def e_TimerEvent(self,obj,event):
        pass
    def e_MouseMoveEvent(self,obj,event):
        pass
    def e_MouseWheelForwardEvent(self,obj,event):
        pass
    def e_MouseWheelBackwardEvent(self,obj,event):
        pass
    def e_ResetCameraEvent(self,obj,event):
        pass
    def e_ResetCameraClippingRangeEvent (self,obj,event):
        pass
    def e_ModifiedEvent(self,obj,event):
        pass
    def e_WindowLevelEvent(self,obj,event):
        pass
    def e_StartWindowLevelEvent(self,obj,event):
        pass
    def e_EndWindowLevelEvent(self,obj,event):
        pass
    def e_ResetWindowLevelEvent(self,obj,event):
        pass
    def e_SetOutputEvent(self,obj,event):
        pass
    def e_ErrorEvent(self,obj,event):
        pass
    def e_WarningEvent(self,obj,event):
        pass
    def e_StartInteractionEvent(self,obj,event):
        pass
    def e_InteractionEvent(self,obj,event):
        pass
    def e_EndInteractionEvent(self,obj,event):
        pass
    def e_EnableEvent(self,obj,event):
        pass
    def e_DisableEvent(self,obj,event):
        pass
    def e_CreateTimerEvent(self,obj,event):
        pass
    def e_DestroyTimerEvent(self,obj,event):
        pass
    def e_PlacePointEvent(self,obj,event):
        pass
    def e_PlaceWidgetEvent(self,obj,event):
        pass
    def e_CursorChangedEvent(self,obj,event):
        pass
    def e_ExecuteInformationEvent(self,obj,event):
        pass
    def e_RenderWindowMessageEvent(self,obj,event):
        pass
    def e_WrongTagEvent(self,obj,event):
        pass
    def e_StartAnimationCueEvent(self,obj,event):
        pass
    def e_AnimationCueTickEvent(self,obj,event):
        pass
    def e_EndAnimationCueEvent(self,obj,event):
        pass
    def e_VolumeMapperRenderProgressEvent(self,obj,event):
        pass
    def e_VolumeMapperComputeGradientsEndEvent(self,obj,event):
        pass
    def e_VolumeMapperComputeGradientsProgressEvent(self,obj,event):
        pass
    def e_VolumeMapperComputeGradientsStartEvent(self,obj,event):
        pass
    def e_WidgetModifiedEvent(self,obj,event):
        pass
    def e_WidgetValueChangedEvent(self,obj,event):
        pass
    def e_WidgetActivateEvent(self,obj,event):
        pass
    def e_UserEvent(self,obj,event):
        pass

# define global event call back function
def NoEvent(obj,event):
    pass
def AnyEvent(obj,event):
    pass
def DeleteEvent(obj,event):
    pass
def StartEvent(obj,event):
    pass
def EndEvent(obj,event):
    pass
def RenderEvent(obj,event):
    pass
def ProgressEvent(obj,event):
    pass
def PickEvent(obj,event):
    pass
def StartPickEvent(obj,event):
    pass
def EndPickEvent(obj,event):
    pass
def AbortCheckEvent(obj,event):
    pass
def ExitEvent(obj,event):
    pass
def LeftButtonPressEvent(obj,event):
    pass
def LeftButtonReleaseEvent(obj,event):
    pass
def MiddleButtonPressEvent(obj,event):
    pass
def MiddleButtonReleaseEvent(obj,event):
    pass
def RightButtonPressEvent(obj,event):
    pass
def RightButtonReleaseEvent(obj,event):
    pass
def EnterEvent(obj,event):
    pass
def LeaveEvent(obj,event):
    pass
def KeyPressEvent(obj,event):
    key = obj.GetKeySym() 
    pass
def KeyReleaseEvent(obj,event):
    pass
def CharEvent(obj,event):
    pass
def ExposeEvent(obj,event):
    pass
def ConfigureEvent(obj,event):
    pass
def TimerEvent(obj,event):
    pass
def MouseMoveEvent(obj,event):
    pass
def MouseWheelForwardEvent(obj,event):
    pass
def MouseWheelBackwardEvent(obj,event):
    pass
def ResetCameraEvent(obj,event):
    pass
def ResetCameraClippingRangeEvent (obj,event):
    pass
def ModifiedEvent(obj,event):
    pass
def WindowLevelEvent(obj,event):
    pass
def StartWindowLevelEvent(obj,event):
    pass
def EndWindowLevelEvent(obj,event):
    pass
def ResetWindowLevelEvent(obj,event):
    pass
def SetOutputEvent(obj,event):
    pass
def ErrorEvent(obj,event):
    pass
def WarningEvent(obj,event):
    pass
def StartInteractionEvent(obj,event):
    pass
def InteractionEvent(obj,event):
    pass
def EndInteractionEvent(obj,event):
    pass
def EnableEvent(obj,event):
    pass
def DisableEvent(obj,event):
    pass
def CreateTimerEvent(obj,event):
    pass
def DestroyTimerEvent(obj,event):
    pass
def PlacePointEvent(obj,event):
    pass
def PlaceWidgetEvent(obj,event):
    pass
def CursorChangedEvent(obj,event):
    pass
def ExecuteInformationEvent(obj,event):
    pass
def RenderWindowMessageEvent(obj,event):
    pass
def WrongTagEvent(obj,event):
    pass
def StartAnimationCueEvent(obj,event):
    pass
def AnimationCueTickEvent(obj,event):
    pass
def EndAnimationCueEvent(obj,event):
    pass
def VolumeMapperRenderProgressEvent(obj,event):
    pass
def VolumeMapperComputeGradientsEndEvent(obj,event):
    pass
def VolumeMapperComputeGradientsProgressEvent(obj,event):
    pass
def VolumeMapperComputeGradientsStartEvent(obj,event):
    pass
def WidgetModifiedEvent(obj,event):
    pass
def WidgetValueChangedEvent(obj,event):
    pass
def WidgetActivateEvent(obj,event):
    pass
def UserEvent(obj,event):
    pass



# way1: create a interactorstyle and add it to interactor
interactor1 = vtk.vtkRenderWindowInteractor()
new_style = QIN_Style()
interactor1.SetInteractorStyle(new_style)

# way2: add observer to interactor directly
interactor2 = vtk.vtkRenderWindowInteractor()
interactor2.AddObserver(vtk.vtkCommand.LeftButtonPressEvent,LeftButtonPressEvent)

