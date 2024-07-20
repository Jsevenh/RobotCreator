# ***************************************************************************
# *   Copyright (c) 2023-2024 David Carter <dcarter@davidcarter.ca>         *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************
"""Class for drawing material tab"""

'''
important resources 
python material tests 
https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/Material/materialtests/TestMaterials.py

c++ material tests 
https://github.com/FreeCAD/FreeCAD/blob/main/tests/src/Mod/Material/App/TestMaterials.cpp

code relating to the UI python 
https://github.com/davesrocketshop/Rocket/blob/materials_20240307/Ui/Widgets/MaterialTab.py
'''
__title__ = "FreeCAD Material Tab"
__author__ = "David Carter"
__url__ = "https://www.davesrocketshop.com"
    

from PySide2.QtCore import QSize
import FreeCADGui

from DraftTools import translate

import Materials
import MatGui


from PySide2.QtWidgets import QGridLayout, QVBoxLayout,QDialog,QDialogButtonBox
from PySide2 import QtCore

from Rocket.Material import Material

class MaterialTab(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.uuid=None
        btns=QDialogButtonBox.Ok|QDialogButtonBox.Cancel
        self.dialog_btns=QDialogButtonBox(btns)
        self.dialog_btns.accepted.connect(self.accept)
        self.dialog_btns.rejected.connect(self.cancel)
        self.setTabMaterial()
        self.move(300,250)
        self.setWindowTitle("Material Selection")
    def setTabMaterial(self):
        self.materialManager = Materials.MaterialManager()

        ui = FreeCADGui.UiLoader()

        self.materialTreeWidget = ui.createWidget("MatGui::MaterialTreeWidget")
        self.materialTreePy = MatGui.MaterialTreeWidget(self.materialTreeWidget)
        self.materialTreeWidget.onMaterial.connect(self.onMaterial)
        
        row = 0
        grid = QGridLayout()

        grid.addWidget(self.materialTreeWidget, row, 0)
        row += 1

        layout = QVBoxLayout()
        layout.addItem(grid)
        layout.addWidget(self.dialog_btns)
        self.setLayout(layout)
        
    def transferTo(self, obj):
        "Transfer from the dialog to the object"
        obj.ShapeMaterial = self.materialManager.getMaterial(self.uuid)

    def transferFrom(self, obj):
        "Transfer from the object to the dialog"
        self.uuid = obj.ShapeMaterial.UUID
        self.materialTreePy.UUID = self.uuid

    def onMaterial(self, uuid):
        self.uuid = uuid
    def sizeHint(self) -> QSize:
        return QSize(700,400)
    
    def accept(self):
        print(self.uuid)
        self.close()
    def cancel(self):
        self.close()
        
if __name__=="__main__":
    m=MaterialTab()
    m.exec_()