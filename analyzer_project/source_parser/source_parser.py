# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .python_source_parser import PythonSourceParser


def get_source_parser(type_source):
    """
    Возвращает класс-парсер кода
    :param type_source: тип парсера
    :return: класс
    """
    dict_source_parser = {
        'python': PythonSourceParser
    }
    assert type_source in dict_source_parser, \
        'type_source must be in ({0})'.format(', '.join(dict_source_parser.keys()))
    return dict_source_parser[type_source]


def get_words_from_sources(sources, type_source, types_identificators):
    """
    Получить слова из исходных кодов (генератор)
    :param sources: список исходных кодов
    :param type_source: тип исходного кода (язык)
    :param types_identificators: список типов идентификаторов
    """
    cls_source_parser = get_source_parser(type_source)
    for source in sources:
        source_parser = cls_source_parser(source)
        try:
            for word in source_parser.get_words(types_identificators):
                yield word
        finally:
            del source_parser
