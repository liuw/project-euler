#!/usr/bin/python

# Algorithm 1: for a given number
#   1. find all prime factors
#   2. combine prime factors to make new factors
#   3. deduplicate all factors

def seq_gen():
    counter = 0
    val = 0
    while True:
        counter += 1
        val += counter
        yield val

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

import time
s = time.time()
primesss = get_primes_erat(1000000)

print "Done generating primes", time.time() - s

def prime_factors(n):
    p_factors = []
    global primesss
##    primes = get_primes_erat(n+1)
    primes = primesss

    if n in primes: return [n]

    for p in primes:
        while n % p == 0:
            p_factors.append(p)
            n /= p

    return p_factors

##print prime_factors(24)

def solve():
    j = 1
##    for n in seq_gen():
    while True:

        primes = prime_factors(76564125)
        primes_uniq = set(primes)
        
        num_divisors = 1
        for i in primes_uniq:
            num_divisors *= (primes.count(i)+1)
##        print j, n, num_divisors
        j += 1

        print num_divisors
        break
        if num_divisors > 500:
            print
            print n
            break

def main():
    import time
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"

main()
