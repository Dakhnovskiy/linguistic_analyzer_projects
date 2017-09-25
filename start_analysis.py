# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import argparse
import shutil
import os
from analyzer_project.source_getter.source_getter import get_source_getter
from analyzer_project.files_find import find_files_by_extension
from analyzer_project.files_read import get_content_files
from analyzer_project.source_parser.source_parser import get_words_from_sources
from analyzer_project.morphological_analysis.filters import filter_by_parts_of_speech
from analyzer_project.morphological_analysis.analyzer import get_top_words
from analyzer_project.report.report import dict_formats_report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repo', required=True, help='link to repository')
    parser.add_argument('-f', '--func', action='store_true', help='analyse functions')
    parser.add_argument('-v', '--var', action='store_true', help='analyse variables')
    parser.add_argument('-vb', '--verb', action='store_true', help='analyse verbs')
    parser.add_argument('-nn', '--noon', action='store_true', help='analyse noons')
    parser.add_argument('-rt', '--reptype', choices=dict_formats_report.keys(), default='console', help='report type')

    args = parser.parse_args()

    types_identificators = []
    if args.func:
        types_identificators.append('function')
    if args.var:
        types_identificators.append('variable')

    parts_of_speech = []
    if args.verb:
        parts_of_speech.append('verb')
    if args.noon:
        parts_of_speech.append('noon')

    source_getter = get_source_getter('github')()
    try:
        repo_dir = source_getter.get_source(args.repo)
        try:
            files = find_files_by_extension(repo_dir, file_ext='.py')
            files_content = get_content_files(files)
            words = get_words_from_sources(files_content, 'python', types_identificators)
            words_filtered = filter_by_parts_of_speech(words, parts_of_speech)
            top_words = get_top_words(words_filtered)

        finally:
            if os.path.exists(repo_dir):
                shutil.rmtree(repo_dir)
    finally:
        del source_getter
