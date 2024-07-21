from PySide2.QtCore import QSize
from PySide2.QtWidgets import QDialog,QListView
from PySide2 import QtCore

from ..RD_utils import parse_assembly,initialize_element_tree
from .. import common



class link_list(QtCore.QAbstractListModel):
    def __init__(self):
        super.__init__()
        self.proxy=App.ActiveDocument.urdf.Proxy
        # get the dictionary to store  info 
        self.d=self.Proxy.element_dict
        self.links=[]
        self.density=1 #kg/m^3
        self.link_elem=initialize_element_tree.convdict_2_tree("link.urdf").get_element
    def get_links(self):
        self.links= App.ActiveDocument.findObjects("App::Link")
        
        for link in self.links:
            link_info=parse_assembly.get_link_info(link)
            
        common.update_dictionary(['urdf'],)
class extract_assembly:
    def __init__(self):
        pass
    
class assemble_ui(QDialog):
    def __init__(self,parent=None):
        super.__init__()

    def sizeHint(self) -> QSize:
        return QSize(250,730)
    def init_ui(self):
        pass