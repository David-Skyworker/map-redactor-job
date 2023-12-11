from UI.UI_Main_2 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QDialog, QButtonGroup, QMessageBox
from PyQt5 import QtWidgets

from icecream import ic
import sys
import os
import time

from libs import config
from libs.thread_handlers import ReadHandler, GenHandler, FileChecker
from utilities.interface_utilities import EventListener, WindowView
from utilities.content_utilities import TableContent, IndicatorConfig
from utilities.validators import RcNameValidator
from utilities.messages import TableTypoMessage, NoFileMessage, FileGoneMessage, FileChangedMessage, DuplicatedOptions
from utilities.messages import UnfinishedChangeMessage
from containers.info_container import RailWayInfo


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
        self.setupUi(self)
        self.start_name_validator = RcNameValidator(self)
        # self.file_checker = FileChecker()
        self.rc_table = TableContent(self)
        self.indicators = IndicatorConfig(self)

        # поля для работы с данными интерфейса
        self.info = RailWayInfo(self)

        # ----------------------------------------------------------------------

        self.setFixedSize(self.size())

        # группы для радио кнопок
        self.radio_name_group = QButtonGroup()

        # установка слушателей событий и сигналов
        EventListener(self).set_window_event_linking()

        self.set_default_ui_view()

        # show the window
        self.show()
    # секция настройки начальной кастомизации приложения
    # ---------------------------------------------------------------------

    def set_default_ui_view(self):
        WindowView(self).set_default_ui_view()

    # ---------------------------------------------------------------------

    # push radio button event listeners and connected func
    # ---------------------------------------------------------------------
    # ФУНКЦИЯ СЛУШАТЕЛЬ
    def change_name_mode_settings(self, radio_id):
        if radio_id == NAME_CHOOSE_ID:
            self.set_choose_rc_name_mode()
            self.rc_table.reset_name_column()
        if radio_id == NAME_CUSTOM_ID:
            self.set_custom_rc_name_mode()
            self.check_and_reset_name_column()

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

    # file monitoring events
    # ---------------------------------------------------------------------
    def inform_and_remove_file_data(self):
        self.send_message_file_gone()
        self.clear_config_and_interface_file_data()

    def send_message_file_gone(self):
        FileGoneMessage()

    def clear_config_and_interface_file_data(self):
        self.setWindowTitle("MapRedactor")
        config.file_path = ""
        config.last_modified_date = None
        config.file_data = None

    def inform_and_offer_data_update(self):
        answer = FileChangedMessage()
        if answer.is_reset_file:
            self.read_file(config.file_path)
    # ---------------------------------------------------------------------

    # push button event listeners and connected func
    # ---------------------------------------------------------------------
    def push_read_button(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(caption="Open File", filter="Config Files (*.ini)")
        if file_path != "":
            self.read_file(file_path)

    def read_file(self, file_path):
        self.prepare_config_path_and_data(file_path)
        self.set_read_and_check_workers()

    def prepare_config_path_and_data(self, path):
        config.file_data = None
        ic(config.file_path)
        config.file_path = path.replace('\\', '???')
        config.file_path = path
        ic(config.file_path)
        config.last_modified_date = time.ctime(os.path.getmtime(config.file_path))


    def set_read_and_check_workers(self):
        file_reader = ReadHandler()
        file_reader.duplicates_file_signal.connect(self.send_message_duplicates)
        file_reader.read_success_signal.connect(self.set_main_window_title)
        file_reader.start()
        # self.file_checker.start()

    def set_main_window_title(self):
        new_title = config.file_path.split('/')[-1]
        ic(new_title)

        self.setWindowTitle("MapRedactor: " + new_title)

    def push_generate_button(self):
        if not self.is_rc_editing_finished():
            self.send_message_unfinished()
            return

        if self.is_table_has_typo():
            self.send_message_typo()
            return

        if self.is_file_choosen():
            # self.pause_file_checker()
            self.do_generation()
        else:
            self.send_message_no_file()

    def is_rc_editing_finished(self):
        is_tabel_updated = self.tableWidget.rowCount() == self.numRcSpin.value()
        return is_tabel_updated

    def send_message_unfinished(self):
        UnfinishedChangeMessage()

    def is_table_has_typo(self):
        self.rc_table.is_edited_correctly()

    def send_message_typo(self):
        TableTypoMessage()

    def is_file_choosen(self):
        return config.file_path != ""

    def pause_file_checker(self):
        self.file_checker.quit()
        # TODO: complete checker pause logic

    def do_generation(self):
        self.send_content_to_config()
        self.info.set()
        self.send_data_to_generate_thread()

    def send_content_to_config(self):
        self.send_indicators_content()
        self.send_rc_content()

    def send_indicators_content(self):
        indicator_configuration = self.indicators.get()
        config.details["ind"] = indicator_configuration

    def send_rc_content(self):
        rc_content = self.rc_table.get()
        config.details["rc"] = rc_content

    def send_data_to_generate_thread(self):
        GenHandler(self.info).start()

    def send_message_no_file(self):
        NoFileMessage()

    # ---------------------------------------------------------------------

    # change value event listeners and connected func
    # ---------------------------------------------------------------------
    def send_message_duplicates(self, error_message):
        DuplicatedOptions(error_message)
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
        if self.start_name_validator.is_valid():
            self.rc_table.set_new_content()

    def check_and_reset_name_column(self):
        if self.start_name_validator.is_valid():
            self.rc_table.reset_name_column()

    def check_and_reset_width_column(self):
        if self.start_name_validator.is_valid():
            self.rc_table.reset_width_column()

    def set_chosen_name(self):
        rc_name = self.comboNameRc.currentText()
        self.rc_name_label.setText(rc_name)

    def set_custom_name(self):
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
