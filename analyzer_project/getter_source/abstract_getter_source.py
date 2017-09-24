# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import os

from abc import ABCMeta, abstractmethod
from tempfile import gettempdir
from uuid import uuid4


class AbstractGetterSource:
    __metaclass__ = ABCMeta

    def __init__(self):
        self.dir_tmp = gettempdir()

    @abstractmethod
    def _get_source(self, repo_url, repo_dir):
        """
        абстракция получение репозитория из repo_url в локальный repo_dir
        :param repo_url: url репозитория
        :param repo_dir: каталог для сохранения репозитория
        """

    def get_source(self, repo_url):
        """
        Получить репозиторий
        :param repo_url: url репозитория
        :return: каталог с локальным репозиторием
        """
        repo_dir = os.path.join(self.dir_tmp, uuid4().hex)
        self._get_source(repo_url, repo_dir)
        return repo_dir
