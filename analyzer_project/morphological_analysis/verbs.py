# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .common import is_parts_of_speech


def is_verb(word):
    """
    Проверяет является ли переданное слово глаголом
    :param word: слово
    :return: True если слово является глаголом, иначе False
    """
    return is_parts_of_speech(word, ['VB'])
