# Given an array of integers, return a new array such that each element at index
# i of the new array is the product of all the numbers in the original array
# except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the
# expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

# arr: int[]
# returns array of products
def index_product(arr):
    totalProduct = 1
    for item in arr:
        totalProduct = totalProduct * item
    output = []
    for item in arr:
        output.append(int(totalProduct/item))
    return output

#
#   Create product array by calculating product on the left and right side of
#   element under consideration
#
def index_product_without_division(arr):
    left = []
    tempProduct = 1
    left.append(tempProduct)
    for item in arr[:len(arr)-1]:
        tempProduct = tempProduct * item
        left.append(tempProduct)

    right = []
    tempProduct = 1
    right.append(tempProduct)
    for item in arr[:0:-1]:
        tempProduct = tempProduct * item
        right.append(tempProduct)
    # reverse the product array
    right = right[::-1]
    product = []
    for index, _ in enumerate(arr):
        product.append(left[index] * right[index])
    return product


arr = [1, 2, 3, 4, 5]
print(index_product(arr))
print(index_product_without_division(arr))

arr = [3, 2, 1]
print(index_product(arr))
print(index_product_without_division(arr))
