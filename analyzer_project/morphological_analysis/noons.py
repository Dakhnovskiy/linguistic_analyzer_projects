# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .common import is_parts_of_speech


def is_noon(word):
    """
    Проверяет является ли переданное слово существительным
    :param word: слово
    :return: True если слово является существительным, иначе False
    """
    return is_parts_of_speech(word, ['NN'])
