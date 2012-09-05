#!/usr/bin/python
# encoding: utf-8

import time
import math

def char_to_ord(c):
    return ord(c.upper()) - ord('A') + 1

def str_sum(s):
    return sum(map(char_to_ord, s))

def is_triangle_number(num):
    ttn = 2 * num
    n = int(math.sqrt(ttn))
    if n * (n+1) / 2 == num:
        return True
    return False

def solve():
    with open("p42_words.txt") as f:
        content = f.read().split(',')
        content = map(lambda s: s.replace('"',''), content)
        l = map(str_sum, content)
        l = filter(is_triangle_number, l)
        print len(l)

def main():
    solve()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
