#!/usr/bin/python


import time


def main():
    n_sum = 1 # starting with 1
    step = 4
    arr = [3, 5, 7, 9]
    while arr[3] <= 1001*1001:
        print arr
        n_sum += sum(arr)
        i = arr[3] + step
        arr = [i, i+step, i+step*2, i+step*3]
        step += 2

    print n_sum

start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
