# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'


class SaveIoToFileMixin:

    def save_to_file(self):
        """
        сохраняет из иостроки в файл
        """
        with open(self.file_name, 'w') as file:
            file.write(self.io_report.getvalue())
