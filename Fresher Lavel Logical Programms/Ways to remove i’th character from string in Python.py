str=input("Enter a string:")
print("The origional string is",str)
newstr=''
for i in range(0,len(str)):
    if i!=0:
        newstr=newstr + str[i]
print("The string after the removel of i'th character is",newstr)


