#Ваша задача - создать функцию, которая может принимать любое неотрицательное целое число в качестве аргумента
#  и возвращать его с цифрами в порядке убывания. По сути, переставьте цифры, чтобы создать максимально возможное число.
#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.

from re import M


def max(n):
    x = [int(a) for a in str(n)]
    #print(x[2])
    x.sort(reverse=True)
    x = [str (a) for a in x]
    res = ''.join(x)
    return(res)
#print(max(148643))

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]
n = [1,2,2,3,3]
def unic_order(n):
    k = list(map(lambda x:x, n))
    res = []
    res.append(k[0])
    for i in range(1, len(k)):
        if k[i] !=k[i-1]:
            res.append(k[i])
    return res
print(unic_order(n))

    
