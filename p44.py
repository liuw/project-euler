#!/usr/bin/python
# encoding: utf-8

import time
import math

def is_pentagonal(num):
    # from wikipedia
    part = math.sqrt(24*num + 1)
    n = (part + 1) / 6
    if n == int(n) and (part % 6 == 5):
        return True
    return False

def pentagonal(n):
    return n * ( 3 * n - 1 ) / 2

def solve():
    i = 1
    found = False
    while not found:
        pk = pentagonal(i)
        for j in xrange(i-1, 0, -1):
            pj = pentagonal(j)
            s = pk + pj
            d = pk - pj
            if is_pentagonal(s) and is_pentagonal(d):
                print d, pj, pk, s
                found = True
                break
        i += 1
                

def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
