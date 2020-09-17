# Write a Program to find sum of unique elements in given Array?

# Input = {1, 6, 4, 3, 2, 2, 3, 8, 1};
# Output : 24
# (Unique elements are: 1, 6, 4, 3, 2, 8)

# Input= {1, 1, 3, 2, 2, 3};
# Output : 6
# (Unique elements are: 1, 2, 3)

lst=[]
n=int(input("Enter the length of the given list:"))
for i in range(n):
    x=int(input("Enter the nexe Value:"))
    lst.append(x)
print(lst)
def remove(lst):
    final_list = []
    for num in lst:
        if num not in final_list:
            final_list.append(num)
    return final_list
s=remove(lst)
sum=0
for i in s:
    sum=sum+i
print(sum)


# def findSum(arr, n):
#     s = set()
#     sum = 0
#
#     # Hash to store all element
#     # of array
#     for i in range(n):
#         if arr[i] not in s:
#             s.add(arr[i])
#     for i in s:
#         sum = sum + i
#
#     return sum
#
#
# # Driver code
# arr = [1, 2, 3, 1, 1, 4, 5, 6]
# n = len(arr)
# print(findSum(arr, n))



