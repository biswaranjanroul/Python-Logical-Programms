# Write a java program to find maximum difference between two elements in given Array?
# Input = { 2, 5, 1, 7, 3, 9, 5}
# Output = 8

# Explanation : The maximum difference is between 1 and 9

# Input = { 9, 2, 12, 5, 4, 7, 3, 19, 5}
# Output: 17

def maxDiff(arr, arr_size):
    max_diff = arr[1] - arr[0]
    min_element = arr[0]

    for i in range(1, arr_size):
        if (arr[i] - min_element > max_diff):
            max_diff = arr[i] - min_element

        if (arr[i] < min_element):
            min_element = arr[i]
    return max_diff

arr = [ 9, 2, 12, 5, 4, 7, 3, 19, 5]
size = len(arr)
print("Maximum difference is",maxDiff(arr, size))