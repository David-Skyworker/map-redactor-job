from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QMessageBox


class Message(ABC):

    @abstractmethod
    def _appear(self):
        # информация сообщенния
        pass


class TableTypoMessage(Message):
    def __init__(self):
        super().__init__()
        self._appear()

    def _appear(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка подготовки генерации!" + "\t" * 4)
        msg.setInformativeText('Генерация не началась, найдена опечатка при заполнении\nтаблицы, столбец "Длинна"!')
        msg.setWindowTitle("Ошибка")
        msg.exec_()


class NoFileMessage(Message):
    def __init__(self):
        super().__init__()
        self._appear()

    def _appear(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка подготовки генерации!" + "\t" * 2)
        msg.setInformativeText('Генерация не началась, файл для записи\nне был выбран!')
        msg.setWindowTitle("Ошибка")
        msg.exec_()


class FileGoneMessage(Message):
    def __init__(self):
        super().__init__()
        self._appear()

    def _appear(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Окончание работы с текущим файлом" + "\t" * 3)
        msg.setInformativeText("Генерация не возможна, редактируемый файл\nбыл удален или перемещен!")
        msg.setWindowTitle("Оповещение")
        msg.exec_()


class FileChangedMessage(Message):
    def __init__(self):
        super().__init__()
        self.is_reset_file = self._appear()

    def _appear(self):
        reset_messagebox = QMessageBox()
        choice = reset_messagebox.question(self, '', "Are you sure to reset all the values?",
                                           reset_messagebox.Yes | reset_messagebox.No)
        return choice == reset_messagebox.Yes


class UnfinishedChangeMessage(Message):
    def __init__(self):
        super().__init__()
        self._appear()

    def _appear(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Ошибка подготовки генерации!" + "\t" * 4)
        msg.setInformativeText("Генерация не началась, проверьте правильность\nнаименования первой рельсовой цепи!")
        msg.setWindowTitle("Ошибка")
        msg.exec_()


class DuplicatedOptions(Message):
    def __init__(self, message):
        super().__init__()
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
