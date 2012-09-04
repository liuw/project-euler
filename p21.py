#!/usr/bin/python

import math
##import itertools
##
### fast prime generator taken from Alex and others
##def erat2():
##    D = {}
##    yield 2
##    for q in itertools.islice(itertools.count(3), 0, None, 2):
##        p = D.pop(q, None)
##        if p is None:
##            D[q*q] = q
##            yield q
##        else:
##            x = p + q
##            while x in D or not (x&1):
##                x += p
##            D[x] = p
##
##def get_primes_erat(n):
##    return list(itertools.takewhile(lambda p: p < n, erat2()))
##
##def comb(items, n=None):
##    if n is None:
##        n = len(items)
##    for i in range(len(items)):
##        v = items[i:i+1]
##        if n == 1:
##            yield v
##        else:
##            rest = items[i+1:]
##            for c in comb(rest, n-1):
##                yield v + c
##
##def all_C_except_one(L):
##    # except C(r, r)
##    for i in xrange(1, len(L)):
##        for elem in comb(L, i):
##            yield elem
##
##def d(n):
##    primes = get_primes_erat(int(math.sqrt(n+1))+1)
##    p_factors = []
##    factors = []
##
##    for p in primes:
##        while n % p == 0:
##            p_factors.append(p)
##            n /= p
##    if n != 1: p_factors.append(n)
##
##    for c in all_C_except_one(p_factors):
##        factors.append(reduce(lambda x,y:x*y, c))
##    factors = set(factors)
##    factors.add(1) # dont forget 1 is also proper divisor
##
##    return sum(factors)

def d(n):
    upper_limit = int(math.sqrt(n))
    sum1 = 0
    for i in xrange(2, upper_limit+1):
        if n % i == 0:
            sum1 += i
            t = n / i
            if t != i:
                sum1 += t
    return sum1 + 1 # dont forget '1'

def solve():
    amicable_set = set()
    for a in xrange(1, 10001):
        b = d(a)
        c = d(b)
        if a == c and a != b:
            amicable_set.add(a)
            amicable_set.add(b)

    print sum(amicable_set)

def main():
    import time
    print "Start"
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"

if __name__ == '__main__':
    main()
