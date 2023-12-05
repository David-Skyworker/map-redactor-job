from PyQt5.QtWidgets import QTableWidgetItem

import re

from utilities.validators import TableContentValidator


NAME_COLUMN = 0
WIDTH_COLUMN = 1


class TableContent:
    def __init__(self, main_window):
        self.window = main_window

        # генеративные данные
        self.params = GenerativeParams(main_window)

        self.index = 0
        self.content = {NAME_COLUMN: ["НАЧАЛО", "КОНЕЦ"], WIDTH_COLUMN: ["40", "40"]}

    def set_new_content(self):
        self.params.get()
        self._generate_content()
        self._set_new_table_content()

    # отрисовка нового контента
    # ---------------------------------------------------------------------

    def _generate_content(self):
        rc_number = self.params.rc_number
        width = str(self.params.width)

        inner_names = NameContent(self.params).get_names()
        self.content[NAME_COLUMN] = ["НАЧАЛО"] + inner_names + ["КОНЕЦ"]
        self.content[WIDTH_COLUMN] = [width] * rc_number

    def _set_new_table_content(self):
        self._clear_table()
        self._set_table_content()

    def _clear_table(self):
        while self.window.tableWidget.rowCount() > 0:
            self.window.tableWidget.removeRow(0)

    def _set_table_content(self):
        row_count = self.params.rc_number
        self.window.tableWidget.setRowCount(row_count)

        for number in range(row_count):
            self._set_row(number)

    def _set_row(self, row_number):
        name = self.content[NAME_COLUMN][row_number]
        self.window.tableWidget.setItem(row_number, NAME_COLUMN, QTableWidgetItem(str(name)))
        width = self.content[WIDTH_COLUMN][row_number]
        self.window.tableWidget.setItem(row_number, WIDTH_COLUMN, QTableWidgetItem(str(width)))

    # обновление РЦ имен таблицы
    # ---------------------------------------------------------------------

    def reset_name_column(self):
        self.params.get()
        if self.is_inner_rc_exist:  # нужно генерировать внутреннии РЦ
            self._generate_name_content()
            self._set_name_table_content()

    def is_inner_rc_exist(self):
        return self.params.rc_number != 2

    def _generate_name_content(self):
        start = self.content[NAME_COLUMN][0]
        end = self.content[NAME_COLUMN][-1]
        inner_names = NameContent(self.params).get_names()

        self.content[NAME_COLUMN] = [start] + inner_names + [end]

    def _set_name_table_content(self):
        last_row = self.params.inner_rc_number + 1
        for index in range(1, last_row):
            self._reset_name(index)

    def _reset_name(self, row_number):
        name = self.content[NAME_COLUMN][row_number]
        self.window.tableWidget.setItem(row_number, NAME_COLUMN, QTableWidgetItem(str(name)))

    # ---------------------------------------------------------------------

    def reset_width_column(self):
        self.params.get()
        self._generate_width_content()
        self._set_width_table_content()

    def _generate_width_content(self):
        width = self.params.width
        rc_number = self.params.rc_number

        widths = [width] * rc_number
        self.content[WIDTH_COLUMN] = widths

    def _set_width_table_content(self):
        row_number = self.params.rc_number
        for index in range(row_number):
            self._reset_width(index)

    def _reset_width(self, row_number):
        width = self.content[WIDTH_COLUMN][row_number]
        self.window.tableWidget.setItem(row_number, WIDTH_COLUMN, QTableWidgetItem(str(width)))

    # ---------------------------------------------------------------------
    def is_edited_correctly(self):
        return TableContentValidator(self.window).is_valid()

    def get(self):
        row_count = self.params.rc_number
        table = self.window.tableWidget

        names = [table.item(row, NAME_COLUMN).text() for row in range(row_count)]
        widths = [int(table.item(row, WIDTH_COLUMN).text()) for row in range(row_count)]
        return {"name": names, "width": widths}


class NameContent:
    def __init__(self, params):
        self.params = params

    def get_names(self):
        inner_rc_count = self.params.inner_rc_number
        inner_indexes = [self._count_index(i) for i in range(inner_rc_count)]
        names = list(map(self._build_name_by_index, inner_indexes))
        return names

    def _count_index(self, index):
        if self.params.is_index_increase:
            index = self.params.start_index + 2 * index
        else:
            index = self.params.start_index - 2 * index

        if index <= 0:
            index = "???"
        return index

    def _build_name_by_index(self, inner_index):
        name = self.params.prefix + str(inner_index) + "П"
        return name



INCREASE_MODE = True
INCREASE_MODE_INDEX = 0
EDGE_NUMBER = 2


class GenerativeParams:
    def __init__(self, main_window):
        self.window = main_window

        self.rc_number = 0
        self.inner_rc_number = 0
        self.width = ""
        self.prefix = ""
        self.start_index = 0
        self.is_index_increase = True

    def get(self):
        self._get_indifferent_mode_params()

        if self._is_mode_choose():
            self._get_choose_mode_params()
        else:
            self._get_custom_mode_params()

    def _get_indifferent_mode_params(self):
        self.rc_number = self.window.numRcSpin.value()
        self.inner_rc_number = self._get_inner_rc_num()
        self.width = self.window.widthRcSpin.value()

    def _get_inner_rc_num(self):
        rc_number = self.window.numRcSpin.value()
        inner_rc_number = rc_number - EDGE_NUMBER
        return inner_rc_number

    def _is_mode_choose(self):
        return self.window.radioNameChoose.isChecked()

    def _get_choose_mode_params(self):
        rc_name = self.window.comboNameRc.currentText()
        self._split_name(rc_name)
        self.is_index_increase = INCREASE_MODE

    def _get_custom_mode_params(self):
        rc_name = self.window.customNameRcEdit.text()
        self._split_name(rc_name)
        self.is_index_increase = self.window.comboIndexNamePatter.currentIndex() == INCREASE_MODE_INDEX

    def _split_name(self, name):
        name_split = re.split(r"(\d{1,2}П)", name)
        self.prefix = name_split[0]
        self.start_index = int(name_split[1][:-1])


class IndicatorConfig:
    def __init__(self, main_window):
        self.window = main_window
        self._indicator_names = ["ОТПР", "ИП1", "ИП2", "КП", "БП", "КК", "БИП1", "БИП2", "ИП3"]
        self._indicator_links = [main_window.checkIndDepartureBox,
                                 main_window.checkIndOncomingBox_1,
                                 main_window.checkIndOncomingBox_2,
                                 main_window.checkIndOccupationBox_1,
                                 main_window.checkIndOccupationBox_2,
                                 main_window.checkIndKKBox,
                                 main_window.checkIndDistanceBox_1,
                                 main_window.checkIndDistanceBox_2,
                                 main_window.checkIndOncomingBox_3]

        self._default_settings = [True, True, True, True, True, True, True, False, False]

    def set_default(self):
        for check_box, state in zip(self._indicator_links, self._default_settings):
            check_box.setChecked(state)

    def get(self):
        states = {name: indicator.isChecked() for name, indicator in zip(self._indicator_names, self._indicator_links)}
        return states


