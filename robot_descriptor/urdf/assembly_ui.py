from PySide2.QtCore import QSize
from PySide2.QtWidgets import QDialog,QListView
from PySide2 import QtCore

from ..RD_utils import parse_assembly


class link_list(QtCore.QAbstractListModel):
    def __init__(self):
        super.__init__()
        self.proxy=App.ActiveDocument.urdf.Proxy
        # get the dictionary to store  info 
        self.d=self.Proxy.element_dict
    def get_links(self):
        self.links= App.ActiveDocument.findObjects("App::Link")
    
class extract_assembly:
    def __init__(self):
        
    
class assemble_ui(QDialog):
    def __init__(self,parent=None):
        super.__init__()

    def sizeHint(self) -> QSize:
        return QSize(250,730)
    