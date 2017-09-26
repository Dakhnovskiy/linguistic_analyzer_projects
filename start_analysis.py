# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import argparse
import shutil
import os
import itertools
from analyzer_project.source_getter.source_getter import get_source_getter
from analyzer_project.files_find import find_files_by_extension
from analyzer_project.files_read import get_content_files
from analyzer_project.source_parser.source_parser import get_words_from_sources
from analyzer_project.morphological_analysis.filters import filter_by_parts_of_speech
from analyzer_project.morphological_analysis.analyzer import get_top_words
from analyzer_project.report.report import dict_formats_report, make_report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repo', required=True, help='link to repository')
    parser.add_argument('-f', '--func', action='store_true', help='analyse functions')
    parser.add_argument('-v', '--var', action='store_true', help='analyse variables')
    parser.add_argument('-vb', '--verb', action='store_true', help='analyse verbs')
    parser.add_argument('-nn', '--noon', action='store_true', help='analyse noons')
    parser.add_argument('-rf', '--repformat', choices=dict_formats_report.keys(), default='console',
                        help='report format')

    args = parser.parse_args()

    types_identificators = list(itertools.compress(['function', 'variable'], [args.func, args.var]))
    parts_of_speech = list(itertools.compress(['verb', 'noon'], [args.verb, args.noon]))

    source_getter = get_source_getter('github')()
    try:
        repo_dir = source_getter.get_source(args.repo)
        try:
            files = find_files_by_extension(repo_dir, file_ext='.py')
            files_content = get_content_files(files)
            words = get_words_from_sources(files_content, 'python', types_identificators)
            words_filtered = filter_by_parts_of_speech(words, parts_of_speech)
            top_words = get_top_words(words_filtered)
            make_report(top_words, args.repformat, headers=['word', 'count'])
        finally:
            if os.path.exists(repo_dir):
                shutil.rmtree(repo_dir)
    finally:
        del source_getter
