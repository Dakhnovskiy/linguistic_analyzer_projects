# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import io
import collections
from abc import ABCMeta, abstractmethod


class AbstractReport:
    __metaclass__ = ABCMeta

    def __init__(self, data_report, headers):
        """
        :param data_report: данные отчета
        :param headers: список заголовков
        """

        assert isinstance(data_report, collections.Iterable), 'data_report must be iterable'
        self.data_report = data_report
        self.headers = headers
        self.io_report = io.StringIO()
        self._make_io_report()

    def __del__(self):
        self.io_report.close()

    @abstractmethod
    def _make_io_report(self):
        """
        записывает в io_report отчет в строковом виде
        """

    @abstractmethod
    def make_report(self):
        """
        Сформировать отчёт
        """