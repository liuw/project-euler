#!/usr/bin/python


import time

cache = {}
cache[0] = 1
cache[1] = 1
cache[2] = 2
def factorial(n):
    global cache
    if n in cache.keys():
        return cache[n]
    prod = 1
    m = n
    while m >= 1:
        prod = prod * m
        m -= 1
    cache[n] = prod
    return prod

# 9! = 362880

def solve():
    t_sum = 0
    for i in xrange(3, 50000):
        fact_sum = sum(map(lambda x: factorial(int(x)), str(i)))
        if fact_sum == i:
            t_sum += i

    print t_sum


def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
