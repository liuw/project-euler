#!/usr/bin/python

def valid(s):
    if '0' in s: return False
    if len(s) != 9: return False
    if len(set(s)) != 9: return False
    return True


def solve():
    largest = 0
    number = 0
    l = []
    for i in range(2, 10):
        low_exp = 9 / i - 1
        high_exp = 9 / i 
        high = 10 ** high_exp
        low = 10 ** low_exp
        for n in xrange(high, low - 1, -1):
            s = ''
            r = range(1, i+1)
            for x in r:
                s += str(x * n)
            if valid(s):
                print s, n, r
                if int(s) > largest:
                    largest = int(s)
                    number = n
                    l = r
    print "Ans:", largest, number, l


def main():
    import time
    print "Start"
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"


if __name__ == '__main__':
    main()
