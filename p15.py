#!/usr/bin/python

def C(n, r):
    def frac(x):
        return reduce(lambda x,y:x*y, range(1,x+1))
    if n == r: return 1
    return frac(n) / (frac(r)* frac(n-r))

def solve():
    print C(40,20)

def main():
    import time
    print "Start"
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"

if __name__ == '__main__':
    main()
