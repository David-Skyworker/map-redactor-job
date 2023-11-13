import re


class TableContent:
    def __init__(self, parameters):
        # генеративные данные
        self.row_number = parameters["number"]
        self.start_name = parameters["start_name"]
        self.width = parameters["width"]
        self.is_index_increase = parameters["index_pattern"] == 0

        # составные части данных
        self.prefix = ""
        self.start_number = 0

        self.content = {0: ["НАЧАЛО"], 1: []}
        self._generate_content()

    def _generate_content(self):
        self._get_generated_names()
        self._get_widths()

    def _get_generated_names(self):
        self._get_name_parameters()
        self._generate_names()

    def _get_name_parameters(self):
        name_parts = re.split(r"(\d{1,2}П)", self.start_name)
        self.prefix = name_parts[0]
        self.start_number = int(name_parts[1][:-1])

    def _generate_names(self):
        for inner_num in range(self.row_number - 2):
            self._generate_inner_name(inner_num)
        self.content[0].append("КОНЕЦ")

    def _generate_inner_name(self, rc_number):
        index = self._count_index(rc_number)
        name = self.prefix + str(index) + "П"
        self.content[0].append(name)

    def _count_index(self, rc_number):
        if self.is_index_increase:
            index = self.start_number + 2 * rc_number
        else:
            index = self.start_number - 2 * rc_number

        if index <= 0:
            index = "???"
        return index

    def _get_widths(self):
        widths = [self.width] * self.row_number
        self.content[1] = widths

