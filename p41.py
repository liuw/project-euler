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

st1 = time.time()
print "Generating primes"
primes = get_primes_erat(10000000)
st2 = time.time()
print "done", st2-st1

arr = [ 0, 1, 3, 6, 10, 15, 21, 28, 36, 45 ]
# judging from the array above, the target number cannot be consisted
# of 8 and 9 digits, as they are always divisible by 3
def is_pandigital(n):
    s  = str(n)
    s1 = set(s)
    s2 = set(map(int, s1))
    if '0' in s1: return False
    if len(s) != len(s1): return False
    if sum(s2) != arr[len(s1)]: return False
    return True

def solve():
    global primes
    for i in xrange(len(primes)-1, -1, -1):
        if is_pandigital(primes[i]):
            print primes[i]
            break

def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
