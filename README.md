# linguistic_analyzer_projects
start_analysis.py - скрипт для анализа репозитория на наличие глаголов/существительных в именах функций/переменных функций

usage: start_analysis.py [-h] -r REPO [-f] [-v] [-vb] [-nn]
                         [-rf {console,json,csv}]

optional arguments:
  -h, --help            show this help message and exit
  -r REPO, --repo REPO  link to repository
  -f, --func            analyse functions
  -v, --var             analyse variables
  -vb, --verb           analyse verbs
  -nn, --noon           analyse noons
  -rf {console,json,csv}, --repformat {console,json,csv} report format

Example:
start_analysis.py --repo https://github.com/Dakhnovskiy/linguistic_analyzer_projects -f -nn -vb -rf console