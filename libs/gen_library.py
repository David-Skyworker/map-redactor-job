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

    mkrc_list, mkrc_nums = _generate_mkrc(info["mkrc"], info["general"], rc_coordinates)

    rc_list = _set_rc_mkrc_linking(rc_list, mkrc_nums)
    print(rc_list)

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

    # генерация сдвигов рельсовых цепей в относительно начальной точки зависимости от напраления
    if general["direct"] == 0:
        # слева направо
        shifts = [0] + [sum(list(map(int, details.values()))[0:i + 1]) for i in range(info["num"] - 1)]
    else:
        # справа налево
        shifts = [-sum(list(map(int, details.values()))[0:i + 1]) for i in range(info["num"])]

    # список для хранения РЦ
    generated_rc = []
    coordinates = []

    # цикл добавления цепи в "generated_rc"
    for i, (name, width) in enumerate(details.items()):

        # инициализация временной переменой РЦ для шага генерации
        rc = ['0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '']

        # запись параметров РЦ
        rc[0] = str(general["coordinates"][1])              # сдвиг по Y
        rc[1] = str(general["coordinates"][0] + shifts[i])  # сдвиг по X
        rc[2] = info["height"]
        rc[3] = width
        rc[4] = name
        rc[8] = general["set_num"]
        rc[12] = str(i + 1)                                 # номер рц

        # настройка параметров боковых и внутренних РЦ
        if i + 1 not in [1, info["num"]]:
            # настройка внутренних РЦ
            rc[11] = str(int(general["reserved"]))       # резервирование
        elif i + 1 == info["num"]:
            # настройка увязки конечной РЦ
            rc[9] = "64"
            rc[13] = "2"
        elif i == 0:
            # настройка увязки начальной РЦ в зависимости от типа интерфейса
            if general["interface"] == 0:
                # релейный интерфейс
                rc[13] = "1"
            else:
                # цифровой интерфейс
                rc[13] = "3"

        coordinates.append(int(rc[1]))
        generated_rc.append(rc)

    return generated_rc, coordinates, info["height"]


def _generate_mkrc(info, general, coordinates):
    """
    Функция генерации МКРЦ.
    :param info: dict
        данные о аттрибутах мкрц необходимые для их отрисовки(width, height etc.)

    :return: список, содержащий результат генерации МКРЦ
    """
    # проверка на наличие МКРЦ
    if info["num"] <= 0:
        return [], []

    # генерация  координат МКРЦ пары в зависимости от направления прегона
    # ----------------------------------------------------------------------------------------------------
    if general["direct"] == 0:  # слева направо

        # генерация  координат МКРЦ пары в зависимости от стартового РЦ
        if info["start_rc"] == 0:  # 1-ое РЦ
            mkrc_coordinates = coordinates[1::2]
        else:                      # 2-ое РЦ
            mkrc_coordinates = coordinates[2::2]
    else:                       # справа налево

        # генерация  координат МКРЦ пары в зависимости от стартового РЦ
        if info["start_rc"] == 0:  # 1-ое РЦ
            mkrc_coordinates = coordinates[::2]
        else:                      # 2-ое РЦ
            mkrc_coordinates = coordinates[1:-1:2]
    # ----------------------------------------------------------------------------------------------------

    # задание границ для МКРЦ от направления прегона
    # ----------------------------------------------------------------------------------------------------
    if general["direct"] == 0:
        rc_edges = [coordinates[1], coordinates[-1]]
    else:
        rc_edges = [coordinates[0], coordinates[-2]]
    # ----------------------------------------------------------------------------------------------------

    mkrc_coordinates = mkrc_coordinates[:info["num"]]

    generated_mkrc = []
    mkrc_nums = []
    # цикл для присваивания параметров МКРЦ
    for i, coordinate_x in enumerate(mkrc_coordinates):
        # инициализация временной переменой МКРЦ для шага генерации
        mkrc = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '']

        mkrc[0] = str(general["coordinates"][1] + info["upper_margin"])  # сдвиг по Y
        mkrc[2] = info["height"]
        mkrc[3] = info["width"]
        mkrc[8] = general["set_num"]  # номер комплекта
        mkrc[9] = str(i + 1)          # номер МКРЦ
        mkrc[10] = '2'                # увязка (номерация РЦ)
        # 9 - номер мкрц и 10 - привязка к рц

        # одиночная/пара МКРЦ
        if coordinate_x in rc_edges:  # одиночная МКРЦ

            # центрирование абсциссы
            shift_x = round(int(info["width"]) / 2)
            mkrc[1] = str(coordinate_x - shift_x)

            # сохранение данных по одиночному МКРЦ (параметры, номер)
            mkrc_nums.append(str(i + 1))
            generated_mkrc.append(';'.join(mkrc))

        else:  # парное МКРЦ
            mkrc_1 = mkrc.copy()
            mkrc_1[10] = '1'      # увязка (номерация РЦ)

            mkrc_2 = mkrc.copy()

            # вычисление абсцисс для левой и правой МКРЦ одной пары
            x = int(coordinate_x)
            left_x = str(x - int(info["width"]) - 1)
            right_x = str(x + 1)

            # сдвиг элемента пары МКРЦ в зависимости от направления
            if general["direct"] == 0:  # слева направо
                mkrc_1[1], mkrc_2[1] = left_x, right_x
            else:                       # справа налево
                mkrc_1[1], mkrc_2[1] = right_x, left_x

            # сохранение данных по 1-му элементу пары МКРЦ (параметры, номер)
            generated_mkrc.append(';'.join(mkrc_1))
            mkrc_nums.append(str(i + 1))

            # сохранение данных по 2-му элементу пары МКРЦ (параметры, номер)
            generated_mkrc.append(';'.join(mkrc_2))
            mkrc_nums.append(str(i + 1))

    return generated_mkrc, mkrc_nums


