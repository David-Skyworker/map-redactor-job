from copy import copy

from libs import config


def generate_way(info):
    """
        Функция генерации перегона.
        :param info:
            словарь, содержащий данные для генерации объектов программой, таких как РЦ, МГКС, МКРЦ и т.д.

        :return: словарь, содержащий полную информацию о сгенерированном перегоне в соответствующим формате для
        сохранения в .ini файл.
    """
    _adjust_margins(info)

    rc_list, rc_coordinates, mkrc_shift_y = _generate_rc(info.rc, info.general)

    mkrc_list, mkrc_nums = _generate_mkrc(info.mkrc_info, info.general, rc_coordinates)

    rc_list = _set_rc_mkrc_linking(rc_list, mkrc_nums)

    mgks_list = _generate_mgks(info.mgks, info.general, rc_coordinates)

    arrow, ind_start, arrow_height = _generate_arrow(info.arrow, info.general, rc_list[0])

    ind_list = _generate_ind(info.ind, info.general, ind_start, arrow_height)

    return {"rc": rc_list, "mkrc": mkrc_list, "mgks": mgks_list, "uksps": rc_list, "arrow": arrow, "ind": ind_list}


def _adjust_margins(info):
    """
        Функция настройки отступов МКРЦ и МГКС от ближайших к ним элементов на оступы от координат,
        заданных в пользовательском интерфейсе.
        :param info: dict
            данные о аттрибутах мкрц необходимые для их отрисовки(width, height etc.)
    """
    mkrc = info.mkrc
    rc = info.rc
    mgks = info.mgks

    mkrc_margin = mkrc.upper_margin + rc.height
    mgks_margin = mgks.upper_margin + mkrc_margin + mkrc.height

    mkrc.upper_margin, mgks.upper_margin = mkrc_margin, mgks_margin


