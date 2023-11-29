# карта расположения элементов в поле информации
import copy

element_info_map = {"Arrow": 2,"MKRCenter": 3, "MGKSexit": 4, "PerRC": 5, "Ind": 7, "UKSPS": 8}

# дефолтные поля элементов для последующего занесения данных
default_element_params = {
                          "UKSPS": ['630', '1064', '20', '20', '', '', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '']}

file_path = ""
last_modified_date = None
file_data = None

rc_default = {}
ind_default = {'ОТПР': True, 'ИП1': True, 'ИП2': True, 'КП': True, 'БП': True,
               'КК': True, 'БИП1': True, 'БИП2': False, 'ИП3': False}

details = {"rc": {}, "ind": copy.copy(ind_default)}


def set_default():
    details["rc"] = dict()
    details["ind"] = copy.copy(ind_default)




