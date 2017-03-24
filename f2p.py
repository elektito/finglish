#!/usr/bin/env python3

import itertools

def load_conversion_file(filename):
    with open(filename) as f:
        l = list(f)
        l = [i for i in l if i.strip()]
        l = [i.strip().split() for i in l]
    return {i[0]: i[1:] for i in l}

beginning = load_conversion_file('f2p-beginning.txt')
middle = load_conversion_file('f2p-middle.txt')
ending = load_conversion_file('f2p-ending.txt')

def f2p_word(word):
    persian = []
    for i, letter in enumerate(word):
        if i == 0:
            convertor = beginning
        elif i == len(word) - 1:
            convertor = ending
        else:
            convertor = middle
        conversions = convertor.get(letter)
        conversions = ['' if i == 'nothing' else i for i in conversions]
        persian.append(conversions)

    alternatives = itertools.product(*persian)
    return [''.join(i) for i in alternatives]

def f2p(s):
    results = [f2p_word(w) for w in s.strip().split()]
    return [' '.join(i) for i in itertools.product(*results)]

def main():
    print('fenglish: ', end='')
    phrase = input()
    print(f2p(phrase))

if __name__ == '__main__':
    main()
