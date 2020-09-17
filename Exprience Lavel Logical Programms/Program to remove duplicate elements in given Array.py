# Write a Java Program to remove duplicate elements in given Array?
# Input:  1, 2, 5, 5, 6, 6, 7, 2
# Output:  1, 2, 5, 6, 7

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Driver Code
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))