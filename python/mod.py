'a test module'

__author__ = 'chen wang'

import sys

def __test():
    args = sys.argv
    if len(args) == 1:
        print('hello world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    __test()