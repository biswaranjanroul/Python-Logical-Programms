
def summation(n):
    sum = 0
    j = 1

    for i in range(1, n + 1):
        sum = sum + j
        j = (j * 10) + 1

    return sum


# Driver Code
n = int(input("Enter how many terms you want:"))

print(summation(n))