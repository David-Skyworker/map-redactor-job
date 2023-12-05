from abc import ABC, abstractmethod


class RailWayInfo:
    def __init__(self, main_window):
        self.window = main_window

        self.general = GeneralInfo()
        self.rc_info = RCInfo()
        self.mgks_info = MKRCInfo()
        self.mkrc_info = MGKSInfo()
        self.uksps_info = UKSPSInfo()
        self.arrow_info = ArrowInfo()
        self.ind_info = IndicatorInfo()

    def get(self):
        self._get_general_data()
        self._get_rc_data()
        self._get_mkrc_data()
        self._get_mgks_data()

    def _get_general_data(self):
        coord_x, coord_y = self.window.spinBoxAbscissa.value(), self.window.spinBoxOrdinate.value()
        reserved = self.window.checkBoxReserv.isChecked()

        # общая ифнформация о перегоне, считанная из пользовательского интерфейса
        self.general = GeneralInfo()
        self.general.coordinates = Coordinate(coord_x, coord_y)
        self.general.reserved = reserved
        self.general.direction = self.window.comboBoxDirect.currentIndex()
        self.general.set_number = self.window.setNumSpin.value()

    def _get_rc_data(self):
        # ифнформация об РЦ, считанная из пользовательского интерфейса
        self.rc_info = RCInfo()
        self.rc_info.number = self.window.numRcSpin.value()
        self.rc_info.height = self.window.heightRcSpin.value()
        self.rc_info.width = self.window.widthRcSpin.value()

    def _get_mkrc_data(self):
        # ифнформация об МКРЦ, считанная из пользовательского интерфейса
        self.mkrc_info = MKRCInfo()
        self.mkrc_info.number = self.window.numContrSpin.value()
        self.mkrc_info.height = self.window.heightControlSpin.value()
        self.mkrc_info.width = self.window.widthControlSpin.value()
        self.mkrc_info.upper_margin = self.window.MarginControlSpin.value()
        self.mkrc_info.start_rc = self.window.radioConrolStartFirstPattern.isChecked()

    def _get_mgks_data(self):
        # ифнформация об МГКС, считанная из пользовательского интерфейса
        self.mgks_info = MGKSInfo()
        self.mgks_info.number = self.window.numGenSpin.value()
        self.mgks_info.height = self.window.heightGenSpin.value()
        self.mgks_info.width = self.window.widthGenlSpin.value()
        self.mgks_info.upper_margin = self.window.marginGenSpin.value()
        self.mgks_info.start_rc = self.window.radioGenStartFirstPattern.isChecked()
        self.mgks_info.pattern = self.window.radioGenDistFirstPattern.isChecked()

    def _get_uksps_data(self):
        # не реализовано
        pass

    def _get_arrow_data(self):
        self.arrow_info = ArrowInfo()
        self.arrow_info.number = int(self.window.windowcheckBoxArrow.isChecked())
        self.arrow_info.height = self.window.heightArrowSpin.value(),
        self.arrow_info.width = self.window.widthArrowlSpin.value()

    def _get_ind_data(self):
        self.ind_info = IndicatorInfo()
        self.ind_info.height = self.window.heightIndSpin.value()
        self.ind_info.width = self.window.widthIndlSpin.value()
        self.ind_info.ind_arrow_margin = self.window.marginIndSpin.value()


class GeneralInfo:
    def __init__(self):
        self.coordinates = Coordinate(0, 0)
        self.reserved = False
        self.direction = 0
        self.set_number = 0
        self.interface_type = 0
        self.rc_arrow_margin = 0


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_reversed_x(self):
        pass

    def _count_start_x(self):
        # do something
        pass


class Info(ABC):
    def __init__(self):
        self.number = 0
        self.height = 0
        self.width = 0


class RCInfo(Info):
    def __init__(self):
        super().__init__()
        self.number = 2


class MKRCInfo(Info):
    def __init__(self):
        super().__init__()
        self.upper_margin = 0
        self.start_rc = True


class MGKSInfo(Info):
    def __init__(self):
        super().__init__()
        self.upper_margin = 0
        self.start_rc = True
        self.pattern = True


class UKSPSInfo(Info):
    def __init__(self):
        super().__init__()


class ArrowInfo(Info):
    def __init__(self):
        super().__init__()
        self.number = 1
        self.exists = True


class IndicatorInfo(Info):
    def __init__(self):
        super().__init__()
        self.ind_arrow_margin = 0
