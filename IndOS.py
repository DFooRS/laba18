#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


if __name__ == "__main__":
    """
    Программа создаёт папку в текущей директории
    Если папка существует, выводит сообщение
    """
    name = input("Enter folder name: ")
    if os.path.exists(name):
        print("This folder exists")
    else:
        os.mkdir(f"{name}")
        print(f'Folder "{name}" was created')
