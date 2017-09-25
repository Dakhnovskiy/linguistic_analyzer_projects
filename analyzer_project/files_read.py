# -*- coding: utf-8 -*-


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
