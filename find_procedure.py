# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

from pprint import pprint
import os


def find_files(files_list):
    while True:
        short_files_list = []
        search_string = input('Введите строку для поиска:')
        for file in files_list:
            with open(file, 'rt') as reading_file:
                for line in reading_file:
                    if search_string in line:
                        short_files_list.append(file)
                        break
        pprint(short_files_list)
        print('Всего:', len(short_files_list))
        if len(short_files_list) <= 1:
            return
        else:
            find_files(short_files_list)


migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
search_dir = os.path.join(current_dir, migrations)
os.chdir(search_dir)
sql_files = list()
sql_files = [f for f in os.listdir(search_dir) if f.endswith('.sql')]

find_files(sql_files)
