#!/usr/bin/python
# encoding: utf-8

# Find the sum of all the primes below two million

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

def main():
    print sum(get_primes_erat(2000000))

start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
