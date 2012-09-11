#!/usr/bin/python
# encoding: utf-8

import time
import itertools

# Fast prime generator from python cookbook
def erat2():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat(n):
    return list(itertools.takewhile(lambda p: p < n, erat2()))

primes = get_primes_erat(800000)

def slice_from_right(p):
    if p < 10: return False
    for i in xrange(len(str(p)), 0, -1):
        if int((str(p)[:i])) not in primes:
            return False
    return True

def slice_from_left(p):
    if p < 10: return False
    for i in xrange(1, len(str(p))):
        if int((str(p)[i:])) not in primes:
            return False
    return True

def solve():
    l = []
    for p in primes:
        if slice_from_left(p) and slice_from_right(p):
            l.append(p)
    print l
    print sum(l)
        

def main():
    solve()

start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
