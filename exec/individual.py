#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выполнить индивидуальное задание 2 лабораторной работы 2.19, добавив аннотации
типов. Выполнить проверку программы с помощью утилиты mypy. Индивидуальное
задание 2 в лабораторной работе 2.19 представляло собой написание консольной
программы, которая при указании пути выводит список всех документов и
каталогов на указанной глубине (уровне).
"""

import os
import argparse


def tree(path: str, level: int, max_levels: int, show_hidden: bool) -> None:
    """
    Вывод списка каталогов и файлов по указанному пути,
    аналогично утилите tree в ОС Linux.

    Аргументы:
        path (str): Путь к директории.
        level (int): Уровень глубины для вывода.
        max_levels (int): Максимальный уровень глубины.
        show_hidden (bool): Флаг для отображения скрытых файлов.
    """
    if level > max_levels:
        return

    for element in os.listdir(path):
        if not show_hidden and element.startswith('.'):
            continue

        dir_path = os.path.join(path, element)
        if os.path.isdir(dir_path):
            print('  ' * level + f'/{element}')
            tree(dir_path, level + 1, max_levels, show_hidden)
        else:
            print('  ' * level + element)


def main() -> None:
    """
    Основная функция для обработки аргументов командной строки
    и вызова функции tree.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help="Директория"
    )

    parser.add_argument(
        '-l',
        '--level',
        type=int,
        default=float('inf'),
        help="Максимальный уровень глубины"
    )

    parser.add_argument(
        '-a',
        '--all',
        action='store_true',
        help="Вывод скрытых файлов"
    )

    parser.add_argument(
        '--author',
        nargs='?',
        help="Вывод автора программы"
    )

    args = parser.parse_args()

    if args.author:
        print("> Автор работы: Иващенко О.А.\n")
        return

    path = os.path.abspath(args.directory)
    if not os.path.exists(path):
        print("Указанного каталога не существует")
        return

    if not os.path.isdir(path):
        print(f"Ошибка: {path} - не каталог")
        return

    print(f'Список файлов в каталоге {path}')
    tree(path, 0, args.level, args.all)


if __name__ == "__main__":
    main()
