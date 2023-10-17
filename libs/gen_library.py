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

    rc_list, _ = _generate_rc(info["rc"], info["general"])

    return {"rc": rc_list,"mgks": rc_list,"mkrc": rc_list,"uksps": rc_list,"arrow": rc_list,"ind": rc_list}


def _generate_rc(info, general):
    """
    Функция генерации рельсовых цепей.
    :param info: dict
        данные о аттрибутах рельсовых цепей необходимые для их отрисовки(width, height etc.)

    :return: список, содержащий результат генерации РЦ и список координат РЦ
    """
    # список для хранения РЦ
    generated_rc = []
    rc_coordinates = []

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

    # цикл добавления цепи в "generated_rc"
    for i, (name, width) in enumerate(details.items()):

        # инициализация временной переменой РЦ для шага генерации
        rc = ['0', '0', '20', '40', 'Имя', '1', '0', '0', '0', '0', '0', '0', '0', '0', '']

        # запись параметров РЦ
        rc[0] = str(general["coordinates"][1])              # сдвиг по X
        rc[1] = str(general["coordinates"][0] + shifts[i])  # сдвиг по Y
        rc[2] = info["height"]
        rc[3] = width
        rc[4] = name
        rc[8] = general["set_num"]                       # номер комплекта
        rc[12] = str(i + 1)                              # номер РЦ

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

        generated_rc.append(';'.join(rc))

    return generated_rc, shifts


def _generate_mgks(info):
    return None


def _generate_mkrc(info):
    return None


def _generate_uksps(info):
    return None


def _generate_arrow(info):
    return None


def _generate_ind(info):
    return None



