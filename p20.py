#!/usr/bin/python

def solve():
    def frac(x):
        return reduce(lambda x,y:x*y, range(1,x+1))
    num = frac(100)
    sum1 = 0
    while num > 0:
        sum1 += num % 10
        num /= 10
    print sum1

def main():
    import time
    print "Start"
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"

if __name__ == '__main__':
    main()
