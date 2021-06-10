#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
	# Write your code here
	# First try to extract all individual numbers
	temp_num = i
	length_num = 0
	num_beautiful_days = 0
	while temp_num > 0:
		temp_num //= 10
		length_num += 1
	for num in range(i, j + 1):
		temp_num = num
		reverse_num = 0
		#print(temp_num / (10 ** length_num))
		while temp_num / (10 ** length_num) >= 1:
			length_num += 1
		length_num_pointer = 1
		while temp_num > 0:
			each_char = temp_num % 10
			temp_num //= 10
			reverse_num += each_char * (10 ** (length_num - length_num_pointer))
			length_num_pointer += 1
            #print(num, each_char, reverse_num)
		# Calculate difference and if it is divisible by k
		difference = abs(num - reverse_num)
		#print(num, reverse_num, difference)
		if difference % k == 0:
			num_beautiful_days += 1
	return num_beautiful_days


if __name__ == '__main__':
    print(beautifulDays(99,101, 3))
