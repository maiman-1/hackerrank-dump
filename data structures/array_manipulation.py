#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    # Use pointers: possible complexity: O(N)
    max_num = 0
    prev_num = 0
    # Store how much each index increases and decreases. Ensure the end is at i+1 instead
    slope = [0] * (n+1)
    for query in queries:
        slope[query[0] - 1] += query[2]
        slope[query[1]] -= query[2]
    print(slope)
    for i in range(n):
        prev_num += slope[i]
        max_num = max(max_num, prev_num)
    return max_num
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
