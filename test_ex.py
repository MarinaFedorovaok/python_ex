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
    if len(k) == 0:
         return k
    res = []
    res.append(k[0])
    for i in range(1, len(k)):
        if k[i] !=k[i-1]:
            res.append(k[i])
    return res
#print(unic_order(n))
# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

l1 = ["Ryan", "Kieran", "Jason", "Yous"] 
l2 = ["Ryan", "Jason"]

# def filter_duplicate(string_to_check):
#     if string_to_check in ll:
#         return True
#     else:
#         return False
# ll = l1
# out_filter = list(filter(filter_duplicate, l2))

#  С лямбдой
def friend(x):
    filtered_str = list(filter(lambda s: len(s)==4, x))
    return filtered_str


#print("Отфильтрованный список:", friend(l1, l2))

# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters -
#  each taken only once - coming from s1 or s2.
s1 = "xyaabbbccccdefww"
s2 = "xxxxyyyyabklmopq"
def filter_double(s1):
    #проверяем на уникальность строку
    s1_res=[]
    for i in range(len(s1)-1):
        if s1[i] != s1[i+1]:
            s1_res.append(s1[i])
    return s1_res
l1 = filter_double(s1)
l2 = filter_double(s2)
second_part_str = ''.join((filter(lambda s: s not in l1, l2)))
firts_part =''.join(l1) 
result = firts_part+second_part_str
print(result)