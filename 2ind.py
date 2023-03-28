#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    cmd = input(': ')
    parts = cmd.split()
    if parts[0] == 'cat':
        file_list = parts[1:]
        if len(cmd) > 3:
            for i, item in enumerate(file_list):
                with open(item, "r", encoding="utf-8") as fileptr:
                    text = str(fileptr.readlines())
                    print(text)
        else:
            print("Команда введена без аргументов", file=sys.stderr)
    else:
        print("Команда введена неверно", file=sys.stderr)
