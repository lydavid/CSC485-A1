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
from argparse import ArgumentParser as _Parser

# nltk uses "lazy loading," so importing nltk directly rather than using
# relative imports is not terribly slow
import nltk

def main(args=None):
    grammar1 = nltk.data.load('file:ex1.cfg')
    sent = "Joe frightened the angry bear".split()
    rd_parser = nltk.RecursiveDescentParser(grammar1)
    for tree in rd_parser.nbest_parse(sent):
        print tree
    

if __name__ == '__main__':
    exit(main())
