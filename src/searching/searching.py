# TO-DO: Implement a recursive implementation of binary search

# first_pass = True
def binary_search(arr, target, start, end):
    if end <= 0:
        return -1
    """
    take the array and find the midpoint, if that number is too large set start to it
    and find the midpoint again. Or if the number is too small set the end to it and
    find the lower midpoint. Once we find the number or there are no more other values
    return the number or target not found
    """
    # global first_pass
    # if first_pass:
    #     first_pass = False
    #     start = arr[0]
    midpoint = (end + start) // 2
    if target == arr[midpoint]:
        return midpoint
    elif target < arr[midpoint]:
        return binary_search(arr, target, start, midpoint)
    elif target > arr[midpoint]:
        return binary_search(arr, target, midpoint, end)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

