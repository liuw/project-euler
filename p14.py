#!/usr/bin/python

# following brute force alogrithm took 47s on a core i3 processor
##def solve():
##    longest_chain = 0
##    number = 0
##    for n in xrange(999999, 2, -1):
##        chain = 1
##        t = n
##        while n != 1:
##            if n % 2 == 0:
##                n /= 2
##            else:
##                n = n * 3 + 1
##            chain += 1
##        if chain > longest_chain:
##            longest_chain = chain
##            number = t
##    print "****"
##    print number, longest_chain
##    print "****"

def f(n, S):
    if n % 2 == 0:
        m = n / 2
    else:
        m = n * 3 + 1
    if m == 1: return 1

    try:
        S[n] = S[m] + 1
    except KeyError:
        chain = f(m, S)
        S[n] = chain + 1
    return S[n]

def solve():
    S = {}
    longest_chain = 0
    number = 0

    for n in xrange(2, 1000000):
        try:
            S[n] # already in hash table, save some time
            continue
        except KeyError:
            pass
        # recursively serach for next term in S
        chain = f(n, S)

        S[n] = chain

        if chain > longest_chain:
            longest_chain = chain
            number = n

    print "****"
    print number
    print "****"

def main():
    import time
    print "Start"
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"

if __name__ == '__main__':
    main()
