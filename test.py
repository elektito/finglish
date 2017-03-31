#!/usr/bin/env python3

from finglish import f2p

def main():
    print('Loading test cases...')

    with open('test.txt') as f:
        pairs = [l.strip().split(' ', 1) for l in f if l.strip()]

    print('{} test cases loaded.'.format(len(pairs)))

    failures = 0
    for finglish, expected_persian in pairs:
        persian = f2p(finglish)
        if len(persian) == 0 or persian != expected_persian:
            print('Test case for "{}" failed: Expected "{}" but got "{}".'
                  .format(finglish, expected_persian, persian))
            failures += 1

    print('{} test case(s) passed successfully. {} failures.'
          .format(len(pairs) - failures, failures))

if __name__ == '__main__':
    main()
