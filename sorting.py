#!/usr/bin/env python
# sorting.py
# implementation of various sorting algorithms

import random
import time

# bubblesort
# general idea: swap inversions interatively
# pros: very simple
# cons: O(n^2) worst case and average case runtime
# when to use: never, basically. use insertsort for simple sorts
def bubblesort(v):
    i = 0
    n = 1
    iterations = 0
    
    while n < len(v):
        # only swap inversions up to what we haven't done
        while i < len(v)-n:
            # swap inversion!
            if v[i] > v[i+1]:
                a = v[i]
                v[i] = v[i+1]
                v[i+1] = a

            i += 1
            iterations += 1

        i = 0
        n += 1
        iterations += 1

    return v, iterations

# insertsort
# general idea: insert number in increasing sorted sublist in front
# pros: simple, runs well for small n
# cons: O(n^2) worst case runtime
# when to use:  for small n (sub method for insertsort
def insertsort(v):
    i = 1
    iterations = 0
    while i < len(v):
        j = i
        while j > 0 and v[j-1] > v[j]:
            # swap
            a = v[j-1]
            v[j-1] = v[j]
            v[j] = a
            j -= 1
            iterations += 1

        i += 1
        iterations += 1

    return v, iterations

# quicksort
# basic idea: recursively move lt / gt elements around pivot
# pro: very fast in practice ( n log n average time ), in place
# con: quadratic worse case time

# lomuto's partition
def lomuto(v, first, last):
    pivot = v[first]
    h = first
    iterations = 0
    for k in range(first+1, last):
        # preserve invariant: move lt value to left of pivot
        if v[k] < pivot:
            h += 1
            a = v[h]
            v[h] = v[k]
            v[k] = a
            iterations += 1

    # swap pivot with h
    v[first] = v[h]
    v[h] = pivot
    iterations += 1
    return h, iterations

# hoare's partition
# TODO: implement this!
def hoare(v, first, last):
    pass

def quicksort(v, first=-999, last=-999):
    if first == -999: first = 0
    if last == -999: last = len(v)

    # recursive case
    if first < last:
        # partition function must return position
        # of pivot to determine recursive cases
        pivot, iterp = lomuto(v, first, last)
        _, iterl = quicksort(v, first, pivot-1)
        _, iterr = quicksort(v, pivot+1, last)
        return v, iterp+iterl+iterr
    else:
        return v, 0


# mergesort
# basic idea: merge sublists that are sorted recursively
# pro: O(nlogn) worse case!, stable sort
# con: not in-place for recursive implementation, runs worse than quicksort
# use when: memory is not an issue
def split(v):
    l = len(v) / 2
    return v[:l], v[l:]

# conquer phase
def merge(a, b):
    new = []
    ai = 0
    bi = 0
    iterations = 0
    while ai < len(a) and bi < len(b):
        # a[i] goes in sorted list
        if a[ai] <= b[bi]:
            new.append(a[ai])
            ai += 1
        # b[i] goes in sorted list
        elif a[ai] > b[bi]:
            new.append(b[bi])
            bi += 1

        iterations += 1

    # one of the lists has extra elems at the end
    # since we know the list itself is already sorted
    # and we can't compare it to elems of the other list
    # (since all of those have already been sorted)
    # we just append the end of the list to the new list
    # note that it cannot be the case that both a and b
    # have leftovers, given the guard of the while loop
    if ai < len(a) - 1:
        new += a[ai:]

    elif bi < len(b) - 1:
        new += b[bi:]

    return new, iterations

def mergesort(v):
    # singleton list; nothing to do here
    if len(v) == 1:
        return v, 0
    # list of 2; might have to reverse it
    elif len(v) == 2:
        return (v, 1) if v[0] < v[1] else (v[::-1],1)
    # recursive case
    else:
        a, b = split(v)
        # divide
        newa, itera = mergesort(a)
        newb, iterb = mergesort(b)

        # conquer
        new, iterm = merge(newa,newb)
        return new, iterm+itera+iterb


# heapsort
# basic idea: repeated pop top off maxheap to build sorted list
# pros: O(n logn) runtime, in place
# cons: slower than quicksort in practice (larger constants)
# use when: whenever quicksort sucks

# make subarray into a maxheap
def heapify(l,i,heap_size=-1):
    if heap_size == -1:
        heap_size = len(l)

    if i < 1 or i > heap_size/2:
        return l, 0

    # there is a -1 at the end because the heap algo
    # assumes an index starting at 1 while python
    # lists have starting index 0 
    # note that the assumption that starting index is 1
    # is need for heap algo (ex. if index is 0, then left = 2*0 = 0)
    iterations = 0
    left = 2*i
    right = 2*i + 1
    largest = i
    if left <= heap_size and l[largest-1] < l[left-1]:
        largest = left
    if right <= heap_size and l[largest-1] < l[right-1]:
        largest = right
    
    # swap head with largest child, make sure child's subarray is a maxheap
    if largest != i:
        a = l[i-1]
        l[i-1] = l[largest-1]
        l[largest-1] = a
        iterations += 1
        _, new_iters = heapify(l, largest, heap_size)
        iterations += new_iters
        return l, iterations
    else:
        return l, 0

# repeated heapify list from the bottom up
# to make maxheap
def make_maxheap(l):
    iterations = 0
    for i in range(len(l)/2, -1, -1):
        _, new_iters = heapify(l,i+1)
        iterations += new_iters

    return l, iterations

# pop top of maxheap, heapify heap and
# keep popping top until sored
def heapsort(l):
    heap_size = len(l)
    _, iterations = make_maxheap(l)
    while heap_size > 1:
        a = l[1-1]
        l[1-1] = l[heap_size-1]
        l[heap_size-1] = a
        heap_size -= 1
        _, new_iters = heapify(l,1,heap_size)
        iterations += new_iters

    return l, iterations

def main():
    n = 100
    l = [random.randint(1,n) for i in range(n)]
    print 'Original list: ', l

    bubble_start = time.clock()
    bubble_list, bubble_iter = bubblesort(l[:])
    bubble_end = time.clock()
    print 'time: {}s'.format(bubble_end - bubble_start)
    print '# iters: {}'.format(bubble_iter)
    print 'bubblesorted: ', bubble_list

    insert_start = time.clock()
    insert_list, insert_iter = insertsort(l[:])
    insert_end = time.clock()
    print 'time: {}s'.format(insert_end - insert_start)
    print '# iters: {}'.format(insert_iter)
    print 'insertsorted: ', insert_list

    merge_start = time.clock()
    merge_list, merge_iter = mergesort(l[:])
    merge_end = time.clock()
    print 'time: {}s'.format(merge_end - merge_start)
    print '# iters: {}'.format(merge_iter)
    print 'mergesorted: ', merge_list

    quick_start = time.clock()
    quick_list, quick_iter = quicksort(l[:], 0, len(l))
    quick_end = time.clock()
    print 'time: {}s'.format(quick_end - quick_start)
    print '# iters: {}'.format(quick_iter)
    print 'quicksorted: ', quick_list

    heap_start = time.clock()
    heap_list, heap_iter = heapsort(l[:])
    heap_end = time.clock()
    print 'time: {}s'.format(heap_end - heap_start)
    print '# iters: {}'.format(heap_iter)
    print 'heapsorted: ', heap_list


if __name__ == '__main__':
    main()
