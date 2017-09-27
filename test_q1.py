#! /usr/bin/env python3.5
""" Question 1 Test"""

# Not necessary; good for python 2.7 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import nltk

def main():
    grammar = nltk.parse.load_parser('q1.cfg')
    sent = 'people walks their dogs in parks'.split()
    sr = nltk.ShiftReduceParser(grammar)
    for tree in sr.parse(sent): #.nbest_parse(sent):
        print(tree)
    

if __name__ == '__main__':
    main()