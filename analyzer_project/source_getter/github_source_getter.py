# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

from .abstract_source_getter import AbstractSourceGetter
from git import Repo


class GithubSourceGetter(AbstractSourceGetter):

    def __init__(self):
        super().__init__()

    def _get_source(self, repo_url, repo_dir):
        """
        получение репозитория из repo_url в локальный repo_dir
        :param repo_url: url репозитория
        :param repo_dir: каталог для сохранения репозитория
        """
        Repo.clone_from(repo_url, repo_dir)
