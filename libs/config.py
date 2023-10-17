# карта расположения элементов в поле информации
element_info_map = {"Arrow": 2,"MKRCenter": 3, "MGKSexit": 4, "PerRC": 5, "Ind": 7, "UKSPS": 8}

# дефолтные поля элементов для последующего занесения данных
default_element_params = {"MGKSexit": ['0', '0', '20', '20', 'Имя', '1', '1', '1', '0', '0', '0', '0', ''],
                          "MKRCenter": ['0', '0', '20', '20', '0', '0', '0', '0', '0', '0', '1', '0', ''],
                          "UKSPS": ['630', '1064', '20', '20', '', '', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '']}

file_path = ""
file_data = None
rewrite_generation = False

details = {}


