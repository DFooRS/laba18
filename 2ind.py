#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":
    cmd = input(': ')
    file_list = []

    if cmd.find("cat") == 0:
        if len(cmd) > 3:
            k = cmd.find(' ')
            cmd = cmd[k+1:]
            file_list = cmd.split()
            print(file_list)
            for i, item in enumerate(file_list):
                with open(item, "r", encoding="utf-8") as fileptr:
                    text = str(fileptr.readlines())
                    print(text)
        else:
            print("Команда введена без аргументов", file=sys.stderr)
    else:
        print("Команда введена неверно", file=sys.stderr)
