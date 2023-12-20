from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QMessageBox
from enum import Enum


class WarningType(Enum):
    TABLE_TYPO = 1
    UNFINISHED_CHANGES = 2
    NO_FILE = 3
    DUPLICATION_FOUND = 4
    FILE_GONE = 5
    FILE_CHANGED = 6


class Message(ABC):
    _registry = {}
    
    def __init_subclass__(cls, warning_type=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if warning_type is not None:
            cls._registry[warning_type] = cls

    def __new__(cls, warning_type, **kwargs):
        subclass = cls._registry[warning_type]
        return object.__new__(subclass)

    @abstractmethod
    def _appear(self):
        # информация сообщенния
        raise NotImplementedError


class TableTypoMessage(Message, warning_type=WarningType.TABLE_TYPO):
    def __init__(self, warning_type):
        super().__init__()
        self._appear()

    def _appear(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка подготовки генерации!" + "\t" * 4)
        msg.setInformativeText('Генерация не началась, найдена опечатка при заполнении\nтаблицы, столбец "Длинна"!')
        msg.setWindowTitle("Ошибка")
        msg.exec_()


class NoFileMessage(Message, warning_type=WarningType.NO_FILE):
    def __init__(self, warning_type):
        self._appear()

    def _appear(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка подготовки генерации!" + "\t" * 2)
        msg.setInformativeText('Генерация не началась, файл для записи\nне был выбран!')
        msg.setWindowTitle("Ошибка")
        msg.exec_()


class FileGoneMessage(Message, warning_type=WarningType.FILE_GONE):
    def __init__(self, warning_type):
        self._appear()

    def _appear(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Окончание работы с текущим файлом" + "\t" * 3)
        msg.setInformativeText("Генерация не возможна, редактируемый файл\nбыл удален или перемещен!")
        msg.setWindowTitle("Оповещение")
        msg.exec_()


class FileChangedMessage(Message, warning_type=WarningType.FILE_CHANGED):
    def __init__(self, warning_type):
        self.is_reset_file = self._appear()

    def _appear(self):
        reset_messagebox = QMessageBox()
        choice = reset_messagebox.question(self, '', "Are you sure to reset all the values?",
                                           reset_messagebox.Yes | reset_messagebox.No)
        return choice == reset_messagebox.Yes


class UnfinishedChangeMessage(Message, warning_type=WarningType.UNFINISHED_CHANGES):
    def __init__(self, warning_type):
        self._appear()

    def _appear(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка подготовки генерации!" + "\t" * 4)
        msg.setInformativeText("Генерация не началась, проверьте правильность\nнаименования первой рельсовой цепи!")
        msg.setWindowTitle("Ошибка")
        msg.exec_()


class DuplicatedOptions(Message, warning_type=WarningType.DUPLICATION_FOUND):
    def __init__(self, warning_type, message):
        self._message = str(message)

        self._build_informative_text()
        self._appear()

    def _appear(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка чтения файла!" + "\t" * 4)
        msg.setInformativeText(self._message)
        msg.setWindowTitle("Ошибка")
        msg.exec_()

    def _build_informative_text(self):
        error_info = self._message.split("'")[1::2]
        key = error_info[1]
        section = error_info[2]
        self._message = f"При чтении файла в секции {section} обнаружено\nдублирование ключа {key}!"
