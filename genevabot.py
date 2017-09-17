#!/usr/bin/env python3
"""
Generates text posts from a given corpus
"""
from sys import argv
import pymarkovchain
from pymarkovchain import MarkovChain
import argparse

PARSER = argparse.ArgumentParser(
        description="Generate Tumblr posts from a Markov chain database.")
PARSER.add_argument("filename", metavar="CORPUS", type=str,
        help="The corpus to use in generating text.")
PARSER.add_argument("number", metavar="NUMBER", type=int,
        help="The number of strings to generate.")
PARSER.add_argument('--minlen', metavar="LENGTH", type=int,
        help="Throw out strings shorter than this.", default=3)
PARSER.add_argument('--notags', action="store_true",
        help="Don't generate tags (legacy database compat behaviour)")

ARGS = PARSER.parse_args()

FILENAME = ARGS.filename
NUMBER = ARGS.number

BOT = MarkovChain(FILENAME)

VALID_SENTENCES = 0
while VALID_SENTENCES < NUMBER:
    SENTENCE = BOT.generateString()
    if len(SENTENCE.split()) < ARGS.minlen:
        continue
    VALID_SENTENCES += 1
    print(SENTENCE)

    if not ARGS.notags:
        try:
            TAGS=BOT.generateStringWithSeed("#")
            print(TAGS)    
            print(" --- ")
        except pymarkovchain.StringContinuationImpossibleError as e:
            print("[FATAL] Your database does not have tag data.")
            print("You can still generate posts without tags using --notags")
            import sys
            sys.exit(1)
    
