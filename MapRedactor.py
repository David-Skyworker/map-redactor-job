from UI.UI_Main import Ui_MainWindow
from UI.UI_RcSettings import Ui_RcDialog
from UI.UI_IndSettings import Ui_IndSettings
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

import sys
import os
from libs import config
from libs.thread_handlers import ReadHandler, GenHandler


class IndWindow(QDialog, Ui_IndSettings):
    """
        Виджет-диалог, предназначенный для объявления идентификаторов перегона.

    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # ссылки и имена настроек индикаторов
        self.names = ["ОТПР", "ИП1", "ИП2", "КП", "БП", "КК", "БИП1", "БИП2", "ИП3"]
        self.links = [self.checkIndDepartureBox,
                      self.checkIndOncomingBox_1,
                      self.checkIndOncomingBox_2,
                      self.checkIndOccupationBox_1,
                      self.checkIndOccupationBox_2,
                      self.checkIndKKBox,
                      self.checkIndDistanceBox_1,
                      self.checkIndDistanceBox_2,
                      self.checkIndOncomingBox_3]

        # загрузка данных
        self.load_settings()

        # подключение функций для нажатых кнопок
        self.buttonIndBox.accepted.connect(self.push_accept_button)
        self.buttonIndBox.rejected.connect(self.push_reject_button)

        self.show()

    def load_settings(self):
        if "ind" in config.details:
            for i, val in enumerate(config.details["ind"].values()):
                self.links[i].setChecked(val)

    def push_reject_button(self):
        self.close()

    def push_accept_button(self):
        # сохранение настроек индекаторов
        indicators = {name: checkbox.isChecked() for name, checkbox in zip(self.names, self.links)}
        print(indicators)
        config.details["ind"] = indicators

        self.close()


class RcWindow(QDialog, Ui_RcDialog):
    """
        Виджет-диалог, предназначенный для более детальной настройки рельсовых цепей.

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
        self.rc_num = int(rc_num)

        # кастомизация таблицы
        self.tableWidget.setColumnWidth(0, 125)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setRowCount(self.rc_num)

        # подключение функций для нажатых кнопок
        self.buttonBox.accepted.connect(self.push_accept_button)
        self.buttonBox.rejected.connect(self.push_reject_button)

        if len(config.details["rc"]) == self.rc_num:
            self.load_data()
        else:
            self.set_data(self.rc_num, width)

        # show the window
        self.show()

    def push_reject_button(self):
        self.close()

    def push_accept_button(self):
        data = {}
        for i in range(0, self.rc_num):
            data[self.tableWidget.item(i, 0).text()] = self.tableWidget.item(i, 1).text()

        config.details["rc"] = data
        self.close()

    def load_data(self):
            # настройки РЦ уже сохранены в config, выводим
            for i, (name, width) in enumerate(config.details["rc"].items()):
                self.tableWidget.setItem(i, 0, QTableWidgetItem(name))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(width))

    def set_new_data(self, num, width):
            # первое РЦ
            self.tableWidget.setItem(0, 0, QTableWidgetItem("НАЧАЛО"))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(width))

            # цикл вывода внутренних РЦ перегона
            for i in range(num - 2):
                name = self.letter + str(i * 2 + self.val) + 'П'

                self.tableWidget.setItem(i + 1, 0, QTableWidgetItem(name))
                self.tableWidget.setItem(i + 1, 1, QTableWidgetItem(width))

            # конечное РЦ
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
        self.setButtonInd.clicked.connect(self.push_set_ind)
    # ---------------------------------------------------------------------

    def calc_start_coordinates(self):
        x = int(self.spinBoxAbscissa.value())
        direct = self.comboBoxDirect.currentIndex()

        # при напралении слева направо - установить коорд., заданные пользователем
        if direct == 0:
            return x

        # при обратном направелении высчитать необходимый сдвиг начала коорд.
        elif direct == 1:
            print("in")
            # данные о ширине были изменены вручную
            rc_num = int(self.numRcText.text())
            if "rc" in config.details == rc_num:
                rc_shift = sum([w for w in config.details["rc"].values()])
            # все РЦ равны по ширине
            else:
                width = int(self.widthRcText.text())
                rc_shift = rc_num * width

            shifted_x = x + rc_shift
            print(shifted_x)
            return shifted_x

    def push_read_button(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(caption="Open File", filter="Config Files (*.ini)")
        if file_name != "":
            config.file_data = None
            file_name = file_name.replace('/', '\\')
            ReadHandler(file_name).start()

    def push_generate_button(self):
        if config.file_path == "":
            return

        coordinates = (self.calc_start_coordinates(), int(self.spinBoxOrdinate.value()))
        reserved = self.checkBoxReserv.isChecked()
        direct = self.comboBoxDirect.currentIndex()
        set_num = self.numSetText.text()

        # общая ифнформация о перегоне, считанная из пользовательского интерфейса
        general_info = {"coordinates": coordinates,
                        "reserved": reserved,
                        "direct": direct,
                        "set_num": set_num,
                        "interface": self.comboInterfaceRc.currentIndex(),
                      "indicator_arrow_margin": int(self.marginArrowText.text())}

        # ифнформация об РЦ, считанная из пользовательского интерфейса
        rc_info = {"num": int(self.numRcText.text()),
                   "height": self.heightRcText.text(),
                   "width": self.widthRcText.text(),
                   "first_rc_name": self.comboNameRc.currentText(),
                   "join_start_rc": self.comboBoxContr.currentIndex()}

        # ифнформация об МКРЦ, считанная из пользовательского интерфейса
        control_info = {"num": int(self.numContrText.text()),
                        "height": self.heightContrText.text(),
                        "width": self.widthContrText.text(),
                        "upper_margin": int(self.marginContrText.text()),
                        "start_rc": self.comboBoxContr.currentIndex()}

        # ифнформация об МГКС, считанная из пользовательского интерфейса
        gen_info = {"num": int(self.numGenText.text()),
                    "height": self.heightGenText.text(),
                    "width": self.widthGenText.text(),
                    "upper_margin": int(self.marginGenText.text()),
                    "start_rc": self.comboBoxGen.currentIndex(),
                    "pattern": self.comboBoxGenPattern.currentIndex()}

        # ифнформация об УКСПС, считанная из пользовательского интерфейса
        uksps_info = {"num": self.numRcText.text(),
                      "height": self.heightUkspsText.text(),
                      "width": int(self.widthUkspsText.text())}

        # ифнформация об стрелке направления, считанная из пользовательского интерфейса
        arrow_info = {"exists": self.checkBoxArrow.isChecked(),
                      "height": self.heightArrowText.text(),
                      "width": self.widthArrowText.text()}

        # ифнформация об индификаторах, считанная из пользовательского интерфейса
        ind_info = {"height": self.heightIndText.text(),
                    "width": self.widthIndText.text()}

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

    def push_set_ind(self):
        dialog = IndWindow()
        dialog.exec_()

    def push_select_button(self):
        print("any button pushed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    app.exec_()
