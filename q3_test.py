#! /usr/bin/env python3.5
""" Question 1 Test"""

# Not necessary; good for python 2.7 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import nltk

def parse(sentence, grammar, parser, should_parse=True):

    print()

    head_string = '\n(' + sentence + ')'
    if should_parse:
        head_string = head_string + ' (Should parse)'
    else:
        head_string = head_string + ' (Should not parse)'
    print(head_string + '\n')

    # If a sentence is not accepted by our grammar, print: No parses

    for tree in parser.parse_all(sentence.split()):
        print(tree)

def strip_comments(string):

    # Break str up into individual lines
    lines = string.split('\n')

    # Remove all text after %
    stripped_lines = []
    for line in lines:
        head, sep, tail = line.partition('%')
        stripped_lines.append(head)

    # Remerge the list of strings into a single string, adding back in newline to separate lines
    # Do no add back lines that are now the empty string (ie were entirely a comment line)
    stripped_string = ''
    for line in stripped_lines:
        if line != '':
            stripped_string = stripped_string + line + '\n'

    return stripped_string



def main():
    
    #cfg_string = ''
    # Import grammar from Grammar file
    with open('Grammar', 'r') as afile:
        cfg_grammar = afile.read()

    # Import lexicon from Lexicon file and append it to our string
    with open('Lexicon', 'r') as afile:
        cfg_lexicon =  afile.read()
    cfg_string = cfg_grammar + '\n' + cfg_lexicon
    print(cfg_string)
    commentless_cfg_string = strip_comments(cfg_string)
    print(commentless_cfg_string)
    # Build our grammar for testing
    grammar = nltk.grammar.CFG.fromstring(commentless_cfg_string)

    # Select our parser
    parser = nltk.parse.BottomUpChartParser(grammar)

    ### Tests for 3.1 ###
    parse('Nadia left immediately', grammar, parser)
    parse('the cat with the long soft fur slowly ate', grammar, parser)
    parse('she arrived', grammar, parser)
    parse('Nadia with the long soft fur slowly ate', grammar, parser, False)
    parse('the cat with the tall her arrived', grammar, parser, False)


    ### Test every line in a file ###
    # print('\nA1-test.txt\n')
    # with open('A1-test.txt', 'r') as afile:
    #     sentences = afile.read()

    # sentence_list = sentences.split('\n')
    # for sentence in sentence_list:
    # 	parse(sentence, grammar, parser)

if __name__ == '__main__':
    main()
