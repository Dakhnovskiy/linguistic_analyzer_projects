# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import json
from .abstract_report import AbstractReport


class JsonReport(AbstractReport):
    def __init__(self, data_report, headers):
        """
        :param data_report: данные отчета
        :param headers: список заголовков
        """
        super().__init__(data_report, headers)

    def __del__(self):
        super().__del__()

    def _make_io_report(self):
        """
        записывает в io_report отчет в строковом виде
        """
        data = [dict(zip(self.headers, row_data)) for row_data in self.data_report]
        self.io_report.write(json.dumps(data, indent=4))

    def make_report(self):
        """
        Сформировать отчёт
        """
        print(self.io_report.getvalue())
