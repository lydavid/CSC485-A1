def demo():
    """
    A demonstration of the shift-reduce parser.
    """

    from nltk import parse, CFG

    grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    NP -> 'I'
    N -> 'man' | 'park' | 'telescope' | 'dog'
    Det -> 'the' | 'a'
    P -> 'in' | 'with'
    V -> 'saw'
    """)

    sent = 'I saw a man in the park'.split()

    parser = parse.ShiftReduceParser(grammar, trace=2)
    for p in parser.parse(sent):
        print(p)


if __name__ == '__main__':
    demo()