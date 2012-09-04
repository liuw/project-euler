#!/usr/bin/python

def calc(s):
    return sum(map(lambda c: ord(c)-ord('A')+1, s))

def solve():
    sum1 = 0

    f = open('p22_names.txt', 'r')
    content = f.read()
    f.close()
    content = sorted(content.replace('"','').split(','))

    for i, elem in enumerate(content, start=1):
        score = calc(elem)
        sum1 += score * i

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
