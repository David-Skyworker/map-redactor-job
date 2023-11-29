from abc import ABC, abstractmethod
import re


class Validator(ABC):
    def __init__(self, main_window):
        self.window = main_window

    @abstractmethod
    def is_valid(self):
        # провести проверку взятого объкта на наличие опечаток
        pass


class RcNameValidator(Validator):
    def __init__(self, main_window):
        super().__init__(main_window=main_window)
        self.name_pattern = r".*[ЧН]\d{1,2}П"

    def is_valid(self):
        return self._is_choose_mode() or self._is_custom_name_valid()

    def _is_choose_mode(self):
        is_chose = self.window.radioNameChoose.isChecked()
        return is_chose

    def _is_custom_name_valid(self):
        name = self.window.customNameRcEdit.text()
        is_valid = re.fullmatch(self.name_pattern, name) is not None
        return is_valid


WIDTH_COLUMN = 1


class TableContentValidator(Validator):
    def __init__(self, main_window):
        super().__init__(main_window=main_window)
        self.rc_table = main_window.tableWidget

    def is_valid(self):
        row_number = self.rc_table.rowCount()
        table = self.rc_table
        width_column_content = [table.item(row, WIDTH_COLUMN).text() for row in range(row_number)]
        is_all_digit = all([row.isdigit() for row in width_column_content])
        return is_all_digit
