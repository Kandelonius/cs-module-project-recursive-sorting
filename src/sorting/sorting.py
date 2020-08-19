# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # merged_arr = []
    """
        this helper function will combine arr[0] of the two arrays that are passed to it
    """
    # a = len(arrA)
    # b = len(arrB) # the while loop appears to be skipping the len(arrB) condition
    # midpoint = len(merged_arr) // 2
    index1 = 0
    index2 = 0
    main_index = 0
    while index1 < len(arrA) and index2 < len(arrB):  # use up all of the elements of each array
        if arrA[index1] < arrB[index2]:  # if arrA is smaller merge that element
            merged_arr[main_index] = (arrA[index1])
            # merged_arr.append(arrA[index1])
            index1 += 1
        else:  # else merge the element in B
            print("Why don't I do anything?")
            merged_arr[main_index] = (arrB[index2])
            # merged_arr.append(arrA[index2])
            index2 += 1
        main_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # if len(arr) <= 1:
    #     return arr
    """
        divide and conquer sort
        will divide the array down the middle recursively until we have all single
        element arrays
    """
    # if the array is larger than one element we break the array down until it we
    # only have arrays of length 1 recursively
    # if len(arr) > 1:
    #     midpoint = len(arr) // 2  # finding the midpoint to divide the arrays evenly
    #     temp1 = arr[:midpoint]  # set the first half of the array to this array
    #     temp2 = arr[midpoint:]  # and the second half to this
    #
    #     merge_sort(temp1)  # recursive calls of the two halves
    #     # print(f"temp1 is {temp1}")
    #     merge_sort(temp2)
    #
    #     # calling the helper function to merge our arrays after they have been
    #     # broken down
    #     return merge(temp1, temp2)
    if len(arr) <= 1:
        return arr
    midpoint = len(arr) // 2  # finding the midpoint to divide the arrays evenly
    temp1 = arr[:midpoint]  # set the first half of the array to this array
    temp2 = arr[midpoint:]  # and the second half to this

    merge_sort(temp1)  # recursive calls of the two halves
    # print(f"temp1 is {temp1}")
    merge_sort(temp2)

    # calling the helper function to merge our arrays after they have been
    # broken down
    return merge(temp1, temp2)

    # return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#
# def merge_sort_in_place(arr, l, r):
#
#     # Your code here

arr1 = [11, 10, 6, 1, 2, 11, 12, 18, 7, 8, 0, 19, 16, 13, 14, 9, 17, 15, 5, 3, 20]
print(merge_sort(arr1))
