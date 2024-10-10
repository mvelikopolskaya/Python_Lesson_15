# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.

import argparse

parser = argparse.ArgumentParser(description='A script to receive two arguments from the command line')
parser.add_argument('number', metavar='number', type=int, help='Input an integer')
parser.add_argument('text', metavar='text', type=str, help='input a string')
parser.add_argument('--verbose', action='store_true', help='If verbose true, show additional information')
parser.add_argument('--repeat', help='A number of repetitions')
args = parser.parse_args()
args.repeat = 2
# args.verbose = True
if args.verbose:
    print(f'{args = }')

# python .\task_4.py 1 Hello - нормальная работа
# python .\task_4.py Hello Hello - вызов ошибки
# python .\task_4.py -h - вызов справки
