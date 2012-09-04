#!/usr/bin/python

# Find the sum of all the numbers that can be written as the sum of
# the fifth powers of their digits

# To find the upper limit of the number sequence:
# The biggest possible for a single position is 9^5=59049
# say we are about to check against 9 digits numbers
# the maximum sum would be 59049*9=531441, which is very far from 100000000

import time

def check(number):
    number_saved = number
    n_sum = 0
    while number > 0:
        i = number % 10
        n_sum += i**5
        number /= 10
    if n_sum == number_saved:
        return True
    else:
        return False

def main():
    print sum(filter(check, xrange(2, 10000000)))

start_time = time.time()
main()
end_time = time.time()

print "Program finished in", end_time - start_time, "second(s)"
