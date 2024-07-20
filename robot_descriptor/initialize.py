import FreeCAD 
import FreeCADGui
import os 
from PySide import QtGui,QtCore

import resources
#import Spreadsheet
import xml.etree.ElementTree as ET 

from .RD_utils import initialize_element_tree
#directory to initilize icon 

__format_pref__=FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/RobotDescriptor")
#class to store the selected properties

_DESCRIPTION_FORMAT='sdf'
_SDF_VERSION='1.10'
#this will hold the entire sdf definition of the sdf file 
#as a dictionary which will then be converted into a .sdf file

class RD_properties:
	def __init__(self):
		# check for the configured  format 
		if __format_pref__.GetBool("format_urdf") is True:
			self.description_format='urdf'
		else:
			self.description_format='sdf'
		self.Type="Dictionary"
		self._element_dict=None
	@property 
	def format(self):
		return self.description_format
    
	@format.setter
	def format(self,value):
		self.description_format=value
    
	@property
	def element_dict(self):
		return self._element_dict
    
	@element_dict.setter
	def element_dict(self,elem_d:dict):
		'''returns a dictionary {"tag":tag_name,"element_str":element converted to string,"children":[]}'''
		self._element_dict=elem_d
        
#===================================================
#initialize
#===================================================
class initialize:
	def __init__(self):
    #ensure there is an active document
		document=FreeCAD.ActiveDocument
		
# check to ensure  a document object exists, if it does not add it
		if not hasattr(FreeCAD.ActiveDocument, "Robot_Description"):
      # create a document group  for robot descriptor 
			group =document.addObject("App::DocumentObjectGroup","Robot_Description")
   # create a folder to use for storing all the meshes generated by the workbench 
			mesh_group=document.addObject("App::DocumentObjectGroup","meshes")
			group.addObject(mesh_group)
			#spreadsheet for points of the road 
			# only add points if forma is sdf 
   # add a seperate container for sdf and urdf  depending on the selected option 
		if __format_pref__.GetBool("format_sdf") is True and hasattr(FreeCAD.ActiveDocument, "sdf") is False:
       # since sdf is true create a container to store sdf related  info
				sdf_description_properties=RD_properties()
				sdf=document.addObject("App::DocumentObjectGroupPython","sdf")
				document.Robot_Description.addObject(sdf)
				points=document.addObject('Spreadsheet::Sheet','points')
				sdf.addObject(points)
			# label columns 
				for row,label in [('A','x'),('B','y'),('C','z')]:
					points.set(f'{row}1',label)
					points.set(f'{row}2','0')
					points.setStyle(f'{row}1','bold')
				sdf.Proxy=sdf_description_properties
		# if description_properties.format=='sdf':
	# create an element tree for the root node 
	# convert to string to allow serialization 
	#there might be a better way to handle this 
				root_elem=initialize_element_tree.convdict_2_tree("root.sdf").get_element
				root_elem_str=ET.tostring(root_elem,encoding='unicode',xml_declaration=None)
# some elements may occur multiple times in a parent element e.g a world can have many models 
# the recurring key is used to track this , if false the elem_str will be a string , if 
#true elem_str will be a list of strings where each index will be an instance of the element
				sdf.Proxy.element_dict={"sdf":{"elem_str":root_elem_str,"recurring":False,"children":{}}}
    #object will store a pointer to the active widget
		if __format_pref__.GetBool("format_urdf") is True and hasattr(FreeCAD.ActiveDocument, "urdf") is False:
       # store urdf related data in the urdf container 
				urdf_description_properties=RD_properties()
				urdf=document.addObject("App::DocumentObjectGroupPython","urdf")
				document.Robot_Description.addObject(urdf)
				root_elem=initialize_element_tree.convdict_2_tree("root.urdf").get_element
				root_elem_str=ET.tostring(root_elem,encoding='unicode',xml_declaration=None)
		#set proxy 
				urdf.Proxy=urdf_description_properties
				urdf.Proxy.element_dict={"urdf":{"elem_str":root_elem_str,"recurring":False,"children":{}}}
		else:
				pass

		document.recompute()
'''
dictionary format:
		{
			key: element tag name
			value: a dictionary 
   				{
					key: elem_str
					value: string representation of the element,

					key: recurring
					value: a boolean value that indicates if an element can have multiple occurences
     
					key: children
					value: a dictionary of children exhibiting the same  format as the parent
     				{
						
					}
				}
		}
'''								

class RD_init:
    
	def GetResources(self):
		return {"Pixmap":":/icons/initialize.svg","Accel":"shift+i","MenuText":"Initialization ","ToolTip":"initialize properties"}
		
	def Activated(self):
		if FreeCAD.activeDocument() is None:
			return
		else:
			self.rd=initialize()
        
	def IsActive(self):
		if FreeCAD.activeDocument() is not None :
			#check if robot description document object is already defined 
			#return false if its already defined no need to re-initialize again
			if hasattr(FreeCAD.ActiveDocument, "Robot_Description"):
				if __format_pref__.GetBool("format_urdf") is True and hasattr(FreeCAD.ActiveDocument, "urdf") is False:
					return True
				elif __format_pref__.GetBool("format_sdf") is True and hasattr(FreeCAD.ActiveDocument, "sdf") is False:
					return True
				else:
					return False
			else:
				return True
		else:
			return False



FreeCADGui.addCommand('RD_init',RD_init()) 