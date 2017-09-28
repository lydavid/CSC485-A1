#! /usr/bin/env python3.5
""" Question 1 Test"""

# Not necessary; good for python 2.7 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import nltk

def attempt_to_parse(sentence, grammar, should_parse=True):

    print()
    head_string = '\n(' + sentence + ')'
    if should_parse:
        head_string = head_string + ' (Should parse)'
    else:
        head_string = head_string + ' (Should not parse)'
    print(head_string + '\n')

    parser = nltk.parse.BottomUpChartParser(grammar)
    for tree in parser.parse(sentence.split()):
        print(tree)


def main():

    with open('q1.cfg', 'r') as afile:
        cfg_string = afile.read()
    grammar = nltk.grammar.CFG.fromstring(cfg_string)

    ###Test Cases###
    attempt_to_parse('people walk their dogs in parks', grammar)

    attempt_to_parse('walk your dogs', grammar)

    attempt_to_parse('who walk their dogs in parks', grammar)
    attempt_to_parse('what will people walk in parks', grammar)
    attempt_to_parse('where should people walk their dogs', grammar)
    attempt_to_parse('should people walk their dogs in parks', grammar)

    attempt_to_parse('what people walk in parks', grammar, should_parse=False)
    attempt_to_parse('what should people walk their dogs in parks', grammar, should_parse=False)
    attempt_to_parse('where walk their dogs in parks', grammar, should_parse=False)
    
    attempt_to_parse('where will people walk their dogs in parks', grammar)

    ###Interrogative who (subject is missing)###
    attempt_to_parse('who saw the dogs under the statues', grammar)

    ###Interrogative what (thing is missing) ###
    attempt_to_parse('what should people walk in parks', grammar)
    attempt_to_parse('what will people saw', grammar)
    attempt_to_parse('what should people saw under red statues', grammar)

    ###Interrogative where (location is missing) ###
    attempt_to_parse('where should people walk their dogs in parks', grammar)
    attempt_to_parse('where will people walk their dogs in parks', grammar)

if __name__ == '__main__':
    main()
