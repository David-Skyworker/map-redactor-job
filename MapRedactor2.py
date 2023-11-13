from UI.UI_Main_2 import Ui_MainWindow
from UI.UI_RcSettings import Ui_RcDialog
from UI.UI_IndSettings import Ui_IndSettings
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog, QButtonGroup, QMessageBox
from PyQt5 import QtWidgets

import re
import sys
from libs import config
from libs.thread_handlers import ReadHandler, GenHandler
from libs.utilities import TableContent

MKRC_TAB_ID = 2
MGKS_TAB_ID = 3
UKSPS_TAB_ID = 4

NAME_CHOOSE_ID = 0
NAME_CUSTOM_ID = 1

INCREASE_MODE = 0
DECREASE_MODE = 1

RC_NAME_ID = 0
RC_WIDTH_ID = 1


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # поля для работы с данными интерфейса
        self.info = {"general": dict(),
                     "rc": dict(),
                     "mgks": dict(),
                     "mkrc": dict(),
                     "uksps": dict(),
                     "arrow": dict(),
                     "ind": dict()}

        # ----------------------------------------------------------------------
        # индикаторы
        self.indicator_names = None
        self.indicator_links = None

        # РЦ
        self.rc_start_name = "Ч1П"
        self.rc_index_pattern = INCREASE_MODE
        self.rc_number = 2
        self.rc_width = 40
        self.rc_content = None
        # ----------------------------------------------------------------------

        self.setupUi(self)
        self.setFixedSize(self.size())

        # группы для радио кнопок
        self.radio_name_group = QButtonGroup()

        self.set_radio_button_listeners()
        self.set_button_listeners()
        self.set_change_event_listeners()

        self.set_default_ui_view()

        # show the window
        self.show()

    # секция установки связи слушателей событий
    # ---------------------------------------------------------------------
    def set_radio_button_listeners(self):
        # установка наименования РЦ
        self.radio_name_group.addButton(self.radioNameChoose, 0)
        self.radio_name_group.addButton(self.radioNameCustome, 1)
        self.radio_name_group.idClicked.connect(self.change_name_mode_settings)

    def set_button_listeners(self):
        self.openButtonAdd.clicked.connect(self.push_read_button)
        self.generateButtonAdd.clicked.connect(self.push_generate_button)

    def set_change_event_listeners(self):
        # появление/скрытие вкладок
        self.numContrSpin.valueChanged.connect(self.on_change_mkrc_number)
        self.numGenSpin.valueChanged.connect(self.on_change_mgks_number)

        # смена имени РЦ на визуализации
        self.comboNameRc.currentIndexChanged.connect(self.set_name_chosen_name)
        self.customNameRcEdit.textChanged.connect(self.set_name_customed_name)

        # обновлении РЦ таблицы
        self.numRcSpin.editingFinished.connect(self.check_and_update_table_content)
        self.widthRcSpin.valueChanged.connect(self.check_and_update_table_content)
        self.horizontalRcSlider.sliderReleased.connect(self.check_and_update_table_content)
        self.horizontalRcSlider.valueChanged.connect(self.check_and_update_table_content)
        self.comboNameRc.currentTextChanged.connect(self.check_and_update_table_content)
        self.customNameRcEdit.editingFinished.connect(self.check_and_update_table_content)
        self.comboIndexNamePatter.currentIndexChanged.connect(self.check_and_update_table_content)

        # смена вкладок
        self.tabGenerateSettings.currentChanged.connect(self.lose_focus)

        # изменение геометрии РЦ
        self.widthRcSpin.valueChanged.connect(self.change_rc_geometry)
        self.horizontalRcSlider.valueChanged.connect(self.change_rc_geometry)
        self.heightRcSpin.valueChanged.connect(self.change_rc_geometry)
        self.verticalRcSlider.valueChanged.connect(self.change_rc_geometry)

        # изменение геометрии МКРЦ
        self.widthControlSpin.valueChanged.connect(self.change_mkrc_geometry)
        self.horizontalControlSlider.valueChanged.connect(self.change_mkrc_geometry)
        self.heightControlSpin.valueChanged.connect(self.change_mkrc_geometry)
        self.verticalControlSlider.valueChanged.connect(self.change_mkrc_geometry)

        # изменение геометрии МГКС
        self.widthGenlSpin.valueChanged.connect(self.change_mgks_geometry)
        self.horizontalGenSlider.valueChanged.connect(self.change_mgks_geometry)
        self.heightGenSpin.valueChanged.connect(self.change_mgks_geometry)
        self.verticalGenSlider.valueChanged.connect(self.change_mgks_geometry)

        # изменение геометрии стрелки
        self.widthArrowlSpin.valueChanged.connect(self.change_arrow_geometry)
        self.horizontalArrowSlider.valueChanged.connect(self.change_arrow_geometry)
        self.heightArrowSpin.valueChanged.connect(self.change_arrow_geometry)
        self.verticalArrowSlider.valueChanged.connect(self.change_arrow_geometry)

        # изменение геометрии индикаторов
        self.widthIndlSpin.valueChanged.connect(self.change_ind_geometry)
        self.horizontalIndSlider.valueChanged.connect(self.change_ind_geometry)
        self.heightIndSpin.valueChanged.connect(self.change_ind_geometry)
        self.verticalIndSlider.valueChanged.connect(self.change_ind_geometry)


    # ---------------------------------------------------------------------

    # секция настройки начальной кастомизации приложения
    # ---------------------------------------------------------------------

    def set_default_ui_view(self):
        self.set_tabs_visibility_off()
        self.set_rc_table()
        self.set_default_indicators()

    def set_tabs_visibility_off(self):
        self.tabGenerateSettings.setTabVisible(MKRC_TAB_ID, False)
        self.tabGenerateSettings.setTabVisible(MGKS_TAB_ID, False)
        self.tabGenerateSettings.setTabVisible(UKSPS_TAB_ID, False)

    def set_rc_table(self):
        self.set_column_widths()
        self.set_table_default_content()

    def set_column_widths(self):
        self.tableWidget.setColumnWidth(RC_NAME_ID, 115)
        self.tableWidget.setColumnWidth(RC_WIDTH_ID, 100)

    def set_table_default_content(self):
        self.set_default_row_number()
        self.set_default_content()

    def set_default_row_number(self):
        default_row_number = 2
        self.tableWidget.setRowCount(default_row_number)

    def set_default_content(self):
        rc_names = ["НАЧАЛО", "КОНЕЦ"]

        for i, name in enumerate(rc_names):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(name))
            self.tableWidget.setItem(i, 1, QTableWidgetItem("40"))

    def set_default_indicators(self):
        self.get_indicator_links_and_names()
        self.set_default_configuration()

    def get_indicator_links_and_names(self):
        # ссылки и имена настроек индикаторов
        self.indicator_names = ["ОТПР", "ИП1", "ИП2", "КП", "БП", "КК", "БИП1", "БИП2", "ИП3"]
        self.indicator_links = [self.checkIndDepartureBox,
                                self.checkIndOncomingBox_1,
                                self.checkIndOncomingBox_2,
                                self.checkIndOccupationBox_1,
                                self.checkIndOccupationBox_2,
                                self.checkIndKKBox,
                                self.checkIndDistanceBox_1,
                                self.checkIndDistanceBox_2,
                                self.checkIndOncomingBox_3]

    def set_default_configuration(self):
        default_indicator_configuration = config.details["ind"].values()

        for indicator_number, is_included in enumerate(default_indicator_configuration):
            self.set_indicator_state(indicator_number, is_included)

    def set_indicator_state(self, number, is_included):
        self.indicator_links[number].setChecked(is_included)

    # ---------------------------------------------------------------------

    # push radio button event listeners and connected func
    # ---------------------------------------------------------------------
    # ФУНКЦИЯ СЛУШАТЕЛЬ
    def change_name_mode_settings(self, radio_id):
        if radio_id == NAME_CHOOSE_ID:
            self.set_choose_rc_name_mode()
            self.update_table_content()
        if radio_id == NAME_CUSTOM_ID:
            self.set_custom_rc_name_mode()
            self.check_and_update_table_content()

    def set_choose_rc_name_mode(self):
        self.set_choose_button_available()
        self.set_chosen_rc_name()

    def set_choose_button_available(self):
        # смена включенных виджетов
        self.comboNameRc.setEnabled(True)
        self.customNameRcEdit.setDisabled(True)
        self.comboIndexNamePatter.setDisabled(True)

    def set_chosen_rc_name(self):
        # установка имени из комбо виджета
        rc_name = self.comboNameRc.currentText()
        self.rc_name_label.setText(rc_name)

    def set_custom_rc_name_mode(self):
        self.set_custom_button_available()
        self.set_custom_rc_name()

    def set_custom_button_available(self):
        # смена включенных виджетов
        self.customNameRcEdit.setEnabled(True)
        self.comboIndexNamePatter.setEnabled(True)
        self.comboNameRc.setDisabled(True)

    def set_custom_rc_name(self):
        # установка имени из комбо виджета
        rc_name = self.customNameRcEdit.text()
        self.rc_name_label.setText(rc_name)

    # ---------------------------------------------------------------------

    # push button event listeners and connected func
    # ---------------------------------------------------------------------
    def push_read_button(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(caption="Open File", filter="Config Files (*.ini)")
        if file_path != "":
            config.file_data = None
            file_name = file_path.split('/')[-1]
            file_path = file_path.replace('/', '\\')
            self.setWindowTitle("MapRedactor: " + file_name)
            ReadHandler(file_path).start()

    def push_generate_button(self):
        if not self.is_rc_editing_finished():
            self.send_message_unfinished()
            return

        if self.is_table_has_typo():
            self.send_message_typo()
            return

        if self.is_file_choosen():
            self.do_generation()
        else:
            self.send_message_no_file()

    def is_rc_editing_finished(self):
        is_tabel_updated = self.tableWidget.rowCount() == self.numRcSpin.value()
        return is_tabel_updated

    def send_message_unfinished(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка подготовки генерации!" + "\t" * 4)
        msg.setInformativeText("Генерация не началась, проверьте правильность\nнаименования первой рельсовой цепи!")
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def is_table_has_typo(self):
        row_number = self.tableWidget.rowCount()
        return not all([self.tableWidget.item(row, 1).text().isdigit() for row in range(row_number)])

    def send_message_typo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка подготовки генерации!" + "\t" * 4)
        msg.setInformativeText('Генерация не началась, найдена опечатка при заполнении\nтаблицы, столбец "Длинна"!')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def is_file_choosen(self):
        return config.file_path != ""

    def do_generation(self):
        self.get_input_data()
        self.send_content_to_config()
        self.send_data_to_generate_thread()

    def send_message_no_file(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка подготовки генерации!" + "\t" * 2)
        msg.setInformativeText('Генерация не началась, файл для записи\nне был выбран!')
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def get_input_data(self):

        self.get_general_data()
        self.get_rc_data()
        self.get_mkrc_data()
        self.get_mgks_data()
        self.get_uksps_data()
        self.get_arrow_data()
        self.get_ind_data()

    def get_general_data(self):
        coordinates = (self.calc_start_coordinates(), int(self.spinBoxOrdinate.value()))
        reserved = self.checkBoxReserv.isChecked()
        direct = self.comboBoxDirect.currentIndex()
        set_num = self.setNumSpin.value()

        # общая ифнформация о перегоне, считанная из пользовательского интерфейса
        self.info["general"] = {"coordinates": coordinates,
                                "reserved": reserved,
                                "direct": direct,
                                "set_num": set_num,
                                "interface": self.comboInterfaceRc.currentIndex(),
                                "rc_arrow_margin": self.marginArrowSpin.value()}

    def calc_start_coordinates(self):
        x = int(self.spinBoxAbscissa.value())
        direct = self.comboBoxDirect.currentIndex()

        # при напралении слева направо - установить коорд., заданные пользователем
        if direct == 0:
            return x

        # при обратном направелении высчитать необходимый сдвиг начала коорд.
        elif direct == 1:
            # данные о ширине были изменены вручную
            rc_num = int(self.numRcText.text())
            if len(config.details["rc"]) == rc_num:
                rc_shift = sum([int(width) for width in config.details["rc"].values()])
            # все РЦ равны по ширине
            else:
                width = int(self.widthRcText.text())
                rc_shift = rc_num * width

            shifted_x = x + rc_shift
            return shifted_x

    def get_rc_data(self):
        # ифнформация об РЦ, считанная из пользовательского интерфейса
        self.info["rc"] = {"num": self.numRcSpin.value(),
                           "height": self.heightRcSpin.value(),
                           "width": self.widthRcSpin.value()}

    def get_mkrc_data(self):
        # ифнформация об МКРЦ, считанная из пользовательского интерфейса
        self.info["mkrc"] = {"num": self.numContrSpin.value(),
                             "height": self.heightControlSpin.value(),
                             "width": self.widthControlSpin.value(),
                             "upper_margin": self.MarginControlSpin.value(),
                             "start_rc": self.radioConrolStartFirstPattern.isChecked()}

    def get_mgks_data(self):
        # ифнформация об МГКС, считанная из пользовательского интерфейса
        self.info["mgks"] = {"num": self.numGenSpin.value(),
                             "height": self.heightGenSpin.value(),
                             "width": self.widthGenlSpin.value(),
                             "upper_margin": self.marginGenSpin.value(),
                             "start_rc": self.radioGenStartFirstPattern.isChecked(),
                             "pattern": self.radioGenDistFirstPattern.isChecked()}

    def get_uksps_data(self):
        # ифнформация об УКСПС, считанная из пользовательского интерфейса
        self.info["uksps"] = {"num": self.numUkspsSpin.value(),
                              "height": self.heightUkspsText.text(),
                              "width": int(self.widthUkspsText.text())}

    def get_arrow_data(self):
        # ифнформация об стрелке направления, считанная из пользовательского интерфейса
        self.info["arrow"] = {"exists": self.checkBoxArrow.isChecked(),
                              "height": self.heightArrowSpin.value(),
                              "width": self.widthArrowlSpin.value()}

    def get_ind_data(self):
        # ифнформация об индификаторах, считанная из пользовательского интерфейса
        self.info["ind"] = {"height": self.heightIndSpin.value(),
                            "width": self.widthIndlSpin.value(),
                            "ind_arrow_margin": self.marginIndSpin.value()}

    def send_content_to_config(self):
        self.send_indicators_content()
        self.send_rc_content()

    def send_indicators_content(self):
        indicators = {name: checkbox.isChecked() for name, checkbox in zip(self.indicator_names, self.indicator_links)}
        config.details["ind"] = indicators

    def send_rc_content(self):
        row_number = self.tableWidget.rowCount()
        names = [self.tableWidget.item(row, 0).text() for row in range(row_number)]
        widths = [int(self.tableWidget.item(row, 1).text()) for row in range(row_number)]
        config.details["rc"] = {0: names, 1: widths}

    def send_data_to_generate_thread(self):
        GenHandler(self.info).start()

    # ---------------------------------------------------------------------

    # change value event listeners and connected func
    # ---------------------------------------------------------------------
    def lose_focus(self):
        self.numRcSpin.clearFocus()
        self.widthRcSpin.clearFocus()
        self.customNameRcEdit.clearFocus()

    def change_rc_geometry(self):
        if self.is_rc_width_changed():
            self.equalize_rc_width_control_values()
        else:
            self.equalize_rc_height_control_values()

    def is_rc_width_changed(self):
        is_width_sender = self.sender() in [self.widthRcSpin, self.horizontalRcSlider]
        return is_width_sender

    def equalize_rc_width_control_values(self):
        new_value = self.sender().value()
        self.widthRcSpin.setValue(new_value)
        self.horizontalRcSlider.setValue(new_value)

    def equalize_rc_height_control_values(self):
        new_value = self.sender().value()
        self.heightRcSpin.setValue(new_value)
        self.verticalRcSlider.setValue(new_value)

    def change_mkrc_geometry(self):
        if self.is_mkrc_width_changed():
            self.equalize_mkrc_width_control_values()
        else:
            self.equalize_mkrc_height_control_values()

    def is_mkrc_width_changed(self):
        is_width_sender = self.sender() in [self.widthControlSpin, self.horizontalControlSlider]
        return is_width_sender

    def equalize_mkrc_width_control_values(self):
        new_value = self.sender().value()
        self.widthControlSpin.setValue(new_value)
        self.horizontalControlSlider.setValue(new_value)

    def equalize_mkrc_height_control_values(self):
        new_value = self.sender().value()
        self.heightControlSpin.setValue(new_value)
        self.verticalControlSlider.setValue(new_value)

    def change_mgks_geometry(self):
        if self.is_mgks_width_changed():
            self.equalize_mgks_width_control_values()
        else:
            self.equalize_mgks_height_control_values()

    def is_mgks_width_changed(self):
        is_width_sender = self.sender() in [self.widthGenlSpin, self.horizontalGenSlider]
        return is_width_sender

    def equalize_mgks_width_control_values(self):
        new_value = self.sender().value()
        self.widthGenlSpin.setValue(new_value)
        self.horizontalGenSlider.setValue(new_value)

    def equalize_mgks_height_control_values(self):
        new_value = self.sender().value()
        self.heightGenSpin.setValue(new_value)
        self.verticalGenSlider.setValue(new_value)

    def change_arrow_geometry(self):
        if self.is_arrow_width_changed():
            self.equalize_arrow_width_control_values()
        else:
            self.equalize_arrow_height_control_values()

    def is_arrow_width_changed(self):
        is_width_sender = self.sender() in [self.widthArrowlSpin, self.horizontalArrowSlider]
        return is_width_sender

    def equalize_arrow_width_control_values(self):
        new_value = self.sender().value()
        self.widthArrowlSpin.setValue(new_value)
        self.horizontalArrowSlider.setValue(new_value)

    def equalize_arrow_height_control_values(self):
        new_value = self.sender().value()
        self.heightArrowSpin.setValue(new_value)
        self.verticalArrowSlider.setValue(new_value)

    def change_ind_geometry(self):
        if self.is_ind_width_changed():
            self.equalize_ind_width_control_values()
        else:
            self.equalize_ind_height_control_values()

    def is_ind_width_changed(self):
        is_width_sender = self.sender() in [self.widthIndlSpin, self.horizontalIndSlider]
        return is_width_sender

    def equalize_ind_width_control_values(self):
        new_value = self.sender().value()
        self.widthIndlSpin.setValue(new_value)
        self.horizontalIndSlider.setValue(new_value)

    def equalize_ind_height_control_values(self):
        new_value = self.sender().value()
        self.heightIndSpin.setValue(new_value)
        self.verticalIndSlider.setValue(new_value)

    def check_and_update_table_content(self):
        if self.is_name_appropriate():
            self.update_table_content()

    def is_name_appropriate(self):
        is_custom_name = self.radioNameCustome.isChecked()
        pattern = r'.*[ЧН]\d{1,2}П'
        name = self.customNameRcEdit.text()
        is_name_appropriate = re.fullmatch(pattern, name) is not None

        return is_custom_name and is_name_appropriate or not is_custom_name

    def update_table_content(self):
        self.clear_table()
        self.generate_table_content()
        self.set_table_content()

    def clear_table(self):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

    def generate_table_content(self):
        self.get_generative_parameters()
        self.save_table_content()

    def get_generative_parameters(self):
        self.rc_number = self.numRcSpin.value()
        self.rc_width = self.widthRcSpin.value()

        is_choose_name_mode = self.radioNameChoose.isChecked()
        if is_choose_name_mode:
            self.rc_start_name = self.comboNameRc.currentText()
            self.rc_index_pattern = INCREASE_MODE
        else:
            self.rc_start_name = self.customNameRcEdit.text()
            self.rc_index_pattern = self.comboIndexNamePatter.currentIndex()

    def save_table_content(self):
        generative_parameters = {"number": self.rc_number,
                                 "start_name": self.rc_start_name,
                                 "width": self.rc_width,
                                 "index_pattern": self.rc_index_pattern}
        self.rc_content = TableContent(generative_parameters).content

    def set_table_content(self):
        self.tableWidget.setRowCount(self.rc_number)

        for number, column_contents in self.rc_content.items():
            self.set_table_column(number, column_contents)

    def set_table_column(self, column, content):
        for row, cell_content in enumerate(content):
            self.tableWidget.setItem(row, column, QTableWidgetItem(str(cell_content)))

    def set_name_chosen_name(self):
        rc_name = self.comboNameRc.currentText()
        self.rc_name_label.setText(rc_name)

    def set_name_customed_name(self):
        rc_name = self.customNameRcEdit.text()
        self.rc_name_label.setText(rc_name)

    def on_change_mkrc_number(self):
        is_visible = self.get_mkrc_tab_state()
        self.tabGenerateSettings.setTabVisible(MKRC_TAB_ID, is_visible)

    def get_mkrc_tab_state(self):
        number_of_mkrc = self.numContrSpin.value()
        return number_of_mkrc > 0

    def on_change_mgks_number(self):
        is_visible = self.get_mgks_tab_state()
        self.tabGenerateSettings.setTabVisible(MGKS_TAB_ID, is_visible)

    def get_mgks_tab_state(self):
        number_of_mgks = self.numGenSpin.value()
        return number_of_mgks > 0

    # ---------------------------------------------------------------------

    def push_select_button(self):
        print("any button pushed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    app.exec_()
