#!/usr/bin/python

import time

def is_palindomic(n):
    s1 = str(n)
    s2 = s1[::-1]
    if s1 != s2: return False
    s3 = bin(n)[2:]
    s4 = s3[::-1]
    if s3 != s4: return False
    return True

def solve():
    print sum(filter(is_palindomic, xrange(1, 1000000)))

def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