def _set_rc_mkrc_linking(rc_arrays_list, mkrc_nums):
    print(mkrc_nums)
    print(rc_arrays_list)

    # проверка на наличие МКРЦ
    if not mkrc_nums:
        return [';'.join(rc) for rc in rc_arrays_list]

    # РЦ без увязки (правый конец)
    not_linked_rc = ['0'] * (len(rc_arrays_list) - len(mkrc_nums) - 2)

    # создание списка для увязки по нумрации
    rc_linking_list_nums = mkrc_nums + not_linked_rc  # [РЦ с увязкой] + [оставшиеся РЦ]

    # создание списка для увязки по нумрации в паре МКРЦ
    pair_nums = ['2' if num not in mkrc_nums[i + 1:] else '1' for i, num in enumerate(mkrc_nums)]
    rc_linking_list_pairs = pair_nums + not_linked_rc

    border_rc = [rc_arrays_list[0], rc_arrays_list[-1]]
    rc_strings_list = [';'.join(rc) for rc in border_rc]
    # цикл для заполнения информации об увязке РЦ с МКРЦ
    for mkrc_num, pair_num, rc_array in zip(rc_linking_list_nums, rc_linking_list_pairs, rc_arrays_list[1:-1]):
        rc_array[9] = mkrc_num
        rc_array[10] = pair_num

        rc_strings_list.insert(len(rc_strings_list) - 1, ';'.join(rc_array))

    return rc_strings_list


# def _generate_mgks(info, general, coordinates):
#     """
#     Функция генерации МГКС.
#     :param info: dict
#         данные о аттрибутах рельсовых МГКС необходимые для их отрисовки(width, height etc.)
#     :param general: dict
#         общие сведения о перегоне
#     :param coordinates: dict
#         координаты начал рельсовых цепей для задания координат МГКС
#
#     :return: список, содержащий результат генерации МГКС
#     """
#
#     # генерация координат МГКС
#
#
#     # список для хранения МГКС
#     generated_mgks = []
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



