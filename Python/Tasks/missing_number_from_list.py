#program to find a missing number from a list.
#supposing arithmetic progression with common difference == 1.

def missing_number(num_list):                 
    for i in range(num_list[0], num_list[-1]):
        if i not in num_list: 
            return i                


print(missing_number([1,2,3,4,6,7,8]))  #5

print(missing_number([10,11,12,14,15,16,17]))  #13
