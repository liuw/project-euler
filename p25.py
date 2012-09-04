#!/usr/bin/python

def solve():
    f1 = 1
    f2 = 1
    i = 2
    while True:
        f3 = f1 + f2
        f1, f2 = f2, f3
        i += 1
        if len(str(f3)) == 1000:
            print i, f3
            break

def main():
    import time
    print "Start"
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"

if __name__ == '__main__':
    main()
