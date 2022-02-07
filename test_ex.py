#Ваша задача - создать функцию, которая может принимать любое неотрицательное целое число в качестве аргумента
#  и возвращать его с цифрами в порядке убывания. По сути, переставьте цифры, чтобы создать максимально возможное число.
#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
# Essentially, rearrange the digits to create the highest possible number.
import numpy as np
def max(n):
    x = [int(a) for a in str(n)]
    #print(x[2])
    x.sort(reverse=True)
    x = [str (a) for a in x]
    res = ''.join(x)
    return(res)
print(max(148643))
