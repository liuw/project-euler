#!/usr/bin/python


import time
import math

# n^2 + a*n + b

def is_prime(n):
    upper_bound = int(math.sqrt(abs(n))) + 1
    for i in xrange(2, upper_bound):
        if n % i == 0:
            return False
    return True

def main():
    result = ()
    maxn = 0
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            n = 0
            while is_prime(n**2 + a*n + b): n += 1
            if n > maxn:
                maxn = n
                result = (n, a, b)

    print result
    n, a, b = result
    print a*b



start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
