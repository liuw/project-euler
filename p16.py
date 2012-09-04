#!/usr/bin/python

def solve():
    num = pow(2, 1000)
    sum1 = 0
    for i in str(num):
        sum1 += int(i)
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
