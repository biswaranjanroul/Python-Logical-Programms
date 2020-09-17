# Write a Java Program to find duplicate elements in given Array?
# Input:  1, 2, 5, 5, 6, 6, 7, 2
# Output:  2, 5, 6



arr = [1, 2, 3, 4, 2, 7, 8, 8, 3]
print("Duplicate elements in given array: ")
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if (arr[i] == arr[j]):
            print(arr[j],end=",")
