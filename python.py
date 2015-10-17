#!/usr/bin/env python
# python.py
# scratchpad for some python quirks

import time

# LEARN PYTHON 3
# new-style classes

# inheritance, method resolution order

# unicode

# foreign function interface

# how is python actually implemented?

### DECORATORS

# a simple decorator
def bold(func):
    def wrap(text):
        return func(text).upper() + '!!'

    return wrap

def sarcasm(func):
    def wrap(text):
        return func(text) + ' /s'

    return wrap

@sarcasm
@bold
def sayName(name):
    return 'Hi, I\'m {}'.format(name)

# more complicated: a decorator that takes an argument
# this of this as a function that returns decorators
def bold2(tmp):
    # decorator to return
    def bold2dec(func):
        def wrap(text):
            return tmp.format(func(text).upper())

        return wrap

    return bold2dec

@bold2('{} !!!')
def sayName2(name):
    return 'Hi, I\'m {}'.format(name)

# memoization decorator
# automatically memoizes functions
memcache = {}

def mem_exists(func, args):
    if func in memcache:
        return args in memcache[func]
    else:
        return False

def mem_update(func, args, val):
    if func in memcache:
        memcache[func][args] = val
    else:
        memcache[func] = {}
        memcache[func][args] = val

def mem_retrieve(func, args):
    return memcache[func][args]

def memoize(func):
    def wrap(*args):
        if mem_exists(func, args):
            return mem_retrieve(func, args)
        else:
            val = func(*args)
            mem_update(func, args, val)
            return val

    return wrap

# automatically memoized!
@memoize
def fibRec(n):
    if n <= 2:
        return 1
    else:
        return fibRec(n-1) + fibRec(n-2)

def fibRec2(n):
    if n <= 2:
        return 1
    else:
        return fibRec2(n-1) + fibRec2(n-2)

def main():
    print sayName('Bob')
    print sayName2('Bob')
    
    rec_start = time.time()
    print fibRec(20)
    rec_end = time.time()

    rec2_start = time.time()
    print fibRec2(20)
    rec2_end = time.time()

    print 'fib w/ memoization: {}s'.format((rec_end-rec_start)*1000)
    print 'fib w/o memoization: {}s'.format((rec2_end-rec2_start)*1000)

if __name__ == '__main__':
    main()

