# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .github_source_getter import GithubSourceGetter


def get_source_getter(type_repo):
    """
    Возвращает класс для получения репозитория
    :param type_repo: тип репозитория
    :return: класс
    """
    dict_source_getter = {
        'github': GithubSourceGetter
    }
    assert type_repo in dict_source_getter, 'type_repo must be in ({0})'.format(', '.join(dict_source_getter.keys()))
    return dict_source_getter[type_repo]
