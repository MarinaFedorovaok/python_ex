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
print (s1[0]>s1[1 ])
# def filter_double(s1):
#     #проверяем на уникальность строку
#     s1_res=[]
#     for i in range(len(s1)-1):
#         if s1[i] != s1[i+1]:
#             s1_res.append(s1[i])
#     return s1_res
# l1 = filter_double(s1)
# l2 = filter_double(s2)
# second_part_str = ''.join((filter(lambda s: s not in l1, l2)))
# firts_part =''.join(l1) 
# result = firts_part+second_part_str
# print(result)

#Вариант с 1 методом для кодворс:
# def longest(a1, a2):
#     s1_res=[]
#     for i in range(len(a1)-1):
#         if a1[i] != a1[i+1]:
#             s1_res.append(a1[i])
#     s2_res=[]
#     for i in range(len(a2)-1):
#         if a2[i] != a2[i+1]:
#             s2_res.append(a2[i])
#     second_part_str = ''.join((filter(lambda s: s not in s1_res, s2_res)))
#     firts_part =''.join(s1_res) 
#     result = firts_part+second_part_str
#     return result

def longest(a1, a2):
    a1=set(a1)
    a2=set(a2)
    a3 = a1.union(a2)
    li = []
    for i in a3:
        li.append(i)
    li = sorted(li)
    result = ''.join(li)
    return result
print(longest(s1, s2))

#print(longest(s1, s2))
# задача понята не верно. нужно по возрастанию
