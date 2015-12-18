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

'''





import vtk


# define a interactor style that re-implement all event callback


class QIN_Style(vtk.vtkInteractorStyleImage):
	def __init__(self):
		self.AddObserver("NoEvent",self.)
		self.AddObserver("AnyEvent",self.)
		self.AddObserver("DeleteEvent",self.)
		self.AddObserver("StartEvent",self.)
		self.AddObserver("EndEvent",self.)
		self.AddObserver("RenderEvent",self.)
		self.AddObserver("ProgressEvent",self.)
		self.AddObserver("PickEvent",self.)
		self.AddObserver("StartPickEvent",self.)
		self.AddObserver("EndPickEvent",self.)
		self.AddObserver("AbortCheckEvent",self.)
		self.AddObserver("ExitEvent",self.)
		self.AddObserver("LeftButtonPressEvent",self.)
		self.AddObserver("LeftButtonReleaseEvent",self.)
		self.AddObserver("MiddleButtonPressEvent",self.)
		self.AddObserver("MiddleButtonReleaseEvent",self.)
		self.AddObserver("RightButtonPressEvent",self.)
		self.AddObserver("RightButtonReleaseEvent",self.)
		self.AddObserver("EnterEvent",self.)
		self.AddObserver("LeaveEvent",self.)
		self.AddObserver("KeyPressEvent",self.)
		self.AddObserver("KeyReleaseEvent",self.)
		self.AddObserver("CharEvent",self.)
		self.AddObserver("ExposeEvent",self.)
		self.AddObserver("ConfigureEvent",self.)
		self.AddObserver("TimerEvent",self.)
		self.AddObserver("MouseMoveEvent",self.)
		self.AddObserver("MouseWheelForwardEvent",self.)
		self.AddObserver("MouseWheelBackwardEvent",self.)
		self.AddObserver("ResetCameraEvent",self.)
		self.AddObserver("ResetCameraClippingRangeEvent",self.)
		self.AddObserver("ModifiedEvent",self.)
		self.AddObserver("WindowLevelEvent",self.)
		self.AddObserver("StartWindowLevelEvent",self.)
		self.AddObserver("EndWindowLevelEvent",self.)
		self.AddObserver("ResetWindowLevelEvent",self.)
		self.AddObserver("SetOutputEvent",self.)
		self.AddObserver("ErrorEvent",self.)
		self.AddObserver("WarningEvent",self.)
		self.AddObserver("StartInteractionEvent",self.)
		self.AddObserver("InteractionEvent",self.)
		self.AddObserver("EndInteractionEvent",self.)
		self.AddObserver("EnableEvent",self.)
		self.AddObserver("DisableEvent",self.)
		self.AddObserver("CreateTimerEvent",self.)
		self.AddObserver("DestroyTimerEvent",self.)
		self.AddObserver("PlacePointEvent",self.)
		self.AddObserver("PlaceWidgetEvent",self.)
		self.AddObserver("CursorChangedEvent",self.)
		self.AddObserver("ExecuteInformationEvent",self.)
		self.AddObserver("RenderWindowMessageEvent",self.)
		self.AddObserver("WrongTagEvent",self.)
		self.AddObserver("StartAnimationCueEvent",self.)
		self.AddObserver("AnimationCueTickEvent",self.)
		self.AddObserver("EndAnimationCueEvent",self.)
		self.AddObserver("VolumeMapperRenderProgressEvent",self.)
		self.AddObserver("VolumeMapperComputeGradientsEndEvent",self.)
		self.AddObserver("VolumeMapperComputeGradientsProgressEvent",self.)
		self.AddObserver("VolumeMapperComputeGradientsStartEvent",self.)
		self.AddObserver("WidgetModifiedEvent",self.)
		self.AddObserver("WidgetValueChangedEvent",self.)
		self.AddObserver("WidgetActivateEvent",self.)
		self.AddObserver("UserEvent",self.)

	def NoEvent(self,obj,event):
		pass
	def AnyEvent(self,obj,event):
		pass
	def DeleteEvent(self,obj,event):
		pass
	def StartEvent(self,obj,event):
		pass
	def EndEvent(self,obj,event):
		pass
	def RenderEvent(self,obj,event):
		pass
	def ProgressEvent(self,obj,event):
		pass
	def PickEvent(self,obj,event):
		pass
	def StartPickEvent(self,obj,event):
		pass
	def EndPickEvent(self,obj,event):
		pass
	def AbortCheckEvent(self,obj,event):
		pass
	def ExitEvent(self,obj,event):
		pass
	def LeftButtonPressEvent(self,obj,event):
		pass
	def LeftButtonReleaseEvent(self,obj,event):
		pass
	def MiddleButtonPressEvent(self,obj,event):
		pass
	def MiddleButtonReleaseEvent(self,obj,event):
		pass
	def RightButtonPressEvent(self,obj,event):
		pass
	def RightButtonReleaseEvent(self,obj,event):
		pass
	def EnterEvent(self,obj,event):
		pass
	def LeaveEvent(self,obj,event):
		pass
	def KeyPressEvent(self,obj,event):
		pass
	def KeyReleaseEvent(self,obj,event):
		pass
	def CharEvent(self,obj,event):
		pass
	def ExposeEvent(self,obj,event):
		pass
	def ConfigureEvent(self,obj,event):
		pass
	def TimerEvent(self,obj,event):
		pass
	def MouseMoveEvent(self,obj,event):
		pass
	def MouseWheelForwardEvent(self,obj,event):
		pass
	def MouseWheelBackwardEvent(self,obj,event):
		pass
	def ResetCameraEvent(self,obj,event):
		pass
	def ResetCameraClippingRangeEvent (self,obj,event):
		pass
	def ModifiedEvent(self,obj,event):
		pass
	def WindowLevelEvent(self,obj,event):
		pass
	def StartWindowLevelEvent(self,obj,event):
		pass
	def EndWindowLevelEvent(self,obj,event):
		pass
	def ResetWindowLevelEvent(self,obj,event):
		pass
	def SetOutputEvent(self,obj,event):
		pass
	def ErrorEvent(self,obj,event):
		pass
	def WarningEvent(self,obj,event):
		pass
	def StartInteractionEvent(self,obj,event):
		pass
	def InteractionEvent(self,obj,event):
		pass
	def EndInteractionEvent(self,obj,event):
		pass
	def EnableEvent(self,obj,event):
		pass
	def DisableEvent(self,obj,event):
		pass
	def CreateTimerEvent(self,obj,event):
		pass
	def DestroyTimerEvent(self,obj,event):
		pass
	def PlacePointEvent(self,obj,event):
		pass
	def PlaceWidgetEvent(self,obj,event):
		pass
	def CursorChangedEvent(self,obj,event):
		pass
	def ExecuteInformationEvent(self,obj,event):
		pass
	def RenderWindowMessageEvent(self,obj,event):
		pass
	def WrongTagEvent(self,obj,event):
		pass
	def StartAnimationCueEvent(self,obj,event):
		pass
	def AnimationCueTickEvent(self,obj,event):
		pass
	def EndAnimationCueEvent(self,obj,event):
		pass
	def VolumeMapperRenderProgressEvent(self,obj,event):
		pass
	def VolumeMapperComputeGradientsEndEvent(self,obj,event):
		pass
	def VolumeMapperComputeGradientsProgressEvent(self,obj,event):
		pass
	def VolumeMapperComputeGradientsStartEvent(self,obj,event):
		pass
	def WidgetModifiedEvent(self,obj,event):
		pass
	def WidgetValueChangedEvent(self,obj,event):
		pass
	def WidgetActivateEvent(self,obj,event):
		pass
	def UserEvent(self,obj,event):
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



