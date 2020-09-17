# Program to find Min and Max elements in given Array?
# Input:  1, 2, 5, 5, 6, 6, 7, 2
# Output:   Min : 1  Max : 7

def getMin(arr, n):
    return min(arr)
def getMax(arr, n):
    return max(arr)
arr = [ 1, 2, 5, 5, 6, 6, 7, 2]
n = len(arr)
print("Minimum element of array: ",getMin(arr, n))
print("Maximum element of array: ",getMax(arr, n))