# def maxDiff(arr, arr_size):
#     max_diff = arr[1] - arr[0]
#     min_element = arr[0]
#     for i in range(1, arr_size):
#         if (arr[i] - min_element > max_diff):
#             max_diff = arr[i] - min_element
#
#         if (arr[i] < min_element):
#             min_element = arr[i]
#     return max_diff
#
#
# # Driver program to test above function
# arr = [2, 5, 1, 7, 3, 9, 5]
# size = len(arr)
# print("Maximum difference is",maxDiff(arr, size))
num=int(input("Enter a number of the row:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
