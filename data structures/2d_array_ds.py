#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    """

    :param arr: int arr[6][6]: an array of integers
    :return: int: the maximum hourglass sum
    """
    # Initialize the hourglass_sums variable
    hourglass_sums = []
    # Loop through arr
    for i in range(len(arr) - 2):
        # Init each row for the hourglass_sums
        hourglass_sums_row = []
        for j in range(len(arr[i]) - 2):
            # Init sum
            sum = 0
            top_row_index = [[i, j], [i, j+1], [i, j+2]]
            mid_row_index = [[i+1, j+1]]
            bottom_row_index = [[i+2, j], [i+2, j+1], [i+2, j+2]]
            for k in top_row_index:
                sum += arr[k[0]][k[1]]
            for k in mid_row_index:
                sum += arr[k[0]][k[1]]
            for k in bottom_row_index:
                sum += arr[k[0]][k[1]]
            hourglass_sums_row.append(sum)
        hourglass_sums.append(hourglass_sums_row)

    # Init return value
    max_value = hourglass_sums[0][0]
    for i in range(len(hourglass_sums)):
        if int(max(hourglass_sums[i])) > max_value:
            max_value = max(hourglass_sums[i])
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
