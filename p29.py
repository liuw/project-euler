#!/usr/bin/python


import time
import math

def main():
    seq = []
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            seq.append(a**b)
    print len(set(seq))


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
