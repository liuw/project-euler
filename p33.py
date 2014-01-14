#!/usr/bin/python

def solve():

    numerator = 1
    denominator = 1

    # xz / zy ; zx / yz ; xz / yz ; zx / zy
    # z being the number to be removed
    # So that x, y and z cannot be 0
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                c = float(x) / float(y)

                a = x * 10 + z
                b = z * 10 + y
                if  float(a) / b == c and a < b:
                    print str(a) + ' / ' + str(b)
                    numerator *= a
                    denominator *= b

                a = z * 10 + x
                b = y * 10 + z
                if  float(a) / b == c and a < b:
                    print str(a) + ' / ' + str(b)
                    numerator *= a
                    denominator *= b

                a = float(x * 10 + z)
                b = float(y * 10 + z)
                if  float(a) / b == c and a < b:
                    print str(a) + ' / ' + str(b)
                    numerator *= a
                    denominator *= b

                a = float(z * 10 + x)
                b = float(z * 10 + y)
                if  float(a) / b == c and a < b:
                    print str(a) + ' / ' + str(b)
                    numerator *= a
                    denominator *= b
    print "Ans:", denominator / numerator

def main():
    import time
    print "Start"
    s = time.time()
    solve()
    e = time.time()
    print "Problem solved in", e-s, "second"


if __name__ == '__main__':
    main()
