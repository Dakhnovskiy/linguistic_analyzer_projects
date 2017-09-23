# -*- coding: utf-8 -*-

import os


def find_files(path):
    """
    Находит файлы в заданном каталоге и его подкаталогах
    @param path: каталог для поиска
    @return: генератор (каталог, имя файла)
    """
    for dir_name, _, files in os.walk(path, topdown=True):
        for file_name in files:
            yield dir_name, file_name


def find_files_by_extension(path, file_ext=None):
    """
    Находит файлы с заданным расширением в заданном каталоге
    @param path: каталог для поиска
    @param file_ext: расширение файла (по умолчанию = .py)
    @return: генератор
    """
    if file_ext is None:
        file_ext = '.py'

    for dir_name, file_name in find_files(path):
        if file_name.endswith(file_ext):
            yield os.path.join(dir_name, file_name)


def find_limited_count_files_by_extension(path, file_ext=None, max_count_files=100):
    """
    Находит ограниченное количество файлов с заданным расширением в заданном каталоге
    @param path: каталог для поиска
    @param file_ext: расширение файла (по умолчанию = .py)
    @param max_count_files: максимальное количество файлов (по умолчанию = 100)
    @return: список файлов
    """
    count_files = 0
    for file in find_files_by_extension(path, file_ext):
        if count_files == max_count_files:
            break
        count_files += 1
        yield file
