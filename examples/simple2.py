#!/usr/bin/env python

"""
A simple example of sequential computation using a function.
"""

import time
#import random

# Array size.

N = 10
delay = 1

# Work function.

def calculate(i, j):

    """
    A supposedly time-consuming calculation on 'i' and 'j'.
    """

    #time.sleep(delay * random.random())
    time.sleep(delay)
    return (i, j, i * N + j)

# Main program.

if __name__ == "__main__":

    t = time.time()

    # Initialise an array.

    results = [0] * N * N

    # Perform the work.

    print "Calculating..."
    for i in range(0, N):
        for j in range(0, N):
            i2, j2, result = calculate(i, j)
            results[i2*N+j2] = result

    # Show the results.

    for i in range(0, N):
        for result in results[i*N:i*N+N]:
            print result,
        print

    print "Time taken:", time.time() - t

# vim: tabstop=4 expandtab shiftwidth=4
