# -*- coding: utf-8 -*-

import ast


def get_content_files(file_names):
    """
    Получает контент списка файлов
    @param file_names: список файлов (итерируемый объект)
    @return: генератор
    """
    for file_name in file_names:
        with open(file_name, 'r', encoding='utf-8') as attempt_handler:
            file_content = attempt_handler.read()
        yield file_content


def get_source_trees(contents):
    """
    Получить синтаксические деревья по списку контентов
    @param contents: список контентов (итерируемый объект)
    @return: генератор
    """
    for file_content in contents:
        try:
            tree = ast.parse(file_content)
            yield tree
        except SyntaxError:
            pass


def get_names_functions_from_tree(tree):
    """
    Получить список имён функций из ast-объекта (генератор)
    @param tree: дерево синтаксического разбора
    @return генератор
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            yield node.name.lower()


def get_names_functions_without_magic(names_functions):
    """
    Получить из списка имён функций список не магических имён функций
    @param names_functions: список имён функций
    @return генератор
    """
    for name_function in names_functions:
        if not (name_function.startswith('__') and name_function.endswith('__')):
            yield name_function


def get_names_functions_without_magic_from_trees(trees):
    """
    Получить список имён функций(без магических) из ast-объектов (генератор)
    @param trees: итерируемый объект из деревьев синтаксического разбора
    """
    for tree in trees:
        for name_function in get_names_functions_without_magic(get_names_functions_from_tree(tree)):
            yield name_function

