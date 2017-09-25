#! /usr/bin/env python3.5
""" Question2 Test"""

# Not necessary; good for python 2.7 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# an example of a relative imports. Generally only import what you're
# using. The 'as _Parser' makes the token "_Parser" refer to the
# 'ArgumentParser' class instead of 'ArgumentParser'. This extra
# aliasing is not really necessary
#from argparse import ArgumentParser as _Parser

# nltk uses "lazy loading," so importing nltk directly rather than using
# relative imports is not terribly slow
import nltk

def main():
    grammar = nltk.grammar.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | NP PP
    VP -> VP PP | V NP PP | V NP
    PP -> P NP
    NP -> 'I'
    Det -> 'the' | 'a'
    N -> 'man'
    V -> 'saw'
    P -> 'in' | 'with'
    N -> 'park' | 'dog' | 'statue'
    Det -> 'my'
    """)
    sent = 'my dog saw a man in the park with a statue'.split()
    sr = nltk.ShiftReduceParser(grammar)
    for tree in sr.parse(sent): #.nbest_parse(sent):
        print(tree)
    

if __name__ == '__main__':
    main()
