#using sRting Built in function
'''str=input("Enter a string:")

if str[::-1]==str:
    print('it is a palindrom')
else:
   print("it is not palindrom")'''




#function With reverse string
'''def reverse(s):
    return s[::-1]
def ispalindrome(s):
    rev=reverse(s)
    if s==rev:
        return True
    return False
s="malayalam"
ans=ispalindrome(s)
if ans==1:
    print("yes")
else:
   print("No")'''
# using loop
str=input("Enter a string: ")
rev=""
for i in str:
    rev=rev+i
    if (rev==str):
        print("It is palindroim")
        break
else:
  print("it is not a palindroim")





