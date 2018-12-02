# Given an array of integers, find the first missing positive integer in linear
# time and constant space. In other words, find the lowest positive integer that
# does not exist in the array. The array can contain duplicates and negative
# numbers as well. For example, the input [3, 4, -1, 1] should give 2. The input
# [1, 2, 0] should give 3. You can modify the input array in-place.

def find_missing(arr):
    smallest, largest = find_smallest_and_largest(arr)
    hashMap = {}
    for item in arr:
        hashMap[item] = True
    for item in range(smallest, largest):
        if item not in hashMap.keys():
            return item
    return largest + 1


def find_smallest_and_largest(arr):
    smallest = arr[0]
    largest = arr[0]
    for element in arr:
        if element < smallest:
            smallest = element
        if element > largest:
            largest = element
    return smallest, largest

input = [3, 4, -1, 1]
print(find_missing(input))
input = [1, 2, 0]
print(find_missing(input))