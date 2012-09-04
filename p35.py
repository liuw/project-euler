#!/usr/bin/python

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

primes = get_primes_erat(1000000)

def is_circular_prime(p):
    global primes
    s = str(p)
    lenp =len(s)

    for i in xrange(1, lenp):
        s = s[1:] + s[0]
        if int(s) not in primes:
            return False
    return True
    

def solve():
    global primes
    count = 0
    for p in primes:
        if is_circular_prime(p):
            count += 1
    print count

def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
