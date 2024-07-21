# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'urdf_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_urdf(object):
    def setupUi(self, urdf):
        if not urdf.objectName():
            urdf.setObjectName(u"urdf")
        urdf.resize(717, 786)
        self.verticalLayout_2 = QVBoxLayout(urdf)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(urdf)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.links_list = QListView(self.splitter)
        self.links_list.setObjectName(u"links_list")
        self.links_list.setMinimumSize(QSize(100, 0))
        self.splitter.addWidget(self.links_list)
        self.link_props = QGroupBox(self.splitter)
        self.link_props.setObjectName(u"link_props")
        self.verticalLayout = QVBoxLayout(self.link_props)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.name_label = QLabel(self.link_props)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.link_name = QLabel(self.link_props)
        self.link_name.setObjectName(u"link_name")
        self.link_name.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.link_name, 0, 1, 1, 1)

        self.parent_label = QLabel(self.link_props)
        self.parent_label.setObjectName(u"parent_label")

        self.gridLayout.addWidget(self.parent_label, 1, 0, 1, 1)

        self.parent = QLabel(self.link_props)
        self.parent.setObjectName(u"parent")
        self.parent.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.parent, 1, 1, 1, 1)

        self.child_label = QLabel(self.link_props)
        self.child_label.setObjectName(u"child_label")

        self.gridLayout.addWidget(self.child_label, 2, 0, 1, 1)

        self.child = QLabel(self.link_props)
        self.child.setObjectName(u"child")
        self.child.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.child, 2, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.material_label = QLabel(self.link_props)
        self.material_label.setObjectName(u"material_label")

        self.horizontalLayout_2.addWidget(self.material_label)

        self.material = QLabel(self.link_props)
        self.material.setObjectName(u"material")

        self.horizontalLayout_2.addWidget(self.material)

        self.material_selection = QPushButton(self.link_props)
        self.material_selection.setObjectName(u"material_selection")
        self.material_selection.setMaximumSize(QSize(40, 30))

        self.horizontalLayout_2.addWidget(self.material_selection)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.density_label = QLabel(self.link_props)
        self.density_label.setObjectName(u"density_label")

        self.horizontalLayout_4.addWidget(self.density_label)

        self.density = QLabel(self.link_props)
        self.density.setObjectName(u"density")

        self.horizontalLayout_4.addWidget(self.density)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 157, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.link_props)

        self.verticalLayout_2.addWidget(self.splitter)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Apply_btn = QPushButton(urdf)
        self.Apply_btn.setObjectName(u"Apply_btn")

        self.horizontalLayout.addWidget(self.Apply_btn)

        self.buttonBox = QDialogButtonBox(urdf)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(urdf)
        self.buttonBox.accepted.connect(urdf.accept)
        self.buttonBox.rejected.connect(urdf.reject)

        QMetaObject.connectSlotsByName(urdf)
    # setupUi

    def retranslateUi(self, urdf):
        urdf.setWindowTitle(QCoreApplication.translate("urdf", u"assemble", None))
        self.link_props.setTitle(QCoreApplication.translate("urdf", u"link properties", None))
        self.name_label.setText(QCoreApplication.translate("urdf", u"name", None))
        self.link_name.setText(QCoreApplication.translate("urdf", u"link name", None))
        self.parent_label.setText(QCoreApplication.translate("urdf", u"Parent", None))
        self.parent.setText(QCoreApplication.translate("urdf", u"world", None))
        self.child_label.setText(QCoreApplication.translate("urdf", u"child", None))
        self.child.setText(QCoreApplication.translate("urdf", u"None", None))
        self.material_label.setText(QCoreApplication.translate("urdf", u"Material name", None))
        self.material.setText(QCoreApplication.translate("urdf", u"carbon", None))
        self.material_selection.setText(QCoreApplication.translate("urdf", u"...", None))
        self.density_label.setText(QCoreApplication.translate("urdf", u"density", None))
        self.density.setText(QCoreApplication.translate("urdf", u"2700", None))
        self.Apply_btn.setText(QCoreApplication.translate("urdf", u"Apply", None))
    # retranslateUi

