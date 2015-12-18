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
		self.AddObserver("NoEvent",self.                                  )
		self.AddObserver("AnyEvent",self.                                 )
		self.AddObserver("DeleteEvent",self.                              )
		self.AddObserver("StartEvent",self.                               )
		self.AddObserver("EndEvent",self.                                 )
		self.AddObserver("RenderEvent",self.                              )
		self.AddObserver("ProgressEvent",self.                            )
		self.AddObserver("PickEvent",self.                                )
		self.AddObserver("StartPickEvent",self.                           )
		self.AddObserver("EndPickEvent",self.                             )
		self.AddObserver("AbortCheckEvent",self.                          )
		self.AddObserver("ExitEvent",self.                                )
		self.AddObserver("LeftButtonPressEvent",self.                     )
		self.AddObserver("LeftButtonReleaseEvent",self.                   )
		self.AddObserver("MiddleButtonPressEvent",self.                   )
		self.AddObserver("MiddleButtonReleaseEvent",self.                 )
		self.AddObserver("RightButtonPressEvent",self.                    )
		self.AddObserver("RightButtonReleaseEvent",self.                  )
		self.AddObserver("EnterEvent",self.                               )
		self.AddObserver("LeaveEvent",self.                               )
		self.AddObserver("KeyPressEvent",self.                            )
		self.AddObserver("KeyReleaseEvent",self.                          )
		self.AddObserver("CharEvent",self.                                )
		self.AddObserver("ExposeEvent",self.                              )
		self.AddObserver("ConfigureEvent",self.                           )
		self.AddObserver("TimerEvent",self.                               )
		self.AddObserver("MouseMoveEvent",self.                           )
		self.AddObserver("MouseWheelForwardEvent",self.                   )
		self.AddObserver("MouseWheelBackwardEvent",self.                  )
		self.AddObserver("ResetCameraEvent",self.                         )
		self.AddObserver("ResetCameraClippingRangeEvent",self.            )
		self.AddObserver("ModifiedEvent",self.                            )
		self.AddObserver("WindowLevelEvent",self.                         )
		self.AddObserver("StartWindowLevelEvent",self.                    )
		self.AddObserver("EndWindowLevelEvent",self.                      )
		self.AddObserver("ResetWindowLevelEvent",self.                    )
		self.AddObserver("SetOutputEvent",self.                           )
		self.AddObserver("ErrorEvent",self.                               )
		self.AddObserver("WarningEvent",self.                             )
		self.AddObserver("StartInteractionEvent",self.                    )
		self.AddObserver("InteractionEvent",self.                         )
		self.AddObserver("EndInteractionEvent",self.                      )
		self.AddObserver("EnableEvent",self.                              )
		self.AddObserver("DisableEvent",self.                             )
		self.AddObserver("CreateTimerEvent",self.                         )
		self.AddObserver("DestroyTimerEvent",self.                        )
		self.AddObserver("PlacePointEvent",self.                          )
		self.AddObserver("PlaceWidgetEvent",self.                         )
		self.AddObserver("CursorChangedEvent",self.                       )
		self.AddObserver("ExecuteInformationEvent",self.                  )
		self.AddObserver("RenderWindowMessageEvent",self.                 )
		self.AddObserver("WrongTagEvent",self.                            )
		self.AddObserver("StartAnimationCueEvent",self.                   )
		self.AddObserver("AnimationCueTickEvent",self.                    )
		self.AddObserver("EndAnimationCueEvent",self.                     )
		self.AddObserver("VolumeMapperRenderProgressEvent",self.          )
		self.AddObserver("VolumeMapperComputeGradientsEndEvent",self.     )
		self.AddObserver("VolumeMapperComputeGradientsProgressEvent",self.)
		self.AddObserver("VolumeMapperComputeGradientsStartEvent",self.   )
		self.AddObserver("WidgetModifiedEvent",self.                      )
		self.AddObserver("WidgetValueChangedEvent",self.                  )
		self.AddObserver("WidgetActivateEvent",self.                      )
		self.AddObserver("UserEvent",self.                                )

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
NoEvent
(obj,event):

	pass
AnyEvent
(obj,event):

	pass
DeleteEvent(obj,event):

	pass
StartEvent(obj,event):

	pass
EndEvent(obj,event):

	pass
RenderEvent(obj,event):

	pass
ProgressEvent(obj,event):

	pass
PickEvent(obj,event):

	pass
StartPickEvent(obj,event):

	pass
EndPickEvent(obj,event):

	pass
AbortCheckEvent(obj,event):

	pass
ExitEvent(obj,event):

	pass
LeftButtonPressEvent(obj,event):

	pass
LeftButtonReleaseEvent(obj,event):

	pass
MiddleButtonPressEvent(obj,event):

	pass
MiddleButtonReleaseEvent(obj,event):

	pass
RightButtonPressEvent(obj,event):

	pass
RightButtonReleaseEvent(obj,event):
	pass
EnterEvent(obj,event):
	pass
LeaveEvent(obj,event):
	pass
KeyPressEvent(obj,event):

	pass
KeyReleaseEvent(obj,event):
	pass
CharEvent(obj,event):
	pass
ExposeEvent(obj,event):
	pass
ConfigureEvent(obj,event):

	pass
TimerEvent(obj,event):

	pass
MouseMoveEvent(obj,event):

	pass
MouseWheelForwardEvent(obj,event):

	pass
MouseWheelBackwardEvent(obj,event):

	pass
ResetCameraEvent(obj,event):

	pass
ResetCameraClippingRangeEvent(obj,event):

	pass
ModifiedEvent(obj,event):

	pass
WindowLevelEvent(obj,event):

	pass
StartWindowLevelEvent(obj,event):

	pass
EndWindowLevelEvent(obj,event):

	pass
ResetWindowLevelEvent(obj,event):

	pass
SetOutputEvent(obj,event):

	pass
ErrorEvent(obj,event):

	pass
WarningEvent(obj,event):

	pass
StartInteractionEvent(obj,event):

	pass
InteractionEvent(obj,event):

	pass
EndInteractionEvent(obj,event):

	pass
EnableEvent(obj,event):

	pass
DisableEvent(obj,event):

	pass
CreateTimerEvent(obj,event):

	pass
DestroyTimerEvent(obj,event):

	pass
PlacePointEvent(obj,event):

	pass
PlaceWidgetEvent(obj,event):

	pass
CursorChangedEvent(obj,event):

	pass
ExecuteInformationEvent(obj,event):

	pass
RenderWindowMessageEvent(obj,event):

	pass
WrongTagEvent(obj,event):

	pass
StartAnimationCueEvent(obj,event):

	pass
AnimationCueTickEvent(obj,event):

	pass
EndAnimationCueEvent(obj,event):

	pass
VolumeMapperRenderProgressEvent(obj,event):

	pass
VolumeMapperComputeGradientsEndEvent(obj,event):

	pass
VolumeMapperComputeGradientsProgressEvent(obj,event):

	pass
VolumeMapperComputeGradientsStartEvent(obj,event):

	pass
WidgetModifiedEvent(obj,event):

	pass
WidgetValueChangedEvent(obj,event):

	pass
WidgetActivateEvent(obj,event):

	pass
UserEvent(obj,event):
	pass




