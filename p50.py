#!/usr/bin/python
# encoding: utf-8

import time
import itertools
try:
    import psyco
    psyco.full()
except ImportError:
    pass

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

limit = 1000000

def solve():
    print "primes"
    primes = get_primes_erat(limit)
    print "primes done"
    result = 0
    l = 0
    lp = len(primes)
    print "maps"
    map_ = [False] * (primes[-1]+1)
    for p in primes:
        map_[p] = True
    print "maps done"
    for i in xrange(0, lp):
        val = sum(primes[i:])
        for j in xrange(lp-1, i, -1):
            if val < limit and val > result and (j-i+1) > l and map_[val]:
                result = val
                l = j - i + 1
                break
            val -= primes[j]

    print result, l
                            

def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
