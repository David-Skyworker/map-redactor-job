from copy import copy

from libs import config


def generate_way(info):
    """
        Функция генерации перегона.
        :param info: dict
            словарь, содержащий данные для генерации объектов программой, таких как РЦ, МГКС, МКРЦ и т.д.

        :return: словарь, содержащий полную информацию о сгенерированном перегоне в соответствующим формате для
        сохранения в .ini файл.
    """
    _adjust_margins(info)

    rc_list, rc_coordinates, mkrc_shift_y = _generate_rc(info["rc"], info["general"])

    mkrc_list = _generate_mkrc(info["mkrc"], info["general"], rc_coordinates)

    return {"rc": rc_list, "mkrc": mkrc_list, "mgks": rc_list, "uksps": rc_list, "arrow": rc_list, "ind": rc_list}


def _adjust_margins(info):
    """
        Функция настройки отступов МКРЦ и МГКС от ближайших к ним элементов на оступы от координат,
        заданных в пользовательском интерфейсе.
        :param info: dict
            данные о аттрибутах мкрц необходимые для их отрисовки(width, height etc.)
    """
    mkrc_margin = info["mkrc"]["upper_margin"] + int(info["rc"]["height"])
    mgks_margin = info["mgks"]["upper_margin"] + mkrc_margin + int(info["mkrc"]["height"])

    info["mkrc"]["upper_margin"], info["mgks"]["upper_margin"] =mkrc_margin, mgks_margin

def _generate_rc(info, general):
    """
    Функция генерации рельсовых цепей.
    :param info: dict
        данные о аттрибутах рельсовых цепей необходимые для их отрисовки(width, height etc.)

    :return: список, содержащий результат генерации РЦ и список координат РЦ
    """

    if "rc" in config.details:
        # словарь с именами и длиннами уже создан
        details = config.details["rc"]
    else:
        # генерация словаря с именами и длиннами
        letter = info["first_rc_name"][0]
        num = int(info["first_rc_name"][1])

        details_name = ["НАЧАЛО"] + [(letter + str(num + i * 2) + 'П') for i in range(info["num"] - 2)] + ["КОНЕЦ"]
        details_width = [info["width"] for _ in range(info["num"])]
        details = dict(zip(details_name, details_width))

    if general["direct"]:
        shifts = [-sum(list(map(int, details.values()))[0:i + 1]) for i in range(info["num"])]
    else:
        shifts = [0] + [sum(list(map(int, details.values()))[0:i + 1]) for i in range(info["num"] - 1)]

    # список для хранения РЦ
    generated_rc = []
    coordinates = []

    # цикл добавления цепи в "generated_rc"
    for i, (name, width) in enumerate(details.items()):

        # инициализация временной переменой РЦ для шага генерации
        rc = ['0', '0', info["height"], width, name, '1', '0', '0', general["set_num"] , '0', '0', '0', str(i + 1)  , '0', '']

        # запись параметров РЦ
        rc[0] = str(general["coordinates"][1])              # сдвиг по Y
        rc[1] = str(general["coordinates"][0] + shifts[i])  # сдвиг по X

        if i + 1 not in [1, info["num"]]:
            # настройка небоковых РЦ
            rc[11] = str(int(general["reserved"]))       # резервирование
        elif i + 1 == info["num"]:
            # настройка увязки конечной РЦ
            rc[9] = "64"
            rc[13] = "2"
        elif i == 0:
            # настройка увязки начальной РЦ
            if general["interface"]:
                # цифровой интерфейс
                rc[13] = "3"
            else:
                # релейный интерфейс
                rc[13] = "1"

        coordinates.append(int(rc[1]))
        generated_rc.append(';'.join(rc))

    return generated_rc, coordinates, info["height"]


