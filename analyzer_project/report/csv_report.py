# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .abstract_report import AbstractReport


class CsvReport(AbstractReport):
    def __init__(self, data_report):
        """
        :param data_report: данные отчета
        """

        super().__init__(data_report)

    def make_report(self):
        """
        Сформировать отчёт
        """
        pass
