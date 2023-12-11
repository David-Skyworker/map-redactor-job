from PyQt5.QtCore import QThread
from PyQt5 import QtCore
import configparser
import time
import os

from libs import config
from libs.gen_library_2 import generate_way


class GenHandler(QThread):
    def __init__(self, info, parent=None):
        super().__init__(parent=parent)
        self.info = info

        self.nums = {"rc": 5, "mkrc": 3, "mgks": 4, "arrow": 2, "ind": 7}
        self.names = {"rc": "PerRC", "mkrc": "MKRCenter", "mgks": "MGKSexit",
                      "arrow": "Arrow", "ind": "Ind"}

    def __del__(self):
        self.wait()
        self.exit()

    def run(self):
        # генерация элементов перегона
        generated_elements = generate_way(self.info)

        # запись сгенерированных элементов в кофигпарсер
        self.write(generated_elements)

        # сохранение обновленных данных в файл
        self.save_config()

    def write(self, elements_data):
        # инициализация информационного поля модуля "StationPlan"
        info = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '']

        # проверка наличия модуля "StationPlan" в .INI файле
        # -------------------------------------------------------------------------
        if "StationPlan" in config.file_data:
            if "INITinfo" in config.file_data["StationPlan"]:
                info = config.file_data["StationPlan"]["INITinfo"].split(';')
            else:
                config.file_data["StationPlan"]["INITinfo"] = ';'.join(info)
        else:
            config.file_data["StationPlan"] = {}
            config.file_data["StationPlan"]["INITinfo"] = ';'.join(info)
        # -------------------------------------------------------------------------

        element_names = ["arrow", "rc", "mkrc", "mgks", "ind"]
        for name in element_names:
            self.write_element(elements_data[name], info, name)

        config.file_data["StationPlan"]["INITinfo"] = ';'.join(info)

    def write_element(self, elements, info, name):
        # проверка списка на наличие элементов
        if not elements:
            return

        info_num = self.nums[name]

        num = info[info_num]
        for i, rc in enumerate(elements):
            num = str(i + int(info[info_num]) + 1)
            config.file_data["StationPlan"][self.names[name] + num] = rc
        else:
            info[info_num] = num

    def save_config(self):
        with open(config.file_path, 'w') as configfile:
            config.file_data.write(configfile, space_around_delimiters=False)


class ReadHandler(QThread):
    duplicates_file_signal = QtCore.pyqtSignal(object)
    read_success_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.file_path = config.file_path

    def __del__(self):
        self.wait()
        self.exit()

    def run(self):
        try:
            self.read_config()
        except configparser.DuplicateOptionError as e:
            self.duplicates_file_signal.emit(e)
            self.deleteLater()
            return

        self.read_success_signal.emit()

    def read_config(self):
        c = configparser.ConfigParser(comment_prefixes='/', allow_no_value=True)
        c.optionxform = lambda option: option
        c.read(self.file_path)
        config.file_data = c


class FileChecker(QThread):
    gone_file_signal = QtCore.pyqtSignal()
    modified_file_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.counter = 0

    def __del__(self):
        self.wait()
        self.exit()

    def run(self) -> None:
        while self.is_changes_found():
            self.counter += 1
            print(self.counter)
            time.sleep(.5)
        else:
            self.indentify_file_changes_and_notify()

    def is_changes_found(self):
        return not(self.is_file_gone() or self.is_file_modified())

    def indentify_file_changes_and_notify(self):
        if self.is_file_gone():
            self.gone_file_signal.emit()
        if self.is_file_modified():
            print("in modified")
            self.modified_file_signal.emit()

    def is_file_gone(self):
        return not os.path.exists(config.file_path)

    def is_file_modified(self):
        try:
            modified = config.last_modified_date != time.ctime(os.path.getmtime(config.file_path))
            print(config.last_modified_date, time.ctime(os.path.getmtime(config.file_path)))
        except FileNotFoundError:
            modified = False
        print(modified)
        return modified

