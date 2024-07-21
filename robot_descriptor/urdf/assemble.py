
import resources
import FreeCAD as App
import FreeCADGui
from PySide2.QtWidgets import QMessageBox
from . import init_assembly
class extract_assembly():
    """My new command"""

    def GetResources(self):
        return {"Pixmap"  : ":/icons/assemble.svg", # the name of a svg file available in the resources
                "Accel"   : "Shift+a", # a default shortcut (optional)
                "MenuText": "extrac assembly info",
                "ToolTip" : "extract assembly info"}

    def Activated(self):
        """Do something here"""
        if len(App.ActiveDocument.findObjects("Assembly::AssemblyObject"))==0:
            QMessageBox.information(self,"Asssembly Status","No assembly Found!!")
            return
        else:
            #to be implemented
            assemble=init_assembly.assemble_ui()
            assemble.exec_()
    def IsActive(self):
        """
        only return true if   Robot_Descriptor and urdf items
        are available
        ."""
        doc=App.ActiveDocument
        if hasattr(doc,"Robot_Description"):
            if hasattr(doc,"urdf"):
                return True
        else:
            return False

FreeCADGui.addCommand("assemble", extract_assembly())