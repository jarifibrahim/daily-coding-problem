# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

import math


# input: int[]
# k: int
# returns: true or false
def sum_pair(input, k):
    if not input or len(input) < 2:
        return False
    hashMap = {}
    for item in input:
        diff = k - item
        if diff in hashMap.keys():
            return True
        hashMap[item] = True
    return False


input = [10, 15, 3, 7]
assert sum_pair(input, 17) # should be true
assert not sum_pair(input, 12) # should be false
assert not sum_pair(input, 1)  # should be false
assert not sum_pair([], 200)   # should be false
assert not sum_pair(input, -2) # should be false

input = [-1, -2, 4, 10, 3]
assert sum_pair(input, 2)  # should be true
assert sum_pair(input, 13) # should be true
assert sum_pair(input, 13) # should be true
assert sum_pair(input, -3) # should be true
