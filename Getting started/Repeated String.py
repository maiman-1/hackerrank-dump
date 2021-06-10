"""
There is a string, s, of lowercase English letters that is repeated infinitely
many times. Given an integer, n, find and print the number of letter a's in
the first n letters of the infinite string.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    """
    :param s: String: a string to repeat
    :param n: Integer: the number of characters to consider
    :return: Integer: the frequency of a in the substring

    Idea: Predict how many a will appear based on s using maths
    For example, "aba" until 1000, will be repeated 1000 // 333 times,
    causing 333 bs. So, output is 1000 - 333.
    333 = n // len(s)
    there is 2 a's. so, 333 * 2
    then, loop over the remainder 1
    """
    num_mult = n // len(s)
    remaining_letters = n % len(s)
    num_a = 0
    for char in s:
        if char == "a":
            num_a += 1
    total_a = num_a * num_mult
    for i in range(remaining_letters):
        if s[i] == "a":
            total_a += 1
    return total_a


if __name__ == '__main__':
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
    """
    s = "aba"
    n = 1000000000000
    print(repeatedString(s,n))