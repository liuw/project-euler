#!/usr/bin/python


import time

# http://en.wikipedia.org/wiki/Repeating_decimal

def calc_cycle_length(n):
    a = 10 % n
    clen = 1
    while a != 1:
        a *= 10
        a %= n
        clen += 1
    return clen
    

def solve():
    max_cycle_length = 0
    result = 0
    for i in xrange(1000, 1, -1):
        if i % 2 == 0 or i % 5 == 0:
            continue
        cycle_length = calc_cycle_length(i)
        if cycle_length > max_cycle_length:
            max_cycle_length = cycle_length
            result = i
        if cycle_length == i - 1:
            break
    print result, "has recurring cycle length of", max_cycle_length


def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
