from PyQt5.QtCore import QThread
import configparser

from libs import config
from libs.gen_library_2 import generate_way


class GenHandler(QThread):
    def __init__(self, info, parent=None):
        super().__init__()
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
            config.file_data.write(configfile)


class ReadHandler(QThread):
    def __init__(self, file_path, parent=None):
        super().__init__()
        self.file_path = file_path

    def __del__(self):
        self.wait()
        self.exit()

    def run(self):
        config.file_path = self.file_path
        config.file_data = self.read()

    def read(self):
        c = configparser.ConfigParser()
        c.optionxform = lambda option: option
        c.read(self.file_path)
        return c
