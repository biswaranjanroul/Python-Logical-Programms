num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    sum=sum+(i*i*i)
    i=i+1
print("The cube of sum of first natual number is",sum)