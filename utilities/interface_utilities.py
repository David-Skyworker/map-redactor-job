from libs import config
from utilities.content_utilities import TableContent

MKRC_TAB_ID = 2
MGKS_TAB_ID = 3
UKSPS_TAB_ID = 4

RC_NAME_ID = 0
RC_WIDTH_ID = 1


class EventListener:
    def __init__(self, main_window):
        self.window = main_window

    def set_window_event_linking(self):
        self._set_radio_button_listeners()
        self._set_button_listeners()
        self._set_change_event_listeners()
        # self._set_file_checker_signals()

    def _set_radio_button_listeners(self):
        # установка наименования РЦ
        self.window.radio_name_group.addButton(self.window.radioNameChoose, 0)
        self.window.radio_name_group.addButton(self.window.radioNameCustome, 1)
        self.window.radio_name_group.idClicked.connect(self.window.change_name_mode_settings)

    def _set_button_listeners(self):
        self.window.openButtonAdd.clicked.connect(self.window.push_read_button)
        self.window.generateButtonAdd.clicked.connect(self.window.push_generate_button)

    def _set_change_event_listeners(self):
        self._tab_visibility_change()
        self._rc_name_visualization_change()
        self._table_content_change()
        self._widget_focus_lose()
        self._geometry_change()

    def _tab_visibility_change(self):
        # появление/скрытие вкладок
        self.window.numContrSpin.valueChanged.connect(self.window.on_change_mkrc_number)
        self.window.numGenSpin.valueChanged.connect(self.window.on_change_mgks_number)

    def _rc_name_visualization_change(self):
        # смена имени РЦ на визуализации
        self.window.comboNameRc.currentIndexChanged.connect(self.window.set_chosen_name)
        self.window.customNameRcEdit.textChanged.connect(self.window.set_custom_name)

    def _table_content_change(self):
        # обновлении РЦ таблицы
        self.window.numRcSpin.editingFinished.connect(self.window.check_and_update_table_content)
        self.window.widthRcSpin.valueChanged.connect(self.window.check_and_update_table_content)
        self.window.horizontalRcSlider.sliderReleased.connect(self.window.check_and_update_table_content)
        self.window.horizontalRcSlider.valueChanged.connect(self.window.check_and_update_table_content)
        self.window.comboNameRc.currentTextChanged.connect(self.window.check_and_reset_name_column)
        self.window.customNameRcEdit.editingFinished.connect(self.window.check_and_reset_name_column)
        self.window.comboIndexNamePatter.currentIndexChanged.connect(self.window.check_and_reset_name_column)

    def _widget_focus_lose(self):
        # смена вкладок
        self.window.tabGenerateSettings.currentChanged.connect(self.window.lose_focus)

    # изменение размеров компонентов перегона
    # -------------------------------------------------------------------------------
    def _geometry_change(self):
        self._rc_geometry_change()
        self._mkrc_geometry_change()
        self._mgks_geometry_change()
        self._arrow_geometry_change()
        self._ind_geometry_change()

    def _rc_geometry_change(self):
        # изменение геометрии РЦ
        self.window.widthRcSpin.valueChanged.connect(self.window.change_rc_geometry)
        self.window.horizontalRcSlider.valueChanged.connect(self.window.change_rc_geometry)
        self.window.heightRcSpin.valueChanged.connect(self.window.change_rc_geometry)
        self.window.verticalRcSlider.valueChanged.connect(self.window.change_rc_geometry)

    def _mkrc_geometry_change(self):
        # изменение геометрии МКРЦ
        self.window.widthControlSpin.valueChanged.connect(self.window.change_mkrc_geometry)
        self.window.horizontalControlSlider.valueChanged.connect(self.window.change_mkrc_geometry)
        self.window.heightControlSpin.valueChanged.connect(self.window.change_mkrc_geometry)
        self.window.verticalControlSlider.valueChanged.connect(self.window.change_mkrc_geometry)

    def _mgks_geometry_change(self):
        # изменение геометрии МГКС
        self.window.widthGenlSpin.valueChanged.connect(self.window.change_mgks_geometry)
        self.window.horizontalGenSlider.valueChanged.connect(self.window.change_mgks_geometry)
        self.window.heightGenSpin.valueChanged.connect(self.window.change_mgks_geometry)
        self.window.verticalGenSlider.valueChanged.connect(self.window.change_mgks_geometry)

    def _arrow_geometry_change(self):
        # изменение геометрии стрелки
        self.window.widthArrowlSpin.valueChanged.connect(self.window.change_arrow_geometry)
        self.window.horizontalArrowSlider.valueChanged.connect(self.window.change_arrow_geometry)
        self.window.heightArrowSpin.valueChanged.connect(self.window.change_arrow_geometry)
        self.window.verticalArrowSlider.valueChanged.connect(self.window.change_arrow_geometry)

    def _ind_geometry_change(self):
        # изменение геометрии индикаторов
        self.window.widthIndlSpin.valueChanged.connect(self.window.change_ind_geometry)
        self.window.horizontalIndSlider.valueChanged.connect(self.window.change_ind_geometry)
        self.window.heightIndSpin.valueChanged.connect(self.window.change_ind_geometry)
        self.window.verticalIndSlider.valueChanged.connect(self.window.change_ind_geometry)

    # -------------------------------------------------------------------------------

    def _set_file_checker_signals(self):
        # сигналы от потока проверяющего наличие/изменение редактируемого файла
        self.window.file_checker.gone_file_signal.connect(self.window.inform_and_remove_file_data)
        self.window.file_checker.modified_file_signal.connect(self.window.inform_and_offer_data_update)


class WindowView:
    def __init__(self, main_window):
        self.window = main_window

    def set_default_ui_view(self):
        self.set_tabs_visibility_off()
        self.set_rc_table()
        self.set_default_indicators()

    def set_tabs_visibility_off(self):
        self.window.tabGenerateSettings.setTabVisible(MKRC_TAB_ID, False)
        self.window.tabGenerateSettings.setTabVisible(MGKS_TAB_ID, False)
        self.window.tabGenerateSettings.setTabVisible(UKSPS_TAB_ID, False)

    def set_rc_table(self):
        self.set_column_widths()
        self.window.rc_table.set_new_content()

    def set_column_widths(self):
        self.window.tableWidget.setColumnWidth(RC_NAME_ID, 115)
        self.window.tableWidget.setColumnWidth(RC_WIDTH_ID, 100)

    def set_default_indicators(self):
        self.window.indicators.set_default()




