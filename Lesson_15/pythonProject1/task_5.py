# Напишите код, который запускается из командной строки и получает на вход путь
# до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. В процессе сбора сохраните данные в текстовый файл используя
# логирование.
import os
import logging
import argparse
from collections import namedtuple

logging.basicConfig(level=logging.INFO, filename='object_info.log', format='%(asctime)s - %(levelname)s - %(message)s', encoding='utf-8')
logger = logging.getLogger()

# parser = argparse.ArgumentParser(description='A script to gather information about the folder')

ObjectInfo = namedtuple('ObjectInfo', ['file_name', 'extension', 'flag', 'parent_dir'])


def collect_info(directory_path):
    """Собирает информацию о содержимом директории и сохраняет в
    лог."""
    if not os.path.isdir(directory_path):
        raise ValueError(f"Указанный путь {directory_path} не является директорией.")
    # Получаем родительский каталог
    parent_directory = os.path.basename(os.path.abspath(directory_path))
    # Перебираем содержимое директории
    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)
        # Проверяем, является ли элемент директорией
        if os.path.isdir(entry_path):
            file_info = ObjectInfo(file_name=entry, extension=None, flag=True, parent_dir=parent_directory)
        else:
            filename, extension = os.path.splitext(entry)
            file_info = ObjectInfo(file_name=filename, extension=extension.lstrip('.'),
                                   flag=False, parent_dir=parent_directory)
        # Запись в лог
        logging.info(f'{file_info.file_name} | {file_info.extension if file_info.extension else "N/A"} | {"Directory" if file_info.flag else "File"} | {file_info.parent_dir}')


def main():
    """Основная функция для обработки командной строки и сбора
    информации."""
    parser = argparse.ArgumentParser(description="Сбор информации о содержимом директории и запись в лог.")
    parser.add_argument(os.getcwd(), type=str, help="Путь до директории для анализа")
    args = parser.parse_args()
    directory_path = args
    collect_info(directory_path)
    # try:
    #     collect_info(directory_path)
    #     print(
    #         f'Информация о содержимом директории "{directory_path}" успешно записана в файл "directory_contents.log".')
    # except ValueError as e:
    #     (
    #         print(e))


if __name__ == '__main__':
    main()
