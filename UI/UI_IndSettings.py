# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_IndSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IndSettings(object):
    def setupUi(self, IndSettings):
        IndSettings.setObjectName("IndSettings")
        IndSettings.resize(256, 238)
        IndSettings.setModal(True)
        self.buttonIndBox = QtWidgets.QDialogButtonBox(IndSettings)
        self.buttonIndBox.setGeometry(QtCore.QRect(0, 210, 261, 23))
        self.buttonIndBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonIndBox.setCenterButtons(True)
        self.buttonIndBox.setObjectName("buttonIndBox")
        self.groupBox = QtWidgets.QGroupBox(IndSettings)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 231, 191))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 211, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkIndOccupationBox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkIndOccupationBox_1.setObjectName("checkIndOccupationBox_1")
        self.gridLayout.addWidget(self.checkIndOccupationBox_1, 4, 0, 1, 1)
        self.checkIndOccupationBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkIndOccupationBox_2.setObjectName("checkIndOccupationBox_2")
        self.gridLayout.addWidget(self.checkIndOccupationBox_2, 4, 2, 1, 1)
        self.checkIndKKBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkIndKKBox.setObjectName("checkIndKKBox")
        self.gridLayout.addWidget(self.checkIndKKBox, 6, 0, 1, 1)
        self.checkIndDistanceBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkIndDistanceBox_2.setObjectName("checkIndDistanceBox_2")
        self.gridLayout.addWidget(self.checkIndDistanceBox_2, 8, 2, 1, 1)
        self.checkIndDistanceBox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkIndDistanceBox_1.setObjectName("checkIndDistanceBox_1")
        self.gridLayout.addWidget(self.checkIndDistanceBox_1, 8, 0, 1, 1)
        self.checkIndOncomingBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkIndOncomingBox_3.setObjectName("checkIndOncomingBox_3")
        self.gridLayout.addWidget(self.checkIndOncomingBox_3, 2, 4, 1, 1)
        self.checkIndOncomingBox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkIndOncomingBox_1.setObjectName("checkIndOncomingBox_1")
        self.gridLayout.addWidget(self.checkIndOncomingBox_1, 2, 0, 1, 1)
        self.checkIndOncomingBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkIndOncomingBox_2.setObjectName("checkIndOncomingBox_2")
        self.gridLayout.addWidget(self.checkIndOncomingBox_2, 2, 2, 1, 1)
        self.checkIndDepartureBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkIndDepartureBox.setObjectName("checkIndDepartureBox")
        self.gridLayout.addWidget(self.checkIndDepartureBox, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 5)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 5)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 5)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 7, 0, 1, 5)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 0, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 2, 1, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 2, 3, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 4, 1, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 4, 3, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 6, 1, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout.addWidget(self.line_11, 8, 1, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout.addWidget(self.line_12, 8, 3, 1, 1)

        self.retranslateUi(IndSettings)
        QtCore.QMetaObject.connectSlotsByName(IndSettings)

    def retranslateUi(self, IndSettings):
        _translate = QtCore.QCoreApplication.translate
        IndSettings.setWindowTitle(_translate("IndSettings", "Настройки индификаторов"))
        self.checkIndOccupationBox_1.setText(_translate("IndSettings", "КП"))
        self.checkIndOccupationBox_2.setText(_translate("IndSettings", "БП"))
        self.checkIndKKBox.setText(_translate("IndSettings", "КК"))
        self.checkIndDistanceBox_2.setText(_translate("IndSettings", "БИП2"))
        self.checkIndDistanceBox_1.setText(_translate("IndSettings", "БИП1"))
        self.checkIndOncomingBox_3.setText(_translate("IndSettings", "ИП3"))
        self.checkIndOncomingBox_1.setText(_translate("IndSettings", "ИП1"))
        self.checkIndOncomingBox_2.setText(_translate("IndSettings", "ИП2"))
        self.checkIndDepartureBox.setText(_translate("IndSettings", "ОТПР"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    IndSettings = QtWidgets.QDialog()
    ui = Ui_IndSettings()
    ui.setupUi(IndSettings)
    IndSettings.show()
    sys.exit(app.exec_())
