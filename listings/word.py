class Word(str):
    '''Class for words, defining comparison based on word length.'''

    def __new__(cls, word):
        # Note that we have to use __new__. This is because str is an 
        # immutable type, so we have to initialize it early (at creation)
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')] 
            # Word is now all chars before first space
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

if __name__ == '__main__':
    w1 = Word('a')
    w2 = Word('bb')
    w3 = Word('c')
    print w1, '<=' if w1 <= w2 else '>', w2
    print w2, '<=' if w2 <= w3 else '>', w3
    print w1, '<=' if w1 <= w3 else '>', w3
    print w1, '<' if w1 < w2 else '>=', w2
    print w2, '<' if w2 <= w3 else '>=', w3
    print w1, '<' if w1 <= w3 else '>=', w3
