# -*- coding: utf-8 -*-

import collections


def get_top_words(words):
    """
    Получить список наиболее часто встречающихся слов, с указанием частоты
    :param words: список слов для анализа
    :return: [(слово1, количество повторений слова1), ..]
    """
    return collections.Counter(words).most_common()
