#!/usr/bin/python
import math
##import itertools
import time

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
##primes = []
##
##def d(n):
##    global primes
##    n_saved = n
##    prod = 1
##    S = {}
##
##    for p in primes:
##        while n % p == 0:
##            try:
##                S[p] += 1
##                n /= p
##            except KeyError:
##                S[p] = 0
##
##    if n != 1: S[n] = 1
##
##    for k in S:
##        t = 0
##        v = S[k]
##        while v >= 0:
##            t += k**v
##            v -= 1
##        prod *= t
##
##    return prod-n_saved # sum of proper divisors

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
    abundant_list = []

    s = time.time()
    for i in xrange(12,28124):
        if d(i) > i:
            abundant_list.append(i)
##    print time.time() - s, len(abundant_list), "...."
    all_list = range(28124)
    for i in xrange(len(abundant_list)):
        for j in xrange(i, len(abundant_list)):
            t = abundant_list[i] + abundant_list[j]
            if t <= 28123: all_list[t] = 0

    print sum(all_list)

def main():
##    global primes
    print "Start"
    s = time.time()
##    primes = get_primes_erat(int(math.sqrt(28123))+1)
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"

if __name__ == '__main__':
    main()
