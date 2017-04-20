#!/usr/bin/env python3
"""
Generates text posts from a given corpus
"""
from sys import argv
from pymarkovchain import MarkovChain

if len(argv) != 3:
    print("USAGE: genevabot.py CORPUS NUMBER")
    exit(1)

FILENAME = argv[1]
NUMBER = int(argv[2])

BOT = MarkovChain(FILENAME)

VALID_SENTENCES = 0
while VALID_SENTENCES < NUMBER:
    SENTENCE = BOT.generateString()
    if len(SENTENCE.split()) < 3:
        continue
    VALID_SENTENCES += 1
    print(SENTENCE)
