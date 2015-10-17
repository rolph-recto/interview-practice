#!/usr/bin/env python
# knapsack.py
# discrete knapsack

def knapsack(W, items):
    V = [[0 for j in xrange(W+1)] for i in xrange(len(items)+1)]

    # build table
    for i, (_, weight, value) in enumerate(items):
        for j in xrange(W):
            a = V[i][j+1]
            if j+1 >= weight:
                b = V[i][j+1-weight] + value
            else:
                b = -1
            V[i+1][j+1] = max(a,b)

    # determine which items are in the optimal solution
    taken_items = []
    i = len(items)
    j = W
    # while there is still weight left, we know there are more
    # items to take for the optimal solution
    # at most this will take len(items) steps
    while j > 0:
        # ith item is in the optimal solution
        if V[i][j] != V[i-1][j]:
            taken_items.append(items[i-1][0])
            j -= items[i-1][1]

        i -= 1

    return V[len(items)][W], taken_items

def main():
    # item name, weight, value
    items = [('apple',8,16), ('cookie',6,10), ('pop tart',4,7)]

    maxval, maxitems = knapsack(10, items)
    print maxval, maxitems

if __name__ == '__main__':
    main()
