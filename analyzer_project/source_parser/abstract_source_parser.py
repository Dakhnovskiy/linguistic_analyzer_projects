# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import itertools
from abc import ABCMeta, abstractmethod


class AbstractSourceParser:
    __metaclass__ = ABCMeta

    def __init__(self, source):
        """
        :param source: исходный код
        """

        self.__type_identificator_funcs = {
            'variable': self.__get_local_variables_from_functions,
            'function': self.__get_functions
        }

        self.__parse_source(source)

    @staticmethod
    @abstractmethod
    def _parse_source(source):
        """
        возвращает разобранный в структуру код
        :param source: исходный код
        """

    def __parse_source(self, source):
        """
        разбирает исходный код, резульат складывает в __parsed_source
        :param source: исходный код
        """
        self.__parsed_source = self._parse_source(source)

    @staticmethod
    @abstractmethod
    def _walk_element(element):
        """
        генератор по элементам переданного элемента
        :param element: элемент разобранной структуры
        """

    def __walk_parsed_source(self):
        """
        генератор по элементам разобранной структуры
        """
        if self.__parsed_source:
            for element in self._walk_element(self.__parsed_source):
                yield element

    @staticmethod
    @abstractmethod
    def _is_variable(element):
        """
        проаверяет является ли элемент структуры переменной
        :param element: элемент
        """

    @staticmethod
    @abstractmethod
    def _is_function(element):
        """
        проаверяет является ли элемент структуры функцией
        :param element: элемент
        """

    def __get_functions(self):
        """
        Генератор по функциям
        """
        for element in self.__walk_parsed_source():
            if self._is_function(element):
                yield element

    def __get_local_variables_from_function(self, function):
        """
        генератор по переменным объявленным внутри функции
        :param function: функция(ast объект)
        """
        for element in self._walk_element(function):
            if self._is_variable(element):
                yield element

    def __get_local_variables_from_functions(self):
        """
        генератор по локальным переменным функций
        """

        # TODO из-за повторного обхода вложенныъ функций приходится выбирать уникальные. Подумать над проблемой
        set_variables = set()
        for function in self.__get_functions():
            for variable in self.__get_local_variables_from_function(function):
                set_variables.add(variable)

        yield from set_variables

    @staticmethod
    @abstractmethod
    def _get_words_from_identificator(identificator):
        """
        получить слова из идентификатора
        :param identificator: идентификатор
        """

    @staticmethod
    @abstractmethod
    def _get_element_name(element):
        """
        получить наименование(идентификатор) элемента разобранной структуры
        :param element: элемент структуры
        """

    def __get_identificators(self, types_identificators):
        """
        генератор по идентификаторам с заданным типом
        :param types_identificators: список типов идентификаторов
        """
        gens = [self.__type_identificator_funcs[types_identificator]() for types_identificator in types_identificators]
        elements = itertools.chain(*gens)
        yield from (self._get_element_name(element) for element in elements)

    def get_words(self, types_identificators):
        """
        генератор по словам идентификаторов с заданным типом
        :param types_identificators: список типов идентификаторов
        """
        assert set(types_identificators).issubset(set(self.__type_identificator_funcs.keys())), \
            'types_identificators must be subset ({0})'.format(', '.join(self.__type_identificator_funcs.keys()))

        for identificator in self.__get_identificators(types_identificators):
            yield from self._get_words_from_identificator(identificator)
