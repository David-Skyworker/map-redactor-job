# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 761, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.Tab1 = QtWidgets.QWidget()
        self.Tab1.setObjectName("Tab1")
        self.groupBox = QtWidgets.QGroupBox(self.Tab1)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 581, 451))
        self.groupBox.setMouseTracking(True)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 171, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.numRcText = QtWidgets.QLineEdit(self.groupBox_2)
        self.numRcText.setGeometry(QtCore.QRect(100, 20, 40, 20))
        self.numRcText.setMouseTracking(False)
        self.numRcText.setAlignment(QtCore.Qt.AlignCenter)
        self.numRcText.setObjectName("numRcText")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 90, 20))
        self.label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 90, 20))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 50, 40, 20))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.heightRcText = QtWidgets.QLineEdit(self.groupBox_2)
        self.heightRcText.setGeometry(QtCore.QRect(100, 50, 40, 20))
        self.heightRcText.setAlignment(QtCore.Qt.AlignCenter)
        self.heightRcText.setObjectName("heightRcText")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 80, 90, 20))
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.widthRcText = QtWidgets.QLineEdit(self.groupBox_2)
        self.widthRcText.setGeometry(QtCore.QRect(100, 80, 40, 20))
        self.widthRcText.setAlignment(QtCore.Qt.AlignCenter)
        self.widthRcText.setObjectName("widthRcText")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 30, 20))
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.spinBoxAbscissa = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxAbscissa.setGeometry(QtCore.QRect(40, 210, 50, 20))
        self.spinBoxAbscissa.setMaximum(2000)
        self.spinBoxAbscissa.setObjectName("spinBoxAbscissa")
        self.spinBoxOrdinate = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxOrdinate.setGeometry(QtCore.QRect(90, 210, 50, 20))
        self.spinBoxOrdinate.setMaximum(2000)
        self.spinBoxOrdinate.setObjectName("spinBoxOrdinate")
        self.setButtonRc = QtWidgets.QPushButton(self.groupBox_2)
        self.setButtonRc.setGeometry(QtCore.QRect(10, 110, 75, 20))
        self.setButtonRc.setObjectName("setButtonRc")
        self.line_4 = QtWidgets.QFrame(self.groupBox_2)
        self.line_4.setGeometry(QtCore.QRect(10, 190, 118, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_92 = QtWidgets.QLabel(self.groupBox_2)
        self.label_92.setGeometry(QtCore.QRect(10, 190, 101, 16))
        self.label_92.setObjectName("label_92")
        self.comboNameRc = QtWidgets.QComboBox(self.groupBox_2)
        self.comboNameRc.setGeometry(QtCore.QRect(95, 140, 45, 20))
        self.comboNameRc.setObjectName("comboNameRc")
        self.comboNameRc.addItem("")
        self.comboNameRc.addItem("")
        self.comboNameRc.addItem("")
        self.comboNameRc.addItem("")
        self.label_52 = QtWidgets.QLabel(self.groupBox_2)
        self.label_52.setGeometry(QtCore.QRect(12, 140, 85, 20))
        self.label_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_52.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 20, 161, 241))
        self.groupBox_3.setObjectName("groupBox_3")
        self.numGenText = QtWidgets.QLineEdit(self.groupBox_3)
        self.numGenText.setGeometry(QtCore.QRect(100, 20, 40, 20))
        self.numGenText.setAlignment(QtCore.Qt.AlignCenter)
        self.numGenText.setObjectName("numGenText")
        self.heightGenText = QtWidgets.QLineEdit(self.groupBox_3)
        self.heightGenText.setGeometry(QtCore.QRect(100, 50, 40, 20))
        self.heightGenText.setAlignment(QtCore.Qt.AlignCenter)
        self.heightGenText.setObjectName("heightGenText")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 90, 20))
        self.label_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 90, 20))
        self.label_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.widthGenText = QtWidgets.QLineEdit(self.groupBox_3)
        self.widthGenText.setGeometry(QtCore.QRect(100, 80, 40, 20))
        self.widthGenText.setAlignment(QtCore.Qt.AlignCenter)
        self.widthGenText.setObjectName("widthGenText")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(10, 80, 90, 20))
        self.label_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_17.setObjectName("label_17")
        self.comboBoxGenPattern = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBoxGenPattern.setGeometry(QtCore.QRect(10, 210, 130, 22))
        self.comboBoxGenPattern.setObjectName("comboBoxGenPattern")
        self.comboBoxGenPattern.addItem("")
        self.comboBoxGenPattern.addItem("")
        self.label_36 = QtWidgets.QLabel(self.groupBox_3)
        self.label_36.setGeometry(QtCore.QRect(10, 180, 90, 20))
        self.label_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_36.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.comboBoxGen = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBoxGen.setGeometry(QtCore.QRect(100, 180, 40, 20))
        self.comboBoxGen.setObjectName("comboBoxGen")
        self.comboBoxGen.addItem("")
        self.comboBoxGen.addItem("")
        self.line_3 = QtWidgets.QFrame(self.groupBox_3)
        self.line_3.setGeometry(QtCore.QRect(10, 130, 118, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.marginGenText = QtWidgets.QLineEdit(self.groupBox_3)
        self.marginGenText.setGeometry(QtCore.QRect(100, 150, 40, 20))
        self.marginGenText.setAlignment(QtCore.Qt.AlignCenter)
        self.marginGenText.setObjectName("marginGenText")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(10, 150, 90, 20))
        self.label_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_22.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(390, 20, 161, 241))
        self.groupBox_4.setObjectName("groupBox_4")
        self.numContrText = QtWidgets.QLineEdit(self.groupBox_4)
        self.numContrText.setGeometry(QtCore.QRect(100, 20, 40, 20))
        self.numContrText.setAlignment(QtCore.Qt.AlignCenter)
        self.numContrText.setObjectName("numContrText")
        self.heightContrText = QtWidgets.QLineEdit(self.groupBox_4)
        self.heightContrText.setGeometry(QtCore.QRect(100, 50, 40, 20))
        self.heightContrText.setAlignment(QtCore.Qt.AlignCenter)
        self.heightContrText.setObjectName("heightContrText")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(10, 50, 90, 20))
        self.label_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 90, 20))
        self.label_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.widthContrText = QtWidgets.QLineEdit(self.groupBox_4)
        self.widthContrText.setGeometry(QtCore.QRect(100, 80, 40, 20))
        self.widthContrText.setAlignment(QtCore.Qt.AlignCenter)
        self.widthContrText.setObjectName("widthContrText")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(10, 80, 90, 20))
        self.label_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_20.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(10, 130, 101, 16))
        self.label_21.setObjectName("label_21")
        self.comboBoxContr = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBoxContr.setGeometry(QtCore.QRect(98, 180, 40, 20))
        self.comboBoxContr.setObjectName("comboBoxContr")
        self.comboBoxContr.addItem("")
        self.comboBoxContr.addItem("")
        self.label_37 = QtWidgets.QLabel(self.groupBox_4)
        self.label_37.setGeometry(QtCore.QRect(10, 180, 90, 20))
        self.label_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_37.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.line = QtWidgets.QFrame(self.groupBox_4)
        self.line.setGeometry(QtCore.QRect(10, 130, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.marginContrText = QtWidgets.QLineEdit(self.groupBox_4)
        self.marginContrText.setGeometry(QtCore.QRect(100, 150, 40, 20))
        self.marginContrText.setAlignment(QtCore.Qt.AlignCenter)
        self.marginContrText.setObjectName("marginContrText")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(10, 150, 90, 20))
        self.label_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_23.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 270, 171, 171))
        self.groupBox_13.setObjectName("groupBox_13")
        self.widthUkspsText = QtWidgets.QLineEdit(self.groupBox_13)
        self.widthUkspsText.setGeometry(QtCore.QRect(100, 50, 40, 20))
        self.widthUkspsText.setAlignment(QtCore.Qt.AlignCenter)
        self.widthUkspsText.setObjectName("widthUkspsText")
        self.label_50 = QtWidgets.QLabel(self.groupBox_13)
        self.label_50.setGeometry(QtCore.QRect(10, 50, 90, 20))
        self.label_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_50.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.heightUkspsText = QtWidgets.QLineEdit(self.groupBox_13)
        self.heightUkspsText.setGeometry(QtCore.QRect(100, 20, 40, 20))
        self.heightUkspsText.setAlignment(QtCore.Qt.AlignCenter)
        self.heightUkspsText.setObjectName("heightUkspsText")
        self.label_51 = QtWidgets.QLabel(self.groupBox_13)
        self.label_51.setGeometry(QtCore.QRect(10, 20, 90, 20))
        self.label_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_51.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.setButtonUksps = QtWidgets.QPushButton(self.groupBox_13)
        self.setButtonUksps.setGeometry(QtCore.QRect(10, 80, 75, 20))
        self.setButtonUksps.setObjectName("setButtonUksps")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_6.setGeometry(QtCore.QRect(200, 270, 351, 171))
        self.groupBox_6.setObjectName("groupBox_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 20, 161, 81))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_38 = QtWidgets.QLabel(self.groupBox_5)
        self.label_38.setGeometry(QtCore.QRect(10, 20, 90, 20))
        self.label_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_38.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.heightArrowText = QtWidgets.QLineEdit(self.groupBox_5)
        self.heightArrowText.setGeometry(QtCore.QRect(100, 20, 40, 20))
        self.heightArrowText.setAlignment(QtCore.Qt.AlignCenter)
        self.heightArrowText.setObjectName("heightArrowText")
        self.widthArrowText = QtWidgets.QLineEdit(self.groupBox_5)
        self.widthArrowText.setGeometry(QtCore.QRect(100, 50, 40, 20))
        self.widthArrowText.setAlignment(QtCore.Qt.AlignCenter)
        self.widthArrowText.setObjectName("widthArrowText")
        self.label_39 = QtWidgets.QLabel(self.groupBox_5)
        self.label_39.setGeometry(QtCore.QRect(10, 50, 90, 20))
        self.label_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_39.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.checkBoxArrow = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBoxArrow.setGeometry(QtCore.QRect(90, 0, 70, 17))
        self.checkBoxArrow.setText("")
        self.checkBoxArrow.setChecked(True)
        self.checkBoxArrow.setObjectName("checkBoxArrow")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_9.setGeometry(QtCore.QRect(190, 20, 161, 111))
        self.groupBox_9.setObjectName("groupBox_9")
        self.widthIndText = QtWidgets.QLineEdit(self.groupBox_9)
        self.widthIndText.setGeometry(QtCore.QRect(100, 50, 40, 20))
        self.widthIndText.setAlignment(QtCore.Qt.AlignCenter)
        self.widthIndText.setObjectName("widthIndText")
        self.label_40 = QtWidgets.QLabel(self.groupBox_9)
        self.label_40.setGeometry(QtCore.QRect(10, 50, 90, 20))
        self.label_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_40.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.heightIndText = QtWidgets.QLineEdit(self.groupBox_9)
        self.heightIndText.setGeometry(QtCore.QRect(100, 20, 40, 20))
        self.heightIndText.setAlignment(QtCore.Qt.AlignCenter)
        self.heightIndText.setObjectName("heightIndText")
        self.label_42 = QtWidgets.QLabel(self.groupBox_9)
        self.label_42.setGeometry(QtCore.QRect(10, 20, 90, 20))
        self.label_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_42.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.setButtonInd = QtWidgets.QPushButton(self.groupBox_9)
        self.setButtonInd.setGeometry(QtCore.QRect(10, 80, 75, 20))
        self.setButtonInd.setObjectName("setButtonInd")
        self.marginArrowText = QtWidgets.QLineEdit(self.groupBox_6)
        self.marginArrowText.setGeometry(QtCore.QRect(110, 140, 40, 20))
        self.marginArrowText.setAlignment(QtCore.Qt.AlignCenter)
        self.marginArrowText.setObjectName("marginArrowText")
        self.line_5 = QtWidgets.QFrame(self.groupBox_6)
        self.line_5.setGeometry(QtCore.QRect(20, 120, 118, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_49 = QtWidgets.QLabel(self.groupBox_6)
        self.label_49.setGeometry(QtCore.QRect(20, 140, 90, 20))
        self.label_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_49.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_49.setAlignment(QtCore.Qt.AlignCenter)
        self.label_49.setObjectName("label_49")
        self.label_24 = QtWidgets.QLabel(self.groupBox_6)
        self.label_24.setGeometry(QtCore.QRect(20, 120, 101, 16))
        self.label_24.setObjectName("label_24")
        self.groupBox_16 = QtWidgets.QGroupBox(self.Tab1)
        self.groupBox_16.setGeometry(QtCore.QRect(590, 10, 151, 161))
        self.groupBox_16.setObjectName("groupBox_16")
        self.comboBoxDirect = QtWidgets.QComboBox(self.groupBox_16)
        self.comboBoxDirect.setGeometry(QtCore.QRect(10, 100, 130, 22))
        self.comboBoxDirect.setObjectName("comboBoxDirect")
        self.comboBoxDirect.addItem("")
        self.comboBoxDirect.addItem("")
        self.numSetText = QtWidgets.QLineEdit(self.groupBox_16)
        self.numSetText.setGeometry(QtCore.QRect(100, 20, 40, 20))
        self.numSetText.setAlignment(QtCore.Qt.AlignCenter)
        self.numSetText.setObjectName("numSetText")
        self.label_16 = QtWidgets.QLabel(self.groupBox_16)
        self.label_16.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_16.setObjectName("label_16")
        self.label_14 = QtWidgets.QLabel(self.groupBox_16)
        self.label_14.setGeometry(QtCore.QRect(10, 20, 90, 20))
        self.label_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.checkBoxReserv = QtWidgets.QCheckBox(self.groupBox_16)
        self.checkBoxReserv.setGeometry(QtCore.QRect(10, 50, 111, 17))
        self.checkBoxReserv.setObjectName("checkBoxReserv")
        self.comboInterfaceRc = QtWidgets.QComboBox(self.groupBox_16)
        self.comboInterfaceRc.setGeometry(QtCore.QRect(80, 130, 60, 20))
        self.comboInterfaceRc.setObjectName("comboInterfaceRc")
        self.comboInterfaceRc.addItem("")
        self.comboInterfaceRc.addItem("")
        self.label_53 = QtWidgets.QLabel(self.groupBox_16)
        self.label_53.setGeometry(QtCore.QRect(10, 130, 70, 20))
        self.label_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_53.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Tab1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(590, 180, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.openButtonAdd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openButtonAdd.setObjectName("openButtonAdd")
        self.verticalLayout.addWidget(self.openButtonAdd)
        self.generateButtonAdd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.generateButtonAdd.setObjectName("generateButtonAdd")
        self.verticalLayout.addWidget(self.generateButtonAdd)
        self.tabWidget.addTab(self.Tab1, "")
        self.Tab2 = QtWidgets.QWidget()
        self.Tab2.setObjectName("Tab2")
        self.tabWidget.addTab(self.Tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.menuFile.addAction(self.action)
        self.menuFile.addAction(self.action_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_4)
        self.menuFile.addAction(self.action_6)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MapRedactor"))
        self.groupBox.setTitle(_translate("MainWindow", "Настройка элемиентов пути"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Рельсовые цепи"))
        self.numRcText.setText(_translate("MainWindow", "2"))
        self.label.setText(_translate("MainWindow", "Количество:"))
        self.label_2.setText(_translate("MainWindow", "Высота :"))
        self.lineEdit_2.setText(_translate("MainWindow", "0"))
        self.heightRcText.setText(_translate("MainWindow", "20"))
        self.label_5.setText(_translate("MainWindow", "Ширина :"))
        self.widthRcText.setText(_translate("MainWindow", "40"))
        self.label_6.setText(_translate("MainWindow", "X,Y:"))
        self.setButtonRc.setText(_translate("MainWindow", "Настроить"))
        self.label_92.setText(_translate("MainWindow", "Расположение"))
        self.comboNameRc.setItemText(0, _translate("MainWindow", "Ч1П"))
        self.comboNameRc.setItemText(1, _translate("MainWindow", "Ч2П"))
        self.comboNameRc.setItemText(2, _translate("MainWindow", "Н1П"))
        self.comboNameRc.setItemText(3, _translate("MainWindow", "Н2П"))
        self.label_52.setText(_translate("MainWindow", "Наим. 1-го РЦ :"))
        self.groupBox_3.setTitle(_translate("MainWindow", "МГКС"))
        self.numGenText.setText(_translate("MainWindow", "0"))
        self.heightGenText.setText(_translate("MainWindow", "20"))
        self.label_7.setText(_translate("MainWindow", "Высота :"))
        self.label_13.setText(_translate("MainWindow", "Количество:"))
        self.widthGenText.setText(_translate("MainWindow", "20"))
        self.label_15.setText(_translate("MainWindow", "Ширина :"))
        self.label_17.setText(_translate("MainWindow", "Расположение"))
        self.comboBoxGenPattern.setItemText(0, _translate("MainWindow", "через одну РЦ"))
        self.comboBoxGenPattern.setItemText(1, _translate("MainWindow", "подряд"))
        self.label_36.setText(_translate("MainWindow", "Первое РЦ :"))
        self.comboBoxGen.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxGen.setItemText(1, _translate("MainWindow", "2"))
        self.marginGenText.setText(_translate("MainWindow", "5"))
        self.label_22.setText(_translate("MainWindow", "Отступ от РЦ :"))
        self.groupBox_4.setTitle(_translate("MainWindow", "МКРЦ"))
        self.numContrText.setText(_translate("MainWindow", "0"))
        self.heightContrText.setText(_translate("MainWindow", "20"))
        self.label_18.setText(_translate("MainWindow", "Высота :"))
        self.label_19.setText(_translate("MainWindow", "Количество:"))
        self.widthContrText.setText(_translate("MainWindow", "20"))
        self.label_20.setText(_translate("MainWindow", "Ширина :"))
        self.label_21.setText(_translate("MainWindow", "Расположение"))
        self.comboBoxContr.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxContr.setItemText(1, _translate("MainWindow", "2"))
        self.label_37.setText(_translate("MainWindow", "Стартовое РЦ :"))
        self.marginContrText.setText(_translate("MainWindow", "5"))
        self.label_23.setText(_translate("MainWindow", "Отступ от РЦ :"))
        self.groupBox_13.setTitle(_translate("MainWindow", "УКСПС"))
        self.widthUkspsText.setText(_translate("MainWindow", "50"))
        self.label_50.setText(_translate("MainWindow", "Ширина :"))
        self.heightUkspsText.setText(_translate("MainWindow", "50"))
        self.label_51.setText(_translate("MainWindow", "Высота :"))
        self.setButtonUksps.setText(_translate("MainWindow", "Настроить"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Список реле"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Стрелка напрв."))
        self.label_38.setText(_translate("MainWindow", "Высота :"))
        self.heightArrowText.setText(_translate("MainWindow", "50"))
        self.widthArrowText.setText(_translate("MainWindow", "50"))
        self.label_39.setText(_translate("MainWindow", "Ширина :"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Индикаторы"))
        self.widthIndText.setText(_translate("MainWindow", "50"))
        self.label_40.setText(_translate("MainWindow", "Ширина :"))
        self.heightIndText.setText(_translate("MainWindow", "50"))
        self.label_42.setText(_translate("MainWindow", "Высота :"))
        self.setButtonInd.setText(_translate("MainWindow", "Настроить"))
        self.marginArrowText.setText(_translate("MainWindow", "50"))
        self.label_49.setText(_translate("MainWindow", "Отступ от РЦ :"))
        self.label_24.setText(_translate("MainWindow", "Располож."))
        self.groupBox_16.setTitle(_translate("MainWindow", "Общее"))
        self.comboBoxDirect.setItemText(0, _translate("MainWindow", "слева направо  →"))
        self.comboBoxDirect.setItemText(1, _translate("MainWindow", "справа налево  ←"))
        self.numSetText.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Направление"))
        self.label_14.setText(_translate("MainWindow", "№ комплекта:"))
        self.checkBoxReserv.setText(_translate("MainWindow", "Резервирование"))
        self.comboInterfaceRc.setItemText(0, _translate("MainWindow", "Релей."))
        self.comboInterfaceRc.setItemText(1, _translate("MainWindow", "Цифр."))
        self.label_53.setText(_translate("MainWindow", "Интерфейс :"))
        self.openButtonAdd.setText(_translate("MainWindow", "Открыть"))
        self.generateButtonAdd.setText(_translate("MainWindow", "Сгенерировать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), _translate("MainWindow", "Дополнение карты"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab2), _translate("MainWindow", "Редактирование карты"))
        self.menuFile.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Открыть"))
        self.action_2.setText(_translate("MainWindow", "Обновить"))
        self.action_4.setText(_translate("MainWindow", "Сохранить"))
        self.action_6.setText(_translate("MainWindow", "Сохранить как..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
