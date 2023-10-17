from PyQt5.QtCore import QThread
import configparser

from libs import config
from libs.gen_library import generate_way


class GenHandler(QThread):
    def __init__(self, info, parent=None):
        super().__init__()
        self.info = info

    def __del__(self):
        self.wait()
        self.exit()

    def run(self):
        # генерация элементов перегона
        generated_elements = generate_way(self.info)

        # запись сгенерированных элементов в кофигпарсер
        # self.write(generated_elements)

        # сохранение обновленных данных в файл
        # self.save_config()

    def write(self, elements):

        if "StationPlan" in config.file_data:
            info = config.file_data["StationPlan"]["INITinfo"].split(';')
        else:
            config.file_data["StationPlan"] = {}
            config.file_data["StationPlan"]["INITinfo"] = ""
            info = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '']
        self.write_rc(elements["rc"], info)
        config.file_data["StationPlan"]["INITinfo"] = ';'.join(info)



    def write_rc(self, rc_list, info):
        num = info[5]
        for i, rc in enumerate(rc_list):
            num = str(i + int(info[5]) + 1)
            config.file_data["StationPlan"]["PerRC" + num] = rc
        else:
            info[5] = num

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
