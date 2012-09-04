#!/usr/bin/python

import math
import itertools

# fast prime generator taken from Alex and others
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

def form(n):
    return n * (n + 1) / 2

def calc_factors(n):
    primes = get_primes_erat(int(math.sqrt(n+1))+1)
    if n % 2 == 0: a1, a2 = n, n+1
    else: a1, a2 = n+1, n
    a1 /= 2
    p1_factors = []
    p2_factors = []
    
    for p in primes:
        while a1 % p == 0:
            p1_factors.append(p)
            a1 /= p
        while a2 % p == 0:
            p2_factors.append(p)
            a2 /= p

    if a1 != 1: p1_factors.append(a1)
    if a2 != 1: p2_factors.append(a2)

    p_factors = p1_factors + p2_factors

    p_factors_uniq = set(p_factors)
    num_divisors = 1
    for i in p_factors_uniq:
        num_divisors *= (p_factors.count(i) + 1)

    return num_divisors

def solve():
    i = 1
    while True:
        nfactors = calc_factors(i)
        if nfactors > 500:
            print "****"
            print i, form(i)
            print "****"
            break
        i += 1

def main():
    import time
    print "Start"
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"

if __name__ == '__main__':
    main()
