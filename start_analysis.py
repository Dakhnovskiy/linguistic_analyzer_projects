# -*- coding: utf-8 -*-
__author__ = 'Dmitriy.Dakhnovskiy'

import argparse
from analyzer_project.source_getter.source_getter import get_source_getter


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--repo', help='link to repository')
    args = parser.parse_args()

    source_getter = get_source_getter('github')()
    try:
        repo_dir = source_getter.get_source(args.repo)
        print(repo_dir)
    finally:
        del source_getter
