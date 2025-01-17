from FreeCAD import Gui
from FreeCAD import Base
import FreeCAD, FreeCADGui, Part, os, math
from robot_descriptor import resources
__title__ = "RobotDescriptor Workbench - Init file"
__author__ = ''
__url__ = "https://www.freecadweb.org"

class RobotDescriptor (Workbench):

	def __init__(self):
		def QT_TRANSLATE_NOOP(context, text):
			return text
		__dirname__ = os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "RobotDescriptor")
		_tooltip = "The RobotDesciptor workbench is used to create robot description files "
		self.__class__.Icon = os.path.join(__dirname__, "robot_descriptor", "icons", "robot_icon.svg")
		self.__class__.MenuText = QT_TRANSLATE_NOOP("RobotDescriptor", "RobotDescriptor")
		self.__class__.ToolTip = QT_TRANSLATE_NOOP("robot_descriptor", _tooltip)

	def Initialize(self):
		"This function is executed when FreeCAD starts"
		__dirname__ = os.path.join(FreeCAD.getUserAppDataDir(), "Mod", "RobotDescriptor")
		#add icon path 
		FreeCADGui.addIconPath(":/icons")
		#print("got dir:" + __dirname__);
		prefer_ui=os.path.join(__dirname__,"robot_descriptor","forms","RobotDescriptor_prefs.ui")
		FreeCADGui.addPreferencePage(prefer_ui,"RobotDescriptor")
		format=App.ParamGet("User parameter:BaseApp/Preferences/Mod/RobotDescriptor")
		# format_sdf is the name used to store the sdf property 
		# check the  preferences ui file  an the FreeCAD documentation on preferences 
		# https://wiki.freecad.org/Workbench_creation then jump to the preferences section
		if format.GetBool("format_sdf") is True:
			from robot_descriptor import initialize ,model_editor
			from robot_descriptor.sdf_elements import world
			self.list = ['RD_initialize','world_properties','Model_Editor']
			self.appendToolbar("RobotDescription",self.list) # creates a new toolbar with your commands
			self.appendMenu("Robot Description",self.list) # creates a new menu
		elif format.GetBool("format_urdf") is True:
			from robot_descriptor import initialize
			self.list=["RD_urdf_init"]
			self.appendToolbar("RobotDescription",self.list) # creates a new toolbar with your commands
			self.appendMenu("Robot Description",self.list) 
		#self.appendMenu(["Robot Description","Tools"],self.list) # appends a submenu to an existing menu
		#add icon path 
	
	def Activated(self):
		"This function is executed when the workbench is activated"
		return

	def Deactivated(self):
		"This function is executed when the workbench is deactivated"
		
		return

	def ContextMenu(self, recipient):
		"This is executed whenever the user right-clicks on screen"
		# "recipient" will be either "view" or "tree"
		self.appendContextMenu("Robot Description",self.list) # add commands to the context menu

	def GetClassName(self): 
		# this function is mandatory if this is a full python workbench
		return "Gui::PythonWorkbench"

Gui.addWorkbench(RobotDescriptor())
