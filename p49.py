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

primes = get_primes_erat(10000)

def is_valid(n):
    return n in primes and n > 1000

def get_perm(n):
    l = []
    for i in itertools.permutations(str(n)):
        l.append(int("".join(list(i))))
    return l

def solve():
    cache = set()
    for p in primes:
        if p < 1000: continue
        nums = get_perm(p)
        nums = set(filter(is_valid, nums))
        if len(nums) < 3: continue
        nums = sorted(list(nums))
        for g in itertools.combinations(nums, 3):
            a, b, c = g
            if a in cache: continue
            if c-b == b-a:
                print a, b, c, c-b
                cache.add(a)
        

def main():
    solve()

start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
