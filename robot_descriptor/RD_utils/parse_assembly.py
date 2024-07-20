import FreeCAD as App
import PySide2
import Materials
import numpy as np 
from scipy.spatial.transform import Rotation as R

#convert the rotation matrix to rpy in radians
def rotation_matrix_to_rpy(rotation_matrix):
	# Ensure the input is a numpy array
	rotation_matrix = np.array(rotation_matrix)
	
	# Check if the matrix is 3x3
	if rotation_matrix.shape != (3, 3):
		raise ValueError("The input rotation matrix must be a 3x3 matrix.")
	
	# Convert the rotation matrix to a Rotation object
	r = R.from_matrix(rotation_matrix)
	
	# Convert to RPY (roll, pitch, yaw) angles in radians
	rpy = r.as_euler('xyz', degrees=False)
	
	return rpy

def calculate_inertia_tensor(obj, rho=1):	
	'''
	rho is in kg *m^2 
	inertia is the value calculated from freecad
	FreeCAD might use a different unit system for its moment of inertia output.
	By interpreting the units as L^5/mm^5 and multiplying by the density (converted to kg/mm^3),
	you can transform the output into kg⋅mm^2 by multiplying by 1e-9
 	Finally, convert to kg⋅m^2  by applying the necessary scaling factor (10^−6).
	reference 
	Physical units are kg•m², freecad assumes density = 1 to decouple the values from the objects mass. 
	So that would be just m²
	https://forum.freecad.org/viewtopic.php?t=6836
	'''
	matrix_of_inertia = [[0,0,0],[0,0,0],[0,0,0]]
	if isinstance(obj,list) and len(obj)==3:
		if rho==1:
			return obj
		else:
			for i in range(3):
				for j in range(3):
					matrix_of_inertia[i][j] =  obj[i][j]*(rho*1e-9)*1e-6
			return matrix_of_inertia
	else:
    #   do this if obj is not a matrix assume its a linkedObject item
		inertia_matrix = obj.Document.Body.Shape.MatrixOfInertia
		matrix_of_inertia[0][0] = inertia_matrix.A11
		matrix_of_inertia[0][1] = inertia_matrix.A12
		matrix_of_inertia[0][2] = inertia_matrix.A13
		matrix_of_inertia[1][1] = inertia_matrix.A22
		matrix_of_inertia[1][2] = inertia_matrix.A23
		matrix_of_inertia[2][2] = inertia_matrix.A33
		for i in range(3):
			for j in range(3):
				matrix_of_inertia[i][j] =  matrix_of_inertia[i][j]*(rho*1e-9)*1e-6
		return matrix_of_inertia

def calc_mass(volume,rho):
	return volume*rho
#this will store the entire assembly structure and all the neccesary 
#information required to define the assembly in urdf
assembly = {}
# this is just a density value for testing 
#actual value will be extracted from the FreeCAD material data

def get_link_info(link, density=1):
		link_properties = {}
		label = link.Label
		link_properties["name"] = label
		# work on extracting visual and inertial properties 
		#allow for selection of material that a link is made up of to allow for
		# calculation of the moment of inertia
		# determine unit system to allow setting the scale of a link
		
		obj = link.LinkedObject
	
		# iii. extract volume 
		# iv. calculate mass
		volume = obj.Shape.Volume
		#convert volume to m^3
		#assuming a mm,kg,s unit system 
		volume = volume * 1e-9 
		mass = volume * density
		
		# v. extract center of mass  
		# this is the value for origin in urdf 
		center_of_mass = obj.Document.Body.Shape.CenterOfMass
		link_properties["inertial_matrix"] = calculate_inertia_tensor(obj)
		link_properties["mass"] = mass
		link_properties["inertial_origin_xyz"] = [center_of_mass[0], center_of_mass[1], center_of_mass[2]]
		placement_matrix = obj.Document.ActiveObject.Placement.Matrix
		
		rpy = rotation_matrix_to_rpy([
			[placement_matrix.A11, placement_matrix.A12, placement_matrix.A13],
			[placement_matrix.A21, placement_matrix.A22, placement_matrix.A23],
			[placement_matrix.A31, placement_matrix.A32, placement_matrix.A33]
		])
		
		link_properties["inertial_origin_rpy"] = rpy.tolist()
  
def extract_joint_info():
	joint_info={}
	joint_list=[]
	#Check if assembly object is available 
	assm=App.ActiveDocument.findObjects("Assembly::AssemblyObject")
 # ensure an assembly exists in the active document 
	if len(assm)==0:
		raise AssertionError("No assembly found in active file")

	
		#find joint object 
	jointGroup=App.ActiveDocument.findObjects("Assembly::JointGroup")
		#  joint group returns a list of all joint groups 
  
	joints=jointGroup[0].Group  # this returns a list too 

	for joint in joints:
     # skip the  grounded joint by checking if it has the attribute  JointType
     # the grounded joint lacks the joint type attribute
		if hasattr(joint,"JointType"):
			type=joint.JointType
			parent_link=joint.Part1
			child_link=joint.Part2
		#to access the labels use the .Label attribute 
			joint_info["type"]=type
			joint_info["parent_link"]=parent_link
			joint_info["child_link"]=child_link
			
'''
tasks:
1. create document object to store meshes to export 
1.1 generate the meshes and store them in the document object
2 .create ui to select location and project name 
 NB : The meshes can be edited by the user before export
    exporting will generally involve reading the mesh files and storing them in the specified location
'''