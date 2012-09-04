#!/usr/bin/python

def validate(n):
    import math
    t = n * 2
    sqrt_root = math.sqrt(t)
    a1 = int(sqrt_root)
    a2 = a1 + 1
    if a1 * a2 / 2 == n: return True
    else: return False

##print validate(6)

primes = [2,3,5,7,11,13,17,19]

def solve():
    pass

def main():
    import time
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"

main()
