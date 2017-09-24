# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from nltk import pos_tag


def is_parts_of_speech(word, list_part_of_speech_tag):
    """
    Проверяет является ли переданное слово частью речи из списка
    :param word: слово
    :param list_part_of_speech_tag: список тэгов соответствующий части речи
    :return: True если слово является одной из частей речи, представленных в списке тэгов, иначе False
    """
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] in list_part_of_speech_tag
