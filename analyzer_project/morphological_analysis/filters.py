# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .noons import is_noon
from .verbs import is_verb


def filter_by_parts_of_speech(words, parts_of_speech):
    """
    отфильтровать список слов по заданным частям речи
    :param words: список слов
    :param parts_of_speech:  список частей речи
    """
    funcs_parts_of_speech = {
        'noon': is_noon,
        'verb': is_verb
    }

    assert set(parts_of_speech).issubset(set(funcs_parts_of_speech.keys())), \
        'parts_of_speech must be subset ({0})'.format(', '.join(funcs_parts_of_speech.keys()))

    for word in words:
        for part_of_speech in parts_of_speech:
            if funcs_parts_of_speech[part_of_speech](word):
                yield word
                break
