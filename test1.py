#! /usr/bin/env python3.5
"""Test"""

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
    grammar1 = nltk.grammar.CFG.fromstring("""
    S -> NP VP
    NP -> Det Nom | PropN
    Nom -> Adj Nom | N
    VP -> V Adj | V NP | V S | V NP PP
    PP -> P NP
    PropN -> 'Buster' | 'Chatterer' | 'Joe'
    Det -> 'the' | 'a'
    N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
    Adj -> 'angry' | 'frightened' | 'little' | 'tall'
    V -> 'chased' | 'saw' | 'said' | 'thought' | 'was' | 'put'
    P -> 'on'
    """)
    sent = 'Joe frightened the angry bear'.split()
    rd = nltk.RecursiveDescentParser(grammar1)
    for tree in rd.parse(sent): #.nbest_parse(sent):
        print(tree)
    

if __name__ == '__main__':
    main()
