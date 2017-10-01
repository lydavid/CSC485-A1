#! /usr/bin/env python3.5
""" Question 1 Test"""

# Not necessary; good for python 2.7 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import nltk

def parse(sentence, grammar, parser, should_parse=True):

    if len(sentence) == 0:
        return

    print()

    # Preliminary step, added to account for sentences that begins with *
    # Strip the *, and set should_parse to False
    if sentence[0] == '*':
        sentence = sentence[1:]
        should_parse = False

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


    ### Test every test sentences provided for us ###
    # print('\nA1-test.txt\n')
    # with open('A1-test.txt', 'r') as afile:
    #     sentences = afile.read()

    # sentences = strip_comments(sentences)

    # sentence_list = sentences.split('\n')
    # for sentence in sentence_list:
    # 	parse(sentence, grammar, parser)

    ### Test every of our own sentences ###
    print('\nSentences\n')
    with open('Sentences', 'r') as afile:
        sentences = afile.read()

    sentences = strip_comments(sentences)

    sentence_list = sentences.split('\n')
    for sentence in sentence_list:
      parse(sentence, grammar, parser)

    # Generate random sentence ###
    from nltk.parse.generate import generate
    import random

    len(list(generate(grammar, depth=3)))
    len(list(generate(grammar, depth=4)))
    len(list(generate(grammar, depth=5)))
    len(list(generate(grammar, depth=6)))
    len(list(generate(grammar, depth=7)))

    # Generate a random depth
    d = random.randint(4,7)
    # Get the number of sentences with that depth
    s_len = len(list(generate(grammar, depth=d)))

    # number of sentences to generate
    num_sentences = 10
    # Get a random offset
    offset = random.randint(0, s_len - num_sentences)

    # print out only the sentences starting from the offset
    inc = 0
    for sentence in generate(grammar, depth=d):
        if inc >= offset:
            print(' '.join(sentence))

        inc = inc + 1

        # return after we pass the number of sentences to print
        if inc > offset + num_sentences:
            return


    #for sentence in generate(grammar, n=10):
    #    print(' '.join(sentence))

if __name__ == '__main__':
    main()
