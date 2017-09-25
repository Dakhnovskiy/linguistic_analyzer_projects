# -*- coding: utf-8 -*-

import collections
from .morphological_analysis.verbs import get_verbs_from_list_word
from .files_find import find_limited_count_files_by_extension
from .files_read import get_content_files, get_source_trees, get_names_functions_without_magic_from_trees


def get_verbs_from_name_function(name_function):
    """
    Возвращает список глаголов, встречающихся в названии фунции
    @param name_function: название фунции (предполагается что слова в имени функции разделены символом _)
    @return: список строк
    """
    return get_verbs_from_list_word(name_function.split('_'))


def get_verbs_from_names_functions(names_functions):
    """
    Возвращает список глаголов из списка имён функций
    @param names_functions: список названий фунций (предполагается что слова в имени функции разделены символом _)
    @return: генератор
    """
    for name_function in names_functions:
        for verb in get_verbs_from_name_function(name_function):
            yield verb


def get_top_verbs_in_path(path, top_size=10):
    """
    Получить список наиболее часто встречающихся глаголов в именах функций в py-файлах
    @param path: каталог для поиска
    @param top_size: верхнее ограничение на количество возвращаемых элементов
    @return: список глаголов
    """
    names_files = find_limited_count_files_by_extension(path=path, max_count_files=100)
    trees = get_source_trees(get_content_files(names_files))
    names_functions = get_names_functions_without_magic_from_trees(trees)
    verbs = get_verbs_from_names_functions(names_functions)
    return [verb for verb, _ in collections.Counter(verbs).most_common(top_size)]
