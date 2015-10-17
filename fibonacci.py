#!/usr/bin/env python
# fibonacci.py
# guess what this code does?

import time

# naive recursive implementation
# returns nth fibonacci number
def fibRec(n):
    if n <= 2:
        return 1
    else:
        return fibRec(n-1) + fibRec(n-2)

# dynamic programming version 1: memoization
# use a global cache to store results of previous subproblems
def fibMem(n,prev=[]):
    if len(prev) == 0:
        prev = [-1 for i in xrange(n)]

    # cached; just return the previously computed answer
    if prev[n-1] != -1:
        return prev[n-1]
    else:
        # base cases
        if n <= 2:
            prev[n-1] = 1
            return 1
        # recursive cases
        else:
            ans = fibMem(n-1, prev) + fibMem(n-2, prev)
            prev[n-1] = ans
            return ans

# another way of implementating dynamic programming
# iteratively fill out a table of previous computations
def fibTable(n):
    i = 0
    prev=[]
    while i < n:
        if i <= 1:
            prev.append(1)
        else:
            prev.append(prev[i-1] + prev[i-2])

        i += 1

    return prev[n-1]

def main():
    # fib sequence: 1 1 2 3 5 8 13 21 34 55
    rec_start = time.time()
    print fibRec(20)
    rec_end = time.time()

    mem_start = time.time()
    print fibMem(20)
    mem_end = time.time()

    table_start = time.time()
    print fibTable(20)
    table_end = time.time()

    print 'FIB RECURSIVE: {}s'.format((rec_end - rec_start)*1000.0)
    print 'FIB MEM: {}s'.format((mem_end - mem_start)*1000.0)
    print 'FIB DYNPROG TABLE: {}s'.format((table_end - table_start)*1000.0)

if __name__ == '__main__':
    main()
