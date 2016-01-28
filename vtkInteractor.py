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
		self.AddObserver("NoEvent",self.NoEvent)
		self.AddObserver("AnyEvent",self.AnyEvent)
		self.AddObserver("DeleteEvent",self.DeleteEvent)
		self.AddObserver("StartEvent",self.StartEvent)
		self.AddObserver("EndEvent",self.EndEvent)
		self.AddObserver("RenderEvent",self.RenderEvent)
		self.AddObserver("ProgressEvent",self.ProgressEvent)
		self.AddObserver("PickEvent",self.PickEvent)
		self.AddObserver("StartPickEvent",self.StartPickEvent)
		self.AddObserver("EndPickEvent",self.EndPickEvent)
		self.AddObserver("AbortCheckEvent",self.AbortCheckEvent)
		self.AddObserver("ExitEvent",self.ExitEvent)
		self.AddObserver("LeftButtonPressEvent",self.LeftButtonPressEvent)
		self.AddObserver("LeftButtonReleaseEvent",self.LeftButtonReleaseEvent)
		self.AddObserver("MiddleButtonPressEvent",self.MiddleButtonPressEvent)
		self.AddObserver("MiddleButtonReleaseEvent",self.MiddleButtonReleaseEvent)
		self.AddObserver("RightButtonPressEvent",self.RightButtonPressEvent)
		self.AddObserver("RightButtonReleaseEvent",self.RightButtonReleaseEvent)
		self.AddObserver("EnterEvent",self.EnterEvent)
		self.AddObserver("LeaveEvent",self.LeaveEvent)
		self.AddObserver("KeyPressEvent",self.KeyPressEvent)
		self.AddObserver("KeyReleaseEvent",self.KeyReleaseEvent)
		self.AddObserver("CharEvent",self.CharEvent)
		self.AddObserver("ExposeEvent",self.ExposeEvent)
		self.AddObserver("ConfigureEvent",self.ConfigureEvent)
		self.AddObserver("TimerEvent",self.TimerEvent)
		self.AddObserver("MouseMoveEvent",self.MouseMoveEvent)
		self.AddObserver("MouseWheelForwardEvent",self.MouseWheelForwardEvent)
		self.AddObserver("MouseWheelBackwardEvent",self.MouseWheelBackwardEvent)
		self.AddObserver("ResetCameraEvent",self.ResetCameraEvent)
		self.AddObserver("ResetCameraClippingRangeEvent",self.ResetCameraClippingRangeEvent)
		self.AddObserver("ModifiedEvent",self.ModifiedEvent)
		self.AddObserver("WindowLevelEvent",self.WindowLevelEvent)
		self.AddObserver("StartWindowLevelEvent",self.StartWindowLevelEvent)
		self.AddObserver("EndWindowLevelEvent",self.EndWindowLevelEvent)
		self.AddObserver("ResetWindowLevelEvent",self.ResetWindowLevelEvent)
		self.AddObserver("SetOutputEvent",self.SetOutputEvent)
		self.AddObserver("ErrorEvent",self.ErrorEvent)
		self.AddObserver("WarningEvent",self.WarningEvent)
		self.AddObserver("StartInteractionEvent",self.StartInteractionEvent)
		self.AddObserver("InteractionEvent",self.InteractionEvent)
		self.AddObserver("EndInteractionEvent",self.EndInteractionEvent)
		self.AddObserver("EnableEvent",self.EnableEvent)
		self.AddObserver("DisableEvent",self.DisableEvent)
		self.AddObserver("CreateTimerEvent",self.CreateTimerEvent)
		self.AddObserver("DestroyTimerEvent",self.DestroyTimerEvent)
		self.AddObserver("PlacePointEvent",self.PlacePointEvent)
		self.AddObserver("PlaceWidgetEvent",self.PlaceWidgetEvent)
		self.AddObserver("CursorChangedEvent",self.CursorChangedEvent)
		self.AddObserver("ExecuteInformationEvent",self.ExecuteInformationEvent)
		self.AddObserver("RenderWindowMessageEvent",self.RenderWindowMessageEvent)
		self.AddObserver("WrongTagEvent",self.WrongTagEvent)
		self.AddObserver("StartAnimationCueEvent",self.StartAnimationCueEvent)
		self.AddObserver("AnimationCueTickEvent",self.AnimationCueTickEvent)
		self.AddObserver("EndAnimationCueEvent",self.EndAnimationCueEvent)
		self.AddObserver("VolumeMapperRenderProgressEvent",self.VolumeMapperRenderProgressEvent)
		self.AddObserver("VolumeMapperComputeGradientsEndEvent",self.VolumeMapperComputeGradientsEndEvent)
		self.AddObserver("VolumeMapperComputeGradientsProgressEvent",self.VolumeMapperComputeGradientsProgressEvent)
		self.AddObserver("VolumeMapperComputeGradientsStartEvent",self.VolumeMapperComputeGradientsStartEvent)
		self.AddObserver("WidgetModifiedEvent",self.WidgetModifiedEvent)
		self.AddObserver("WidgetValueChangedEvent",self.WidgetValueChangedEvent)
		self.AddObserver("WidgetActivateEvent",self.WidgetActivateEvent)
		self.AddObserver("UserEvent",self.UserEvent)

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



# way1: create a interactorstyle and add it to interactor
interactor1 = vtk.vtkRenderWindowInteractor()
new_style = QIN_Style()
interactor1.SetInteractorStyle(new_style)

# way2: add observer to interactor directly
interactor2 = vtk.vtkRenderWindowInteractor()
interactor2.AddObserver(vtk.vtkCommand.LeftButtonPressEvent,LeftButtonPressEvent)

