 #32. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# list1 = [1, 2, 3, 2, 3, 4, 5, 3, 4, 5, 6]
# res = set(list1)
# res1 = list(res)
# print(res1)

#33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²
# from operator import length_hint
# import random
# def koef(k):
#     li = []
#     for i in range(k+1):
#           li.append(random.randint(0,100))
#     return(li)
# li = koef(3)
# length = len(li)
# def el(li, k, l):
#     res_list = ''
#     for m in range(0, l):
#         if k==1: res_list +=(f'{li[m]}*x +')
#         elif k==0: res_list +=(f'{li[m]} = 0')
#         else:
#             res_list +=(f'{li[m]}*x^{k} +')
#         k -=1
#     return(res_list)

# #print (el(li, 4))

# result = el(li, 3, length)
# print(result)
# with open ("34.txt", 'w') as file:
#     file.write(result)

 #35. В файле находится N натуральных чисел, записанных через пробел. 
 # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
 # В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.


# with open('file34.txt') as file:
#     A = [int(x) for x in file.read().split()]

# print(A)
# def finder(A):
#     for i in range(1, len(A)):
#         if not A[i] - 1 == A[i-1]:
#             return A[i] - 1

# print(finder(A))
  #32. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# list1 = [1, 2, 3, 2, 3, 4, 5, 3, 4, 5, 6]
# res = set(list1)
# res1 = list(res)
# print(res1)

#33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x²
# from operator import length_hint
# import random
# def koef(k):
#     li = []
#     for i in range(k+1):
#           li.append(random.randint(0,100))
#     return(li)
# li = koef(3)
# length = len(li)
# def el(li, k, l):
#     res_list = ''
#     for m in range(0, l):
#         if k==1: res_list +=(f'{li[m]}*x +')
#         elif k==0: res_list +=(f'{li[m]} = 0')
#         else:
#             res_list +=(f'{li[m]}*x^{k} +')
#         k -=1
#     return(res_list)

# #print (el(li, 4))

# result = el(li, 3, length)
# print(result)
# with open ("34.txt", 'w') as file:
#     file.write(result)

 #34. Даны два файла в каждом из которых находится запись многочлена. 
 # Сформировать файл содержащий сумму корней многочленов.
from asyncore import write
from unittest import result
import numpy as np
def count_roots(file_name):
    with open(file_name) as f1:
        part1 = f1.read().split()
    print(part1)
    part2 = list(filter(lambda x: x !="+", part1))
    print(part2)
    part3 = list(map(lambda x: x[0], part2))
    print(part3)
    res = np.roots(part3)
    return res
file1='f1_34.txt'
res1 = count_roots(file1)
print(res1)
file2='f3_34.txt'
res2 = count_roots(file2)
print(res2)

with open('f2_34.txt', 'w') as f2:
    f2.write(str(res1))
    f2.write(str(res2))



 #35. В файле находится N натуральных чисел, записанных через пробел. 
 # Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
 # В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.


# with open('file34.txt') as file:
#     A = [int(x) for x in file.read().split()]

# print(A)
# def finder(A):
#     for i in range(1, len(A)):
#         if not A[i] - 1 == A[i-1]:
#             return A[i] - 1

# print(finder(A))

 #36. Дан список чисел. Выделить среди них числа, удовлетворяющие условию:
 #  следующее больше предыдущего. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# from cgitb import text


# li = [1, 5, 2, 3, 85, 4, 6, 1, 7, 10, 12]
# def f(li1):
#     li2=[]
#     for i in range(0, len(li1)-2):
#         if li[i]<li[i+1]<li[i+2]:
#             li2.append(li[i+1])
#     if li[0]<li2[0]:
#         li2.insert(0, li[0])
#     if li[len(li)-1]>li2[len(li2)-1]:
#         li2.append(li[len(li)-1])
                   
#     return(li2)
# print(f(li))


 #38. Напишите программу, удаляющую из текста все слова содержащие "иц".
# text= '''Для вас, души моей царицы,
#         Красавицы, для вас одних
#         Времен минувших небылицы,
#         В часы досугов золотых,
#         Под шепот старины болтливой,
#         Рукою верной я писал;
#         Примите ж вы мой труд игривый!
#         Ничьих не требуя похвал,
#         Счастлив уж я надеждой сладкой,
#         Что дева с трепетом любви
#         Посмотрит, может быть, украдкой
#         На песни грешные мои.'''
# li1 = text.split()

# def find(list_1):
#       list_minus=[]
#       for i in range(0, len(li1)):
#           if li1[i].find('иц') != -1:
#                 list_minus.append(i) #Находим индексы слов, которые надо выкинуть
#       return list_minus
# num = find(li1)

# def res(list_2, num_1):
#       for m in num:
#           list_2[m] = ''
#       return list_2
# res_list = res(li1, num)
# print(res_list)
                ## С Фильтром

# res_list = list(filter(lambda x: x.find('иц') == -1, li1))
# res_string = ' '.join(res_list)
# print(res_string)

# li = [1,2,3,4,5,6,7,8,9,10]
# good = list(filter(lambda x: x%2 ==0 and x%3 !=0, li))
# print(li)
# print(good)                 

# def myfilter(cond, lst):
#   res = []
#   for x in lst:
#     if cond(x):
#       res.append(x)
#   return res

# mygood = list(myfilter(lambda x: x%2 ==0 and x%3 !=0, li))

# print(mygood)
