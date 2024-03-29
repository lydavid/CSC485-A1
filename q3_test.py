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

    #head_string = '\n' + sentence
    # if should_parse:
    #     head_string = head_string + ' (Should parse)'
    # else:
    #     head_string = head_string + ' (Should not parse)'
    print(sentence)

    # If a sentence is not accepted by our grammar, print: No parses

    parsed = False

    for tree in parser.parse_all(sentence.split()):
        print(tree)
        parsed = True

    if not parsed:
        print("No parses")

def strip_comments(string, symbol='%'):

    # Break str up into individual lines
    lines = string.split('\n')

    # Remove all text after %
    stripped_lines = []
    for line in lines:
        head, sep, tail = line.partition(symbol)
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

    commentless_cfg_string = strip_comments(cfg_string)

    # Build our grammar for testing
    grammar = nltk.grammar.CFG.fromstring(commentless_cfg_string)

    # Select our parser
    parser = nltk.parse.BottomUpChartParser(grammar)

    ### Tests for 3.1 ###
    # parse('Nadia left immediately', grammar, parser)
    # parse('the cat with the long soft fur slowly ate', grammar, parser)
    # parse('she arrived', grammar, parser)
    # parse('Nadia with the long soft fur slowly ate', grammar, parser, False)
    # parse('the cat with the tall her arrived', grammar, parser, False)


    ### Test every test sentences provided for us ###
    # print('\nA1-test.txt\n')
    # with open('A1-test.txt', 'r') as afile:
    #     sentences = afile.read()

    # sentences = strip_comments(sentences)

    # sentence_list = sentences.split('\n')
    # for sentence in sentence_list:
    # 	parse(sentence, grammar, parser)

    ### Test every of our own sentences ####
    test_files = ['Positive', 'Negative', 'Overgen', 'Undergen'] #, 'A1-test - Copy.txt']
    for file in test_files:

        #print(file + '\n')
        with open(file, 'r') as afile:
        #with open('A1-test - Copy.txt', 'r') as afile:
        #with open('Sentences', 'r') as afile:
            sentences = afile.read()

        sentences = strip_comments(sentences)

        sentence_list = sentences.split('\n')
        for sentence in sentence_list:
          parse(sentence, grammar, parser)



    ### Generate random sentence ###
    # from nltk.parse.generate import generate
    # import random



    # commentless_grammar_string = strip_comments(cfg_grammar)
    # brief_lexicon_string = strip_comments(cfg_lexicon)
    # brief_lexicon_string = strip_comments(brief_lexicon_string, '|')
    # brief_grammar_string = commentless_grammar_string + '\n' + brief_lexicon_string
    # brief_grammar = nltk.grammar.CFG.fromstring(brief_grammar_string)

    # # allow for multiple samples
    # for x in range(0,9):
    
    #     # Generate a random depth
    #     d = random.randint(5,7)
    #     # Get the number of sentences with that depth
    #     s_len = len(list(generate(brief_grammar, depth=d)))

    #     # number of sentences to generate
    #     num_sentences = 1
    #     # Get a random offset
    #     offset = random.randint(0, s_len - num_sentences)

    #     # print out only the sentences starting from the offset
    #     inc = 0
    #     for sentence in generate(brief_grammar, depth=d):
    #         if inc >= offset:
    #             print(' '.join(sentence))

    #         inc = inc + 1

    #         # return after we pass the number of sentences to print
    #         if inc >= offset + num_sentences:
    #             break


    #for sentence in generate(grammar, n=10):
    #    print(' '.join(sentence))

if __name__ == '__main__':
    main()
