# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import tabulate
from .abstract_report import AbstractReport


class ConsoleReport(AbstractReport):
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
        self.io_report.write(tabulate.tabulate(self.data_report, self.headers))

    def make_report(self):
        """
        Сформировать отчёт
        """
        print(self.io_report.getvalue())