def _generate_rc(info, general):
    """
    Функция генерации рельсовых цепей.
    :param info: dict
        данные о аттрибутах рельсовых цепей необходимые для их отрисовки(width, height etc.)

    :return: список, содержащий результат генерации РЦ и список координат РЦ
    """

    # словарь с именами и длиннами уже создан
    rc_names = config.details["rc"]["name"]
    rc_widths = config.details["rc"]["width"]

    # генерация сдвигов рельсовых цепей в относительно начальной точки зависимости от напраления
    if general.direct == 0:
        # слева направо
        shifts = [0] + [sum(rc_widths[0:i + 1]) for i in range(info.num - 1)]
    else:
        # справа налево
        shifts = [-sum(rc_widths[0:i + 1]) for i in range(info.num)]

    # список для хранения РЦ
    generated_rc = []
    coordinates = []

    # цикл добавления цепи в "generated_rc"
    for i, (name, width) in enumerate(zip(rc_names, rc_widths)):

        # инициализация временной переменой РЦ для шага генерации
        rc = ['0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '']

        # запись параметров РЦ
        coords = general.coordinates

        rc[0] = coords.y              # сдвиг по Y
        rc[1] = coords.x + shifts[i]  # сдвиг по X
        rc[2] = info.height
        rc[3] = width
        rc[4] = name
        rc[8] = general.set_num
        rc[12] = i + 1                                 # номер рц

        # настройка параметров боковых и внутренних РЦ
        if i + 1 not in [1, info.num]:
            # настройка внутренних РЦ
            rc[11] = int(general.reserved)         # резервирование
        elif i + 1 == info.num:
            # настройка увязки конечной РЦ
            rc[9] = 64
            rc[13] = 2
        elif i == 0:
            # настройка увязки начальной РЦ в зависимости от типа интерфейса
            if general["interface"] == 0:
                # релейный интерфейс
                rc[13] = 1
            else:
                # цифровой интерфейс
                rc[13] = 3

        coordinates.append(rc[1])

        rc = [str(attribute) for attribute in rc]
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
        if info["start_rc"]:  # 1-ое РЦ
            mkrc_coordinates = coordinates[1::2]
        else:                      # 2-ое РЦ
            mkrc_coordinates = coordinates[2::2]
    else:                       # справа налево

        # генерация  координат МКРЦ пары в зависимости от стартового РЦ
        if info["start_rc"]:  # 1-ое РЦ
            mkrc_coordinates = coordinates[:-1:2]
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

        mkrc[0] = general["coordinates"][1] + info["upper_margin"]  # сдвиг по Y
        mkrc[2] = info["height"]
        mkrc[3] = info["width"]
        mkrc[8] = general["set_num"]              # номер комплекта
        mkrc[9] = i + 1                           # номер МКРЦ
        mkrc[10] = 2                              # увязка (номерация РЦ)
        mkrc[11] = int(general["reserved"])       # резервирование

        # одиночная/пара МКРЦ
        if coordinate_x in rc_edges:  # одиночная МКРЦ

            # центрирование абсциссы
            shift_x = round(info["width"] / 2)
            mkrc[1] = coordinate_x - shift_x

            # сохранение данных по одиночному МКРЦ (параметры, номер)
            mkrc_nums.append(str(i + 1))
            mkrc = [str(attribute) for attribute in mkrc]
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
            mkrc_1 = [str(attribute) for attribute in mkrc_1]
            generated_mkrc.append(';'.join(mkrc_1))
            mkrc_nums.append(str(i + 1))

            # сохранение данных по 2-му элементу пары МКРЦ (параметры, номер)
            mkrc_2 = [str(attribute) for attribute in mkrc_2]
            generated_mkrc.append(';'.join(mkrc_2))
            mkrc_nums.append(str(i + 1))

    return generated_mkrc, mkrc_nums


def _set_rc_mkrc_linking(rc_arrays_list, mkrc_nums):
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


def _generate_mgks(info, general, coordinates):
    """
        Функция генерации МГКС.
        :param info: dict
            данные о аттрибутах рельсовых МГКС необходимые для их отрисовки(width, height etc.)
        :param general: dict
            общие сведения о перегоне
        :param coordinates: dict
            координаты начал рельсовых цепей для задания координат МГКС

        :return: список, содержащий результат генерации МГКС
    """

    # проверка на наличие МГКС
    if info["num"] <= 0:
        return []

    # генерация  координат МГКС
    # ----------------------------------------------------------------------------------------------------
    # сдвиги и конечные координаты МКРЦ в зависимости от направления перегона
    if general["direct"] == 0:
        start_rc_shift = 1         # свиг стартового РЦ
        end_rc = len(coordinates)  # последняя РЦ
    else:
        start_rc_shift = 0         # свиг стартового РЦ
        end_rc = -1                # предпоследняя РЦ

    # генерация координат МКРЦ в зависимости от паттерна их расположения

    shift_layer_1 = int(not info["start_rc"])
    shift_layer_2 = int(info["start_rc"])
    if info["pattern"]:  # паттерн - "подряд"

        start_rc = start_rc_shift + shift_layer_1  # 1-ое РЦ
        mgks_coordinates = coordinates[start_rc:end_rc]

    else:  # паттерн - "через одну РЦ"

        # второй слой накладывается на пропуски первого

        first_layer_start = shift_layer_1 + start_rc_shift            # 1-ое РЦ : |1 или 0|
        second_layer_start = shift_layer_2 + start_rc_shift  # 1-ое РЦ : |0 или 1|

        mgks_coordinates = coordinates[first_layer_start:end_rc:2] + coordinates[second_layer_start:end_rc:2]

    mgks_coordinates = list(map(int, mgks_coordinates[:info["num"]]))
    # ----------------------------------------------------------------------------------------------------

    # список для хранения МГКС
    generated_mgks = []
    for i, coordinate_x in enumerate(mgks_coordinates):

        # инициализация временной переменой МГКС для шага генерации
        mgks = ['0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '']

        # запись параметров МГКС
        mgks[0] = general["coordinates"][1] + info["upper_margin"]  # координта по Y
        shift_x = round(info["width"] / 2)
        mgks[1] = coordinate_x - shift_x     # координта по X
        mgks[2] = info["height"]
        mgks[3] = info["width"]
        mgks[4] = "МГКС " + str(i + 1)            # наименование
        mgks[9] = general["set_num"]              # номер комплекта
        mgks[10] = i + 1                          # номер МГКС
        mgks[11] = int(general["reserved"])       # резервирование

        mgks = [str(attribute) for attribute in mgks]
        generated_mgks.append(';'.join(mgks))

    return generated_mgks


def _generate_arrow(info, general, first_rc):

    """
    Функция генерации стрелы направления.
    :param info: dict
        данные о аттрибутах рельсовых стрелы направления необходимые для ее отрисовки(width, height etc.)
    :param general: dict
        общие сведения о перегоне
    :param first_rc: dict
        координаты начал рельсовых цепей для задания координат МГКС

    :return: список, содержащий результат генерации МГКС
    """

    # преобразование от строки к массиву
    first_rc = first_rc.split(';')

    # проверка: требуется стрелка или нет
    if not info["exists"]:
        return [], int(first_rc[1]), info["height"]

    # инициализация переменой стрелки
    arrow = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '']

    # координта по Y
    arrow[0] = general["coordinates"][1] - info["height"] - general["rc_arrow_margin"]

    # центрирование стрелки относительно 1-ой РЦ
    differ = int(first_rc[3]) - info["width"]
    shift_x = round(differ / 2)
    arrow[1] = int(first_rc[1]) + shift_x   # координта по X

    arrow[2] = info["height"]
    arrow[3] = info["width"]
    arrow[7] = general["set_num"]      # номер комплекта
    arrow[8] = general["direct"]       # направление

    if general["direct"] == 0:
        ind_start = arrow[1] + info["width"] + 5
    else:
        ind_start = arrow[1] - 5

    arrow = [str(attribute) for attribute in arrow]
    return [';'.join(arrow)], ind_start, info["height"]


def _generate_ind(info, general, ind_start, arrow_height):
    """
            Функция генерации индикаторов.
            :param info: dict
                данные о аттрибутах индикаторов необходимые для их отрисовки(width, height etc.)
            :param general: dict
                общие сведения о перегоне
            :param ind_start: int
                координаты начала индификаторов
            :param arrow_width: int
                высота стрелки для центрирования индикаторов относительно нее

            :return: список, содержащий результат генерации МГКС
        """

    # проверка на наличие индикаторов
    if not sum(config.details["ind"].values()):
        return []

    # генерация  координат индикаторов
    # ----------------------------------------------------------------------------------------------------
    # сдвиги и конечные координаты индикаторов в зависимости от направления перегона
    ind_num = sum(config.details["ind"].values())  # число индикаторов
    shift = int(info["width"])
    if general["direct"] == 0:
        ind_coordinates = [ind_start + shift * i for i in range(ind_num)]
    elif general["direct"] == 1:
        ind_coordinates = [ind_start - shift * (i + 1) for i in range(ind_num)]
    # ----------------------------------------------------------------------------------------------------

    ind_nums = [i + 1 for i, val in enumerate(config.details["ind"].values()) if val]
    # список для хранения МГКС
    generated_inds = []
    for num, coordinate_x in zip(ind_nums, ind_coordinates):
        # инициализация временной переменой индикатора для шага генерации
        ind = ['0', '0', '0', '0', '0', '0', '']

        # запись параметров МГКС
        height = info["height"]
        arrow_center_alignment = round((arrow_height - height) / 2) + height
        ind[0] = general["coordinates"][1] - general["rc_arrow_margin"] - arrow_center_alignment  # координта по Y
        ind[1] = coordinate_x  # координта по X
        ind[2] = height
        ind[3] = info["width"]
        ind[4] = num                # номер, соответствующий значению индикатора
        ind[5] = general["set_num"]  # номер комплекта

        ind = [str(attribute) for attribute in ind]
        generated_inds.append(';'.join(ind))

    return generated_inds


def _generate_uksps(info):
    return None



