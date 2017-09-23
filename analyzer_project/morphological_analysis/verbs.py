# -*- coding: utf-8 -*-

from nltk import pos_tag


def is_verb(word):
    """
    Проверяет является ли переданное слово глаголом
    @param word: слово
    @return: True если слово является глаголом, иначе False
    """
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def get_verbs_from_list_word(list_word):
    """
    Возвращает список глаголов из переданного списка слов
    @param list_word: список слов
    @return: список строк
    """
    return filter(is_verb, list_word)