def _generate_mkrc(info, general, coordinates):
    """
    Функция генерации МКРЦ.
    :param info: dict
        данные о аттрибутах мкрц необходимые для их отрисовки(width, height etc.)

    :return: список, содержащий результат генерации МКРЦ
    """
    if info["num"] <= 0:
        return []

    if general["direct"] == 0:
        if info["start_rc"] == 0:
            mkrc_coordinates = coordinates[1::2]
        else:
            mkrc_coordinates = coordinates[2::2]
    else:
        if info["start_rc"] == 0:
            mkrc_coordinates = coordinates[::2]
        else:
            mkrc_coordinates = coordinates[1:-1:2]

    if general["direct"] == 0:
        rc_edges = [coordinates[1], coordinates[-1]]
    else:
        rc_edges = [coordinates[0], coordinates[-2]]

    mkrc_coordinates = mkrc_coordinates[:info["num"]]

    generated_mkrc = []
    for i, coordinate_x in enumerate(mkrc_coordinates):


        mkrc = ['0', '0', info["height"], info["width"], '0', '0', '0', '0', general["set_num"], str(i + 1), '2', '0', '']
        mkrc[0] = str(general["coordinates"][1] + info["upper_margin"])  # сдвиг по Y

        # 9 - номер мкрц и 10 - привязка к рц

        # одиночная МКРЦ
        if coordinate_x in rc_edges:
            shift_x = round(int(info["width"]) / 2)
            mkrc[1] = str(coordinate_x - shift_x)

            generated_mkrc.append(';'.join(mkrc))
        else:
            mkrc_1 = mkrc.copy()
            mkrc_1[10] = "1"

            mkrc_2 = mkrc.copy()

            x = int(coordinate_x)
            left_x = str(x - int(info["width"]) - 1)
            right_x = str(x + 1)

            if general["direct"] == 0:
                mkrc_1[1], mkrc_2[1] = left_x, right_x
            else:
                mkrc_1[1], mkrc_2[1] = right_x, left_x

            generated_mkrc.append(';'.join(mkrc_1))
            generated_mkrc.append(';'.join(mkrc_2))

    return generated_mkrc


# def _generate_mgks(info, general, coordinates):
#     """
#     Функция генерации МГКС.
#     :param info: dict
#         данные о аттрибутах рельсовых цепей необходимые для их отрисовки(width, height etc.)
#
#     :return: список, содержащий результат генерации МГКС
#     """
#
#     width = info["width"]
#     height = info["height"]
#
#     # список для хранения МГКС
#     generated_mgks = []
#
#     if general["direct"]:
#         shifts = [-sum(list(map(int, details.values()))[0:i + 1]) for i in range(info["num"])]
#     else:
#         shifts = [0] + [sum(list(map(int, details.values()))[0:i + 1]) for i in range(info["num"] - 1)]
#
#     for i in range(info["num"]):
#
#         # инициализация временной переменой РЦ для шага генерации
#         rc = ['0', '0', '20', '40', 'Имя', '1', '0', '0', '0', '0', '0', '0', '0', '0', '']
#
#         # запись параметров РЦ
#         rc[0] = str(general["coordinates"][1])              # сдвиг по X
#         rc[1] = str(general["coordinates"][0] + shifts[i])  # сдвиг по Y
#         rc[2] = height
#         rc[3] = width
#         rc[4] = "МГКС " + str(i + 1)
#         rc[8] = general["set_num"]                       # номер комплекта
#         rc[12] = str(i + 1)                              # номер РЦ
#
#         if i + 1 not in [1, info["num"]]:
#             # настройка небоковых РЦ
#             rc[11] = str(int(general["reserved"]))       # резервирование
#         elif i + 1 == info["num"]:
#             # настройка увязки конечной РЦ
#             rc[9] = "64"
#             rc[13] = "2"
#         elif i == 0:
#             # настройка увязки начальной РЦ
#             if general["interface"]:
#                 # цифровой интерфейс
#                 rc[13] = "3"
#             else:
#                 # релейный интерфейс
#                 rc[13] = "1"
#
#
#     return "None"


def _generate_uksps(info):
    return None


def _generate_arrow(info):
    return None


def _generate_ind(info):
    return None



