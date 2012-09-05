#!/usr/bin/python
# encoding: utf-8

import time

# Cheating XD
def solve():
    sum1 = 0
    for i in xrange(1, 1001):
        sum1 += i**i
    s = str(sum1)
    print s[-10:]

def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
