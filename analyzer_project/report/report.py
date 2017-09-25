# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .console_report import ConsoleReport
from .json_report import JsonReport
from .csv_report import CsvReport


dict_formats_report = {
    'console': ConsoleReport,
    'json': JsonReport,
    'csv': CsvReport
}


def get_cls_report(format_report):
    """
    Возвращает класс-генератор отчёта
    :param format_report: формат отчета
    :return: класс
    """

    assert format_report in dict_formats_report, \
        'format_report must be in ({0})'.format(', '.join(dict_formats_report.keys()))
    return dict_formats_report[format_report]


def make_report(data_report, format_report, headers):
    """
    Формирует отчет
    :param data_report: данные отчета
    :param format_report: формат отчета
    :param headers: список заголовков
    """
    report = get_cls_report(format_report)(data_report, headers)
    report.make_report()
