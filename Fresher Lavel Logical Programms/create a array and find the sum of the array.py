arr=[]
n=int(input("Enter the lenght of the array:"))
for i in range(n):
    x=int(input("Enter the next value of the array:"))
    arr.append(x)
print(arr)
sum=0
for j in range(0,len(arr)):
    sum=sum+ arr[j]
print("The sum of the array is",sum)

