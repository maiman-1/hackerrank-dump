#!/bin/python3

import math
import os
import random
import re
import sys
import sys 
sys.setrecursionlimit(15000)

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def swapNodes(indexes, queries):
    # Write your code here
    """
    for index in indexes:
        # each element = [first_child, second_child]
        # for first_child, substrees are at 2k + 1 and second child, 2k + 2
        print(index)
    """
    # when query is 1, related element is at 0.
    # when query is 2, related element at at 1 and 2 (if at 0[1] and 0[2] are not -1)
    arr = []
    #print(arr)
    # find a way to traverse according to the height
    for k in queries:
        swap(indexes, 0, 1, k)
        arr.append(inorder_traverse(indexes, 0, []))
        #print(arr)
    return arr
        

def inorder_traverse(indexes: list, index: int, arr: list) -> None:
    #print(index)
    if indexes[index][0] != -1:
        inorder_traverse(indexes, indexes[index][0] - 1, arr)
    if index == 0:
       arr.append(1)
    else:
        arr.append(index + 1)
    if indexes[index][1] != -1:
        inorder_traverse(indexes, indexes[index][1] - 1, arr)
    return arr

def swap(indexes: list, index: int, height: int, k:int):
    #print(indexes, index, height)
    if height % k == 0:
        indexes[index][0], indexes[index][1] = indexes[index][1], indexes[index][0]
    if indexes[index][0] != -1:
        swap(indexes, indexes[index][0] - 1, height + 1, k)
    if indexes[index][1] != -1:
        swap(indexes, indexes[index][1] - 1, height + 1, k)
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
