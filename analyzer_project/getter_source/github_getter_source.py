# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .abstract_getter_source import AbstractGetterSource
from git import Repo


class GithubGetterSource(AbstractGetterSource):

    def __init__(self):
        super(GithubGetterSource).__init__(self)

    def _get_source(self, repo_url, repo_dir):
        """
        получение репозитория из repo_url в локальный repo_dir
        :param repo_url: url репозитория
        :param repo_dir: каталог для сохранения репозитория
        """
        Repo.clone_from(repo_url, repo_dir)
