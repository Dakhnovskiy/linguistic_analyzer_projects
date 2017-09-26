# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import json
from .abstract_report import AbstractReport
from .save_io_to_file_mixin import SaveIoToFileMixin


class JsonReport(AbstractReport, SaveIoToFileMixin):
    def __init__(self, data_report, headers):
        """
        :param data_report: данные отчета
        :param headers: список заголовков
        """
        super().__init__(data_report, headers)
        self.file_name = 'report.json'

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
        self.save_to_file()
