# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cell_item.ui'
#
# Created by: PyQt6 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CellWidget(object):
        def setupUi(self, CellWidget):
                CellWidget.setObjectName("CellWidget")
                CellWidget.resize(460, 329)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Preferred,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(CellWidget.sizePolicy().hasHeightForWidth())
                CellWidget.setSizePolicy(sizePolicy)
                self.verticalLayout = QtWidgets.QVBoxLayout(CellWidget)
                self.verticalLayout.setContentsMargins(6, 0, 6, 6)
                self.verticalLayout.setSpacing(0)
                self.verticalLayout.setObjectName("verticalLayout")
                self.addButton = HoverButton(CellWidget)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Preferred,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
                self.addButton.setSizePolicy(sizePolicy)
                self.addButton.setMinimumSize(QtCore.QSize(0, 64))
                self.addButton.setStyleSheet(
                        "#addButton {\n"
                        "    border: 1px solid rgba(134, 134, 134, 128);\n"
                        "    border-radius: 2px;\n"
                        "    background: transparent;\n"
                        "}"
                )
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../img/add_icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.addButton.setIcon(icon)
                self.addButton.setIconSize(QtCore.QSize(20, 20))
                self.addButton.setObjectName("addButton")
                self.verticalLayout.addWidget(self.addButton)
                self.mainFrame = QtWidgets.QFrame(CellWidget)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Ignored,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
                self.mainFrame.setSizePolicy(sizePolicy)
                self.mainFrame.setStyleSheet(
                        "#mainFrame {\n"
                        "    background: rgba(163, 163, 163, 5%);\n"
                        "    border-radius: 6px;\n"
                        "}"
                )
                self.mainFrame.setObjectName("mainFrame")
                self.gridLayout = QtWidgets.QGridLayout(self.mainFrame)
                self.gridLayout.setObjectName("gridLayout")
                self.titleColorButton = QtWidgets.QToolButton(self.mainFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.titleColorButton.sizePolicy().hasHeightForWidth())
                self.titleColorButton.setSizePolicy(sizePolicy)
                self.titleColorButton.setMaximumSize(QtCore.QSize(20, 20))
                self.titleColorButton.setStyleSheet(
                        "#titleColorButton {\n"
                        "    border-radius: 10px;\n"
                        "    background-color: #76bfb4;\n"
                        "    width: 20px;\n"
                        "}"
                )
                self.titleColorButton.setObjectName("titleColorButton")
                self.gridLayout.addWidget(self.titleColorButton, 0, 2, 1, 1)
                self.titleLineEdit = QtWidgets.QLineEdit(self.mainFrame)
                self.titleLineEdit.setObjectName("titleLineEdit")
                self.gridLayout.addWidget(self.titleLineEdit, 0, 1, 1, 1)
                self.titleLabel = QtWidgets.QLabel(self.mainFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
                self.titleLabel.setSizePolicy(sizePolicy)
                self.titleLabel.setMinimumSize(QtCore.QSize(82, 0))
                self.titleLabel.setStyleSheet(
                        "#mainFrame {\n"
                        "    background: rgba(163, 163, 163, 5%);\n"
                        "    border-radius: 6px;\n"
                        "}"
                )
                self.titleLabel.setObjectName("titleLabel")
                self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
                self.dragHandle = DragHandle(self.mainFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.dragHandle.sizePolicy().hasHeightForWidth())
                self.dragHandle.setSizePolicy(sizePolicy)
                self.dragHandle.setMaximumSize(QtCore.QSize(20, 20))
                self.dragHandle.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
                self.dragHandle.setMouseTracking(True)
                icon1 = QtGui.QIcon()
                icon1.addPixmap(QtGui.QPixmap("../img/vert_grip.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.dragHandle.setIcon(icon1)
                self.dragHandle.setObjectName("dragHandle")
                self.gridLayout.addWidget(self.dragHandle, 0, 4, 1, 1)
                self.expandoButton = RotateButton(self.mainFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.expandoButton.sizePolicy().hasHeightForWidth())
                self.expandoButton.setSizePolicy(sizePolicy)
                self.expandoButton.setMaximumSize(QtCore.QSize(20, 20))
                icon2 = QtGui.QIcon()
                icon2.addPixmap(
                        QtGui.QPixmap("../img/chevron_down.svg"),
                        QtGui.QIcon.Mode.Normal,
                        QtGui.QIcon.State.Off
                )
                self.expandoButton.setIcon(icon2)
                self.expandoButton.setIconSize(QtCore.QSize(20, 20))
                self.expandoButton.setObjectName("expandoButton")
                self.gridLayout.addWidget(self.expandoButton, 0, 3, 1, 1)
                self.expandFrame = QtWidgets.QFrame(self.mainFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Ignored,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.expandFrame.sizePolicy().hasHeightForWidth())
                self.expandFrame.setSizePolicy(sizePolicy)
                self.expandFrame.setObjectName("expandFrame")
                self.gridLayout_2 = QtWidgets.QGridLayout(self.expandFrame)
                self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
                self.gridLayout_2.setObjectName("gridLayout_2")
                self.startDayDropdown = QtWidgets.QComboBox(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.startDayDropdown.sizePolicy().hasHeightForWidth())
                self.startDayDropdown.setSizePolicy(sizePolicy)
                self.startDayDropdown.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
                self.startDayDropdown.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
                self.startDayDropdown.setObjectName("startDayDropdown")
                self.startDayDropdown.addItem("")
                self.startDayDropdown.addItem("")
                self.startDayDropdown.addItem("")
                self.startDayDropdown.addItem("")
                self.startDayDropdown.addItem("")
                self.startDayDropdown.addItem("")
                self.startDayDropdown.addItem("")
                self.gridLayout_2.addWidget(self.startDayDropdown, 3, 1, 1, 1)
                self.outputLineEdit = QtWidgets.QLineEdit(self.expandFrame)
                self.outputLineEdit.setObjectName("outputLineEdit")
                self.gridLayout_2.addWidget(self.outputLineEdit, 0, 1, 1, 1)
                self.outputColorButton = QtWidgets.QToolButton(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.outputColorButton.sizePolicy().hasHeightForWidth())
                self.outputColorButton.setSizePolicy(sizePolicy)
                self.outputColorButton.setMaximumSize(QtCore.QSize(20, 20))
                self.outputColorButton.setStyleSheet(
                        "#outputColorButton {\n"
                        "    border-radius: 10px;\n"
                        "    background-color: #FFF;\n"
                        "    width: 20px;\n"
                        "}"
                )
                self.outputColorButton.setObjectName("outputColorButton")
                self.gridLayout_2.addWidget(self.outputColorButton, 0, 2, 1, 1)
                self.frame = QtWidgets.QFrame(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Preferred
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
                self.frame.setSizePolicy(sizePolicy)
                self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame.setObjectName("frame")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.rangeDropdown = QtWidgets.QComboBox(self.frame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.rangeDropdown.sizePolicy().hasHeightForWidth())
                self.rangeDropdown.setSizePolicy(sizePolicy)
                self.rangeDropdown.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
                self.rangeDropdown.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
                self.rangeDropdown.setObjectName("rangeDropdown")
                self.rangeDropdown.addItem("")
                self.rangeDropdown.addItem("")
                self.rangeDropdown.addItem("")
                self.rangeDropdown.addItem("")
                self.rangeDropdown.addItem("")
                self.rangeDropdown.addItem("")
                self.horizontalLayout.addWidget(self.rangeDropdown)
                self.rangeExtraFrame = QtWidgets.QFrame(self.frame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.rangeExtraFrame.sizePolicy().hasHeightForWidth())
                self.rangeExtraFrame.setSizePolicy(sizePolicy)
                self.rangeExtraFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.rangeExtraFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.rangeExtraFrame.setObjectName("rangeExtraFrame")
                self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.rangeExtraFrame)
                self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_4.setSpacing(0)
                self.horizontalLayout_4.setObjectName("horizontalLayout_4")
                self.calendarCheckbox = QtWidgets.QCheckBox(self.rangeExtraFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Maximum,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.calendarCheckbox.sizePolicy().hasHeightForWidth())
                self.calendarCheckbox.setSizePolicy(sizePolicy)
                self.calendarCheckbox.setChecked(True)
                self.calendarCheckbox.setObjectName("calendarCheckbox")
                self.horizontalLayout_4.addWidget(self.calendarCheckbox)
                self.customRangeSpinbox = QtWidgets.QSpinBox(self.rangeExtraFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Maximum,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.customRangeSpinbox.sizePolicy().hasHeightForWidth())
                self.customRangeSpinbox.setSizePolicy(sizePolicy)
                self.customRangeSpinbox.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
                self.customRangeSpinbox.setMaximum(5690)
                self.customRangeSpinbox.setProperty("value", 7)
                self.customRangeSpinbox.setObjectName("customRangeSpinbox")
                self.horizontalLayout_4.addWidget(self.customRangeSpinbox)
                self.horizontalLayout.addWidget(self.rangeExtraFrame)
                self.gridLayout_2.addWidget(self.frame, 2, 1, 1, 1)
                self.directionFrame = QtWidgets.QFrame(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Maximum,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.directionFrame.sizePolicy().hasHeightForWidth())
                self.directionFrame.setSizePolicy(sizePolicy)
                self.directionFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.directionFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
                self.directionFrame.setObjectName("directionFrame")
                self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.directionFrame)
                self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_2.setSpacing(0)
                self.horizontalLayout_2.setObjectName("horizontalLayout_2")
                self.directionVerticalButton = QtWidgets.QPushButton(self.directionFrame)
                self.directionVerticalButton.setEnabled(False)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.directionVerticalButton.sizePolicy().hasHeightForWidth())
                self.directionVerticalButton.setSizePolicy(sizePolicy)
                self.directionVerticalButton.setMaximumSize(QtCore.QSize(42, 16777215))
                icon3 = QtGui.QIcon()
                icon3.addPixmap(QtGui.QPixmap("../img/vert_lines.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.directionVerticalButton.setIcon(icon3)
                self.directionVerticalButton.setObjectName("directionVerticalButton")
                self.horizontalLayout_2.addWidget(self.directionVerticalButton)
                self.directionHorizontalButton = QtWidgets.QPushButton(self.directionFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.directionHorizontalButton.sizePolicy().hasHeightForWidth())
                self.directionHorizontalButton.setSizePolicy(sizePolicy)
                self.directionHorizontalButton.setMaximumSize(QtCore.QSize(42, 16777215))
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("../img/horiz_lines.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.directionHorizontalButton.setIcon(icon4)
                self.directionHorizontalButton.setObjectName("directionHorizontalButton")
                self.horizontalLayout_2.addWidget(self.directionHorizontalButton)
                self.gridLayout_2.addWidget(self.directionFrame, 4, 1, 1, 1)
                self.frame_3 = QtWidgets.QFrame(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Preferred
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
                self.frame_3.setSizePolicy(sizePolicy)
                self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
                self.frame_3.setObjectName("frame_3")
                self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
                self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_3.setObjectName("horizontalLayout_3")
                self.hourLabel = QtWidgets.QLabel(self.frame_3)
                self.hourLabel.setObjectName("hourLabel")
                self.horizontalLayout_3.addWidget(self.hourLabel)
                self.hourEdit = QtWidgets.QLineEdit(self.frame_3)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.hourEdit.sizePolicy().hasHeightForWidth())
                self.hourEdit.setSizePolicy(sizePolicy)
                self.hourEdit.setObjectName("hourEdit")
                self.horizontalLayout_3.addWidget(self.hourEdit)
                self.minuteLabel = QtWidgets.QLabel(self.frame_3)
                self.minuteLabel.setObjectName("minuteLabel")
                self.horizontalLayout_3.addWidget(self.minuteLabel)
                self.minEdit = QtWidgets.QLineEdit(self.frame_3)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.minEdit.sizePolicy().hasHeightForWidth())
                self.minEdit.setSizePolicy(sizePolicy)
                self.minEdit.setObjectName("minEdit")
                self.horizontalLayout_3.addWidget(self.minEdit)
                self.gridLayout_2.addWidget(self.frame_3, 1, 1, 1, 1)
                self.directionLabel = QtWidgets.QLabel(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.directionLabel.sizePolicy().hasHeightForWidth())
                self.directionLabel.setSizePolicy(sizePolicy)
                self.directionLabel.setObjectName("directionLabel")
                self.gridLayout_2.addWidget(self.directionLabel, 4, 0, 1, 1)
                self.startDayLabel = QtWidgets.QLabel(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.startDayLabel.sizePolicy().hasHeightForWidth())
                self.startDayLabel.setSizePolicy(sizePolicy)
                self.startDayLabel.setObjectName("startDayLabel")
                self.gridLayout_2.addWidget(self.startDayLabel, 3, 0, 1, 1)
                self.rangeLabel = QtWidgets.QLabel(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.rangeLabel.sizePolicy().hasHeightForWidth())
                self.rangeLabel.setSizePolicy(sizePolicy)
                self.rangeLabel.setObjectName("rangeLabel")
                self.gridLayout_2.addWidget(self.rangeLabel, 2, 0, 1, 1)
                self.unitLabel = QtWidgets.QLabel(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.unitLabel.sizePolicy().hasHeightForWidth())
                self.unitLabel.setSizePolicy(sizePolicy)
                self.unitLabel.setObjectName("unitLabel")
                self.gridLayout_2.addWidget(self.unitLabel, 1, 0, 1, 1)
                self.outputLabel = QtWidgets.QLabel(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Maximum
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.outputLabel.sizePolicy().hasHeightForWidth())
                self.outputLabel.setSizePolicy(sizePolicy)
                self.outputLabel.setMinimumSize(QtCore.QSize(82, 0))
                self.outputLabel.setObjectName("outputLabel")
                self.gridLayout_2.addWidget(self.outputLabel, 0, 0, 1, 1)
                spacerItem = QtWidgets.QSpacerItem(
                        24,
                        0,
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Minimum
                )
                self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
                self.removeButton = HoverButton(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.removeButton.sizePolicy().hasHeightForWidth())
                self.removeButton.setSizePolicy(sizePolicy)
                self.removeButton.setMinimumSize(QtCore.QSize(0, 0))
                self.removeButton.setMaximumSize(QtCore.QSize(20, 20))
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("../img/remove_icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.removeButton.setIcon(icon5)
                self.removeButton.setIconSize(QtCore.QSize(20, 20))
                self.removeButton.setObjectName("removeButton")
                self.gridLayout_2.addWidget(self.removeButton, 0, 4, 1, 1)
                self.codeButton = HoverButton(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Fixed,
                        QtWidgets.QSizePolicy.Policy.Fixed
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.codeButton.sizePolicy().hasHeightForWidth())
                self.codeButton.setSizePolicy(sizePolicy)
                self.codeButton.setMinimumSize(QtCore.QSize(0, 0))
                self.codeButton.setMaximumSize(QtCore.QSize(20, 20))
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap("../img/code_icon.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
                self.codeButton.setIcon(icon6)
                self.codeButton.setIconSize(QtCore.QSize(20, 20))
                self.codeButton.setObjectName("codeButton")
                self.gridLayout_2.addWidget(self.codeButton, 4, 4, 1, 1)
                self.codeTextEdit = QtWidgets.QPlainTextEdit(self.expandFrame)
                sizePolicy = QtWidgets.QSizePolicy(
                        QtWidgets.QSizePolicy.Policy.Expanding,
                        QtWidgets.QSizePolicy.Policy.Preferred
                )
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.codeTextEdit.sizePolicy().hasHeightForWidth())
                self.codeTextEdit.setSizePolicy(sizePolicy)
                self.codeTextEdit.setMaximumSize(QtCore.QSize(16777215, 128))
                self.codeTextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
                self.codeTextEdit.setTabChangesFocus(False)
                self.codeTextEdit.setObjectName("codeTextEdit")
                self.gridLayout_2.addWidget(self.codeTextEdit, 5, 0, 1, 5)
                self.gridLayout.addWidget(self.expandFrame, 1, 0, 1, 5)
                self.verticalLayout.addWidget(self.mainFrame)

                self.retranslateUi(CellWidget)
                QtCore.QMetaObject.connectSlotsByName(CellWidget)

        def retranslateUi(self, CellWidget):
                _translate = QtCore.QCoreApplication.translate
                CellWidget.setWindowTitle(_translate("CellWidget", "Form"))
                self.titleColorButton.setToolTip(_translate("CellWidget", "Set a custom title text color."))
                self.titleLabel.setToolTip(
                        _translate("CellWidget", "Text that appears above or to-the-left-of the output.")
                )
                self.titleLabel.setText(_translate("CellWidget", "Title"))
                self.startDayDropdown.setToolTip(_translate("CellWidget", "The day a new week should start on."))
                self.startDayDropdown.setCurrentText(_translate("CellWidget", "Sunday"))
                self.startDayDropdown.setItemText(0, _translate("CellWidget", "Sunday"))
                self.startDayDropdown.setItemText(1, _translate("CellWidget", "Monday"))
                self.startDayDropdown.setItemText(2, _translate("CellWidget", "Tuesday"))
                self.startDayDropdown.setItemText(3, _translate("CellWidget", "Wednesday"))
                self.startDayDropdown.setItemText(4, _translate("CellWidget", "Thursday"))
                self.startDayDropdown.setItemText(5, _translate("CellWidget", "Friday"))
                self.startDayDropdown.setItemText(6, _translate("CellWidget", "Saturday"))
                self.outputColorButton.setToolTip(_translate("CellWidget", "Set a custom output text color."))
                self.rangeDropdown.setToolTip(
                        _translate("CellWidget", "Time range to filter through for the ranged total stat.")
                )
                self.rangeDropdown.setItemText(0, _translate("CellWidget", "Total"))
                self.rangeDropdown.setItemText(1, _translate("CellWidget", "Past Week"))
                self.rangeDropdown.setItemText(2, _translate("CellWidget", "Past 2 Weeks"))
                self.rangeDropdown.setItemText(3, _translate("CellWidget", "Past Month"))
                self.rangeDropdown.setItemText(4, _translate("CellWidget", "Past Year"))
                self.rangeDropdown.setItemText(5, _translate("CellWidget", "Custom"))
                self.calendarCheckbox.setToolTip(
                        _translate("CellWidget", "Use the start of the selected range instead of using its timespan.")
                )
                self.calendarCheckbox.setText(_translate("CellWidget", "Use Calendar Week"))
                self.customRangeSpinbox.setToolTip(
                        _translate("CellWidget", "Amount of days to filter the custom range.")
                )
                self.customRangeSpinbox.setSuffix(_translate("CellWidget", " days"))
                self.hourLabel.setText(_translate("CellWidget", "Hour"))
                self.hourEdit.setText(_translate("CellWidget", "hrs"))
                self.minuteLabel.setText(_translate("CellWidget", "Minute"))
                self.minEdit.setText(_translate("CellWidget", "min"))
                self.directionLabel.setToolTip(
                        _translate("CellWidget", "Set text-stacking direction to either vertical/horizontal.")
                )
                self.directionLabel.setText(_translate("CellWidget", "Direction"))
                self.startDayLabel.setToolTip(
                        _translate("CellWidget", "Day to consider the first day of a calendar week.")
                )
                self.startDayLabel.setText(_translate("CellWidget", "Week-Start Day"))
                self.rangeLabel.setToolTip(
                        _translate("CellWidget", "Preset range to use for macros with an expected range.")
                )
                self.rangeLabel.setText(_translate("CellWidget", "Selected Range"))
                self.unitLabel.setToolTip(
                        _translate(
                                "CellWidget",
                                "Text to be appended to any time-related measurements for all output text."
                        )
                )
                self.unitLabel.setText(_translate("CellWidget", "Units"))
                self.outputLabel.setToolTip(
                        _translate("CellWidget", "Text that appears below or to-the-right-of the title.")
                )
                self.outputLabel.setText(_translate("CellWidget", "Output"))


from .forms import DragHandle, HoverButton, RotateButton

if __name__ == "__main__":
        import sys

        app = QtWidgets.QApplication(sys.argv)
        CellWidget = QtWidgets.QWidget()
        ui = Ui_CellWidget()
        ui.setupUi(CellWidget)
        CellWidget.show()
        sys.exit(app.exec_())
