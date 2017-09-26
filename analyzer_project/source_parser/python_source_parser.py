# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import ast
from .abstract_source_parser import AbstractSourceParser


class PythonSourceParser(AbstractSourceParser):

    def __init__(self, source):
        """
        :param source: исходный код
        """
        super().__init__(source)

    @staticmethod
    def _parse_source(source):
        """
        возвращает разобранный в структуру код
        :param source: исходный код
        """
        try:
            parsed_source = ast.parse(source)
        except SyntaxError:
            parsed_source = None

        return parsed_source

    @staticmethod
    def _walk_element(element):
        """
        генератор по элементам разобранной структуры
        :param element: элемент разобранной структуры
        """
        return ast.walk(element)

    @staticmethod
    def _is_variable(element):
        """
        проаверяет является ли элемент структуры переменной
        :param element: элемент
        """
        return isinstance(element, ast.Name) and not isinstance(element.ctx, ast.Load)

    @staticmethod
    def _is_function(element):
        """
        проаверяет является ли элемент структуры функцией
        :param element: элемент
        """
        if isinstance(element, ast.FunctionDef):
            name_function = PythonSourceParser._get_element_name(element)
            return not (name_function.startswith('__') and name_function.endswith('__'))

        return False

    @staticmethod
    def _get_words_from_identificator(identificator):
        """
        получить слова из идентификатора
        :param identificator: идентификатор
        """
        return identificator.split('_')

    @staticmethod
    def _get_element_name(element):
        """
        получить наименование(идентификатор) элемента разобранной структуры
        :param element: элемент структуры
        """
        element_name = None
        if hasattr(element, 'name'):
            element_name = element.name.lower()
        elif hasattr(element, 'id'):
            element_name = element.id.lower()
        return element_name
