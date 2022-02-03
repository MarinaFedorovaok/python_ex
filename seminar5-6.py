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
li = [1, 5, 2, 3, 4, 6, 1, 7, 10]
def f(li1):
    li2=[]
    for i in range(0, len(li1)-2):
        if li[i]<li[i+1]<li[i+2]:
            li2.append(li[i+1])
    if li[0]<li2[0]:
        li2.insert(0, li[0])
    if li[len(li)-1]>li2[len(li2)-1]:
        li2.append(li[len(li)-1])
           
                        
    return(li2)
print(f(li))


