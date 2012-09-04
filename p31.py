#!/usr/bin/python


import time

# dumb solution, it just works
def solve():
    count = 0
    for a1 in xrange(0, 200/100 + 1):
        for a2 in xrange(0, (200-a1*100)/50+1):
            for a3 in xrange(0, (200-a1*100-a2*50)/20+1):
                for a4 in xrange(0, (200-a1*100-a2*50-a3*20)/10+1):
                    for a5 in xrange(0, (200-a1*100-a2*50-a3*20-a4*10)/5+1):
                        for a6 in xrange(0, (200-a1*100-a2*50-a3*20-a4*10-a5*5)/2+1):
                            a7 = 200-a1*100-a2*50-a3*20-a4*10-a5*5-a6*2
                            count += 1
    print count + 1 # plus 1 because we have (1, 0, 0, 0, 0, 0, 0, 0)


# dynamic programming, much much faster
def solve1():
    numbers = [ 1, 2, 5, 10, 20, 50, 100, 200 ]
    counts = [0] * (max(numbers) + 1)
    counts[0] = 1
    for n in numbers:
        for i in xrange(n, len(counts)):
            counts[i] += counts[i-n]
    print max(counts)

# recursion
arr = [ 200, 100, 50, 20, 10, 5, 2, 1 ]
def _solve2(remain, level):
    m_sum = 0
    if level == len(arr)-1:
        return 1
    for i in xrange(level, len(arr)):
        if (remain - arr[i] == 0): m_sum += 1
        if (remain - arr[i] > 0): m_sum += _solve2(remain-arr[i], i)
    return m_sum

def solve2():
    print _solve2(200, 0)


def main():
    solve2()


start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
