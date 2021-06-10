"""
Objective: Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

Example: 7 socks, [1,2,1,2,1,3,2]. There's 1 pair of 1s and 1 pair of 2s. So,
it should output number of pairs = 2.
"""
"""
Original Code:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    """
    Return an integer representing the number of matching pairs of socks that are available.

    :param n: Integer: the number of socks in the pile
    :param ar: List(Integer): the colors of each sock
    :return: Integer: The number of matching pairs of socks that are available

    Steps:
    1. Loops through list
    2. Stores the first element and it's index
    3. Loops through rest of list
    4. If there is another copy of the element:
        - Stores the copy's index
        - add one to number of pairs
        - Removes elements and both index
        - breaks the loop
    5.  Continues for the rest of the elements on the list

    num_pairs = 0
    i = 0
    while i < len(ar):
        ele = ar[i]
        index_par = i
        for j in range(i, len(ar)):
            if ele == ar[j]:
                index_child = j
                del ar[index_child]
                del ar[index_par]
                break
        i += 1
    """
    # Initialize the number to be outputted
    num_pairs = 0
    colors = set()
    for i in range(n):
        if ar[i] not in colors:
            colors.add(ar[i])
        else:
            num_pairs += 1
            colors.remove(ar[i])
    return num_pairs

if __name__ == '__main__':
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
    """
    n = 10
    ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
    print(sockMerchant(n, ar))
