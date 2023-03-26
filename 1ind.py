#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    with open("TextInd1.txt", "r", encoding="utf-8") as fileptr:
        sentences = str(fileptr.readlines())
        sentences = sentences[2:(len(sentences)-2)]

        while len(sentences) > 1:
            n = sentences.find('.')
            if sentences[1] == ' ':
                print(sentences[:n+1])
            sentences = sentences[n+2:]
