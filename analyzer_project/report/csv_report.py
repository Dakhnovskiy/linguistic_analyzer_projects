# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .abstract_report import AbstractReport


class CsvReport(AbstractReport):
    def __init__(self, data_report, headers):
        """
        :param data_report: данные отчета
        :param headers: список заголовков
        """
        super().__init__(data_report, headers)

    def make_report(self):
        """
        Сформировать отчёт
        """
        pass
