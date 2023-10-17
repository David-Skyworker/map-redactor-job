from UI.UI_Main import Ui_MainWindow
from UI.UI_RcSettings import Ui_RcDialog
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

import sys
import os
from libs import config
from libs.thread_handlers import ReadHandler, GenHandler


class RcWindow(QDialog, Ui_RcDialog):
    """
        Виджет-диалог предназначенный для более детальной настройки рельсовых цепей.

        ...
        Attributes
        -------
        rc_name: str
            первое наименование рельсовой цепи после станции, разъезда или блок-поста
        rc_num: int
            общее количество рельсовых цепей в перегоне
        width: str
            ширина рельсовой цепи установленная в главном окне

        """
    def __init__(self, rc_name, rc_num, width):
        super().__init__()
        self.setupUi(self)

        self.letter = rc_name[0]
        self.val = int(rc_name[1])
        self.way_num = int(rc_num)

        # кастомизация таблицы
        self.tableWidget.setColumnWidth(0, 125)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setRowCount(self.way_num)


        # подключение функций для нажатых кнопок
        self.buttonBox.accepted.connect(self.push_accept_button)
        self.buttonBox.rejected.connect(self.push_reject_button)

        self.set_data(self.way_num, width)

        # show the window
        self.show()

    def push_reject_button(self):
        self.close()

    def push_accept_button(self):
        data = {}
        for i in range(0, self.way_num):
            data[self.tableWidget.item(i, 0).text()] = self.tableWidget.item(i, 1).text()
        config.details["rc"] = data

        self.close()

    def set_data(self, num, width):
        self.tableWidget.setItem(0, 0, QTableWidgetItem("НАЧАЛО"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(width))

        for i in range(num - 2):
            name = self.letter + str(i * 2 + self.val) + 'П'

            self.tableWidget.setItem(i + 1, 0, QTableWidgetItem(name))
            self.tableWidget.setItem(i + 1, 1, QTableWidgetItem(width))

        self.tableWidget.setItem(num - 1, 0, QTableWidgetItem("КОНЕЦ"))
        self.tableWidget.setItem(num - 1, 1, QTableWidgetItem(width))


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # подключение функций для нажатых кнопок в части программы для генерации новых путей
        self.add_generate_action()

        # данные
        self.rc_widths = None

        # show the window
        self.show()

    # секция назначения кнопок
    # ---------------------------------------------------------------------
    def add_generate_action(self):
        self.setButtonRc.clicked.connect(self.push_set_rc)
        self.setButtonUksps.clicked.connect(self.push_select_button)
        self.openButtonAdd.clicked.connect(self.push_read_button)
        self.generateButtonAdd.clicked.connect(self.push_generate_button)
    # ---------------------------------------------------------------------

    def push_read_button(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(caption="Open File", filter="Config Files (*.ini)")
        if file_name != "":
            config.file_data = None
            file_name = file_name.replace('/', '\\')
            ReadHandler(file_name).start()

    def push_generate_button(self):
        if config.file_path == "":
            return

        coordinates = (self.spinBoxAbscissa.value(), self.spinBoxOrdinate.value())
        reserved = self.checkBoxReserv.isChecked()
        direct = self.comboBoxDirect.currentIndex()
        set_num = self.numSetText.text()

        # общая ифнформация о перегоне, считанная из пользовательского интерфейса
        general_info = {"coordinates": coordinates,
                        "reserved": reserved,
                        "direct": direct,
                        "set_num": set_num,
                        "interface": self.comboInterfaceRc.currentIndex()}

        # ифнформация об РЦ, считанная из пользовательского интерфейса
        rc_info = {"num": int(self.numRcText.text()),
                   "height": self.heightRcText.text(),
                   "width": self.widthRcText.text(),
                   "first_rc_name": self.comboNameRc.currentText()}

        # ифнформация об МГКС, считанная из пользовательского интерфейса
        gen_info = {"num": int(self.numGenText.text()),
                    "height": int(self.heightGenText.text()),
                    "width": int(self.widthGenText.text()),
                    "upper_margin": int(self.marginGenText.text()),
                    "start_rc": self.comboBoxGen.currentIndex(),
                    "patten": self.comboBoxGenPattern.currentIndex()}

        # ифнформация об МКРЦ, считанная из пользовательского интерфейса
        control_info = {"num": int(self.numContrText.text()),
                        "height": int(self.heightContrText.text()),
                        "width": int(self.widthContrText.text()),
                        "upper_margin": int(self.marginContrText.text()),
                        "start_rc": self.comboBoxContr.currentIndex()}

        # ифнформация об УКСПС, считанная из пользовательского интерфейса
        uksps_info = {"num": self.numRcText.text(),
                      "height": self.heightUkspsText.text(),
                      "width": int(self.widthUkspsText.text())}

        # ифнформация об стрелке направления, считанная из пользовательского интерфейса
        arrow_info = {"exists": self.checkBoxArrow.isChecked(),
                      "height": int(self.heightRcText.text()),
                      "width": int(self.widthRcText.text()),
                      "lower_margin": int(self.marginArrowText.text())}

        # ифнформация об индификаторах, считанная из пользовательского интерфейса
        ind_info = {"num": int(self.numIndText.text()),
                    "height": int(self.heightIndText.text()),
                    "width": int(self.widthIndText.text())}

        # ифнформация о перегоне
        info = {"general": general_info,
                "rc": rc_info,
                "mgks": gen_info,
                "mkrc": control_info,
                "uksps": uksps_info,
                "arrow": arrow_info,
                "ind": ind_info}

        GenHandler(info).start()




    def push_set_rc(self):
        name = self.comboNameRc.currentText()
        number = self.numRcText.text()
        width = self.widthRcText.text()

        dialog = RcWindow(name, number, width)
        dialog.exec_()


    def push_select_button(self):
        print("any button pushed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    app.exec_()
