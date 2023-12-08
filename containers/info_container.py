from abc import ABC, abstractmethod
from libs import config


class RailWayInfo:
    def __init__(self, main_window):
        self.window = main_window

        self.general = GeneralInfo()
        self.rc = RCInfo()
        self.mgks = MKRCInfo()
        self.mkrc = MGKSInfo()
        self.uksps = UKSPSInfo()
        self.arrow = ArrowInfo()
        self.ind = IndicatorInfo()

    def set(self):
        self._set_general_data()
        self._set_rc_data()
        self._set_mkrc_data()
        self._set_mgks_data()
        self._set_arrow_data()
        self._set_ind_data()

    def _set_general_data(self):
        coord_x, coord_y = self.window.spinBoxAbscissa.value(), self.window.spinBoxOrdinate.value()
        direction = self.window.comboBoxDirect.currentIndex()

        # общая ифнформация о перегоне, считанная из пользовательского интерфейса
        self.general = GeneralInfo()
        self.general.coordinates = Coordinate(coord_x, coord_y, direction)
        self.general.reserved = self.window.checkBoxReserv.isChecked()
        self.general.direction = direction
        self.general.interface_type = self.window.comboInterfaceRc.currentIndex()
        self.general.set_number = self.window.setNumSpin.value()
        self.general.rc_arrow_margin = self.window.marginArrowSpin.value()


    def _set_rc_data(self):
        # ифнформация об РЦ, считанная из пользовательского интерфейса
        self.rc = RCInfo()
        self.rc.number = self.window.numRcSpin.value()
        self.rc.height = self.window.heightRcSpin.value()
        self.rc.width = self.window.widthRcSpin.value()

    def _set_mkrc_data(self):
        # ифнформация об МКРЦ, считанная из пользовательского интерфейса
        self.mkrc = MKRCInfo()
        self.mkrc.number = self.window.numContrSpin.value()
        self.mkrc.height = self.window.heightControlSpin.value()
        self.mkrc.width = self.window.widthControlSpin.value()
        self.mkrc.upper_margin = self.window.MarginControlSpin.value()
        self.mkrc.start_rc = self.window.radioConrolStartFirstPattern.isChecked()

    def _set_mgks_data(self):
        # ифнформация об МГКС, считанная из пользовательского интерфейса
        self.mgks = MGKSInfo()
        self.mgks.number = self.window.numGenSpin.value()
        self.mgks.height = self.window.heightGenSpin.value()
        self.mgks.width = self.window.widthGenlSpin.value()
        self.mgks.upper_margin = self.window.marginGenSpin.value()
        self.mgks.start_rc = self.window.radioGenStartFirstPattern.isChecked()
        self.mgks.pattern = self.window.radioGenDistFirstPattern.isChecked()

    def _set_uksps_data(self):
        # не реализовано
        pass

    def _set_arrow_data(self):
        self.arrow = ArrowInfo()
        self.arrow.number = int(self.window.checkBoxArrow.isChecked())
        self.arrow.height = self.window.heightArrowSpin.value()
        self.arrow.width = self.window.widthArrowlSpin.value()

    def _set_ind_data(self):
        self.ind = IndicatorInfo()
        self.ind.height = self.window.heightIndSpin.value()
        self.ind.width = self.window.widthIndlSpin.value()
        self.ind.ind_arrow_margin = self.window.marginIndSpin.value()


class GeneralInfo:
    def __init__(self):
        self.coordinates = Coordinate(0, 0, 0)
        self.reserved = False
        self.direction = 0
        self.set_number = 0
        self.interface_type = 0
        self.rc_arrow_margin = 0


REVERSED_DIRECTION = 1


class Coordinate:
    def __init__(self, x, y, direct):

        self._x = x
        self.y = y
        self.direct = direct

    @property
    def x(self):
        if self._is_reversed():
            shift = sum([int(width) for width in config.details["rc"]["width"]])
            return self._x + shift
        return self._x

    def _is_reversed(self):
        return self.direct == REVERSED_DIRECTION


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
