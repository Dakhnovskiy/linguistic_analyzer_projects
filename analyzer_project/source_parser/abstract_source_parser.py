# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from abc import ABCMeta, abstractmethod


class AbstractSourceParser:
    __metaclass__ = ABCMeta

    @property
    def parsed_source(self):
        """
        разобранная из исходного кода структура
        :return: разобранная из исходного кода структура
        """
        return self.__parsed_source

    def __init__(self, source):
        """
        :param source: исходный код
        """

        self.__type_identificator_funcs = {
            'variable': self._is_variable,
            'functions': self._parse_source
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

    @abstractmethod
    def _walk_parsed_source(self):
        """
        генератор по элементам разобранной структуры
        """

    def __walk_parsed_source(self):
        """
        генератор по элементам разобранной структуры
        """
        if self.__parsed_source:
            for element in self._walk_parsed_source():
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

    def __element_in_types_identificators(self, element, types_identificators):
        """
        Проверяет является ли элемент разобранной структуры одним из типов идентификаторов
        :param element: элемент структуры
        :param types_identificators: список типов идентификаторов для проверки
        :return: true/false
        """
        ret = False
        for type_identificator in types_identificators:
            ret = self.__type_identificator_funcs[type_identificator](element)
            if ret:
                break
        return ret

    def __get_identificators(self, types_identificators):
        """
        генератор по идентификаторам с заданным типом
        :param types_identificators: список типов идентификаторов
        """
        for element in self.__walk_parsed_source():
            if self.__element_in_types_identificators(element, types_identificators):
                yield self._get_element_name(element)

    def get_words(self, types_identificators):
        """
        генератор по словам идентификаторов с заданным типом
        :param types_identificators: список типов идентификаторов
        """
        assert set(types_identificators).issubset(set(self.__type_identificator_funcs.keys())), \
            'types_identificators must be subset ({0})'.format(', '.join(self.__type_identificator_funcs.keys()))

        for identificator in self.__get_identificators(types_identificators):
            for word in self._get_words_from_identificator(identificator):
                yield word
