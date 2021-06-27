#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Use pointers to find how many people has bride and stuff
    nums_bribe = 0
    for i in range(len(q)):
        print(i+1, q[i], nums_bribe)
        # each q[i] should be the same as i + 1
        if (q[i] - (i + 1) > 2):
            print("Too chaotic")
            return
        for j in range(max(q[i] - 2, 0), i):
            print(q[j], q[i])
            if q[j] > q[i]:
                nums_bribe += 1
    print(nums_bribe)
        

if __name__ == '__main__':
    qs = [[5, 1, 2, 3, 7, 8, 6, 4],
		[1, 2, 5, 3, 7, 8, 6, 4]]

    for q in qs:
        minimumBribes(q)
