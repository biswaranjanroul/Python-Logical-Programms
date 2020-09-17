def fabonacci(nth):
    #nth=nth term of the number
    if nth<0:
        print("Enter a positive number.")
    elif nth==1:
       return 0
    elif nth==2:
        return 1
    else:
        return fabonacci(nth-1)+fabonacci(nth-2)

print(fabonacci(10))

