# program to find third largest number in given Array ?
#
# Input = [6, 8, 1, 9, 2, 1, 10]
# Output: Third largest element: 8
#
# a = [6, 8, 1, 9, 2, 1, 10, 12]
# Output: Third largest element: 9

# a = [6]
# Output: Invalid Input, array size is less than 3

import sys
def print3largest(arr, arr_size):
    # There should be atleast three
    # elements
    if (arr_size < 3):
        print(" Invalid Input ")
        return
    third = first = second = -sys.maxsize
    for i in range(0, arr_size):

        # If current element is greater
        # than first
        if (arr[i] > first):

            third = second
            second = first
            first = arr[i]
        # If arr[i] is in between first
        # and second then update second
        elif (arr[i] > second):
            third = second
            second = arr[i]
        elif (arr[i] > third):
            third = arr[i]

    print("Three largest elements are",first,second,third)
arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
print3largest(arr, n)