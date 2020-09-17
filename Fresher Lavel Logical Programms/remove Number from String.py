# define Numbers
digit= "0,1,2,3,4,5,6,7,8,9"
# take input from the user
str = input("Enter a string: ")
# remove digits from the string
nodigit = ""
for char in str:
   if char not in digit:
       nodigit = nodigit + char
# display the undigits string
print(nodigit)