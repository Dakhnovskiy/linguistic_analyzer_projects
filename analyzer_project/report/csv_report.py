# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import csv
from .abstract_report import AbstractReport
from .save_io_to_file_mixin import SaveIoToFileMixin


class CsvReport(AbstractReport, SaveIoToFileMixin):

    def __init__(self, data_report, headers):
        """
        :param data_report: данные отчета
        :param headers: список заголовков
        """
        super().__init__(data_report, headers)
        self.file_name = '/tmp/tmp.csv'

    def __del__(self):
        super().__del__()

    def _make_io_report(self):
        """
        записывает в io_report отчет в строковом виде
        """
        writer = csv.writer(self.io_report, delimiter=' ')
        writer.writerow(self.headers)
        writer.writerows(self.data_report)

    def make_report(self):
        """
        Сформировать отчёт
        """
        self.save_to_file()
