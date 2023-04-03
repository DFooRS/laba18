#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    with open("TextInd1.txt", "r", encoding="utf-8") as fileptr:
        ftext = fileptr.readlines()

    sentences = ','.join(ftext)
    parts = sentences.split('. ')
    other_sent = ""
    for i, item in enumerate(parts):
        if item[1] == ' ':
            print(item)
        else:
            other_sent += (item + "\n")
    print(other_sent)
