# -*- coding: utf-8 -*-

import os


def find_files(path):
    """
    Находит файлы в заданном каталоге и его подкаталогах
    :param path: каталог для поиска
    :return: генератор (каталог, имя файла)
    """
    for dir_name, _, files in os.walk(path, topdown=True):
        for file_name in files:
            yield dir_name, file_name


def find_files_by_extension(path, file_ext=None):
    """
    Находит файлы с заданным расширением в заданном каталоге
    :param path: каталог для поиска
    :param file_ext: расширение файла (по умолчанию = .py)
    :return: генератор
    """
    if file_ext is None:
        file_ext = '.py'

    for dir_name, file_name in find_files(path):
        if file_name.endswith(file_ext):
            yield os.path.join(dir_name, file_name)
