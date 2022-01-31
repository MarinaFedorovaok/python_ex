# 11. Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.

# def cubs(n):
#     m = {1}
#     for i in range (1, n):
#         m.add(3**i)
#     return(sorted(m))

# def minus(x):
#     res = x
#     for j in range (1, len(x), 2):
#         res[j] = -x[j]
#     return(res)
# print(cubs(10))
# print(minus(cubs(10)))

#12. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1.     
# def dict(n):
#     dict1  = {}
#     for i in range(0, n):
#         dict1[i] = 3*i+1
#     return(dict1)
# print(dict(8))

#13. Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.
# s1 = 'vwlvwrgewshewrlkwrskswr'
# s2 = 'w'
# def counter (s11, s22):
#     count = 0
#     while s22 in s11:
#         count+=1
#         s11 = s11[s11.find(s22) + 1:]
#     return count
# print(counter(s1, s2))
  
# 14. Подсчитать сумму цифр в вещественном числе
# num = 11.242
# list = str(num)
# num_point = list.find(".")
# list_part1 = list[0:num_point]
# list_part2 = list[num_point+1:]
# list2 = list_part1+list_part2
# # list2 = [1, 2, 3, 4, 5]
# n = 0
# summ = 0
# for i in range(0, len(list2)):
#     summ += int(list2[i])
# print(summ)

#15.  Написать программу получающую набор произведений чисел от 1 до N.
# def fact(n1):
#     global n
#     n1 = n
#     list =[]
#     res = 1
#     i = 1
#     while i <= n:
#         res = i*res
#         #print(res)
#         i +=1
#         #print(i)
#         list.append(res)
#     return(list)
# print(fact(6))

#16. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму
# def sequence(n):
#     list = []
#     for i in range (1, n):
#         res = (1+(1/i))**i
#         list.append(res)
#     return(list)
# print(sequence(6))
# print(sum(sequence(6), start=0)) # встроенная функция sum

#17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число

# def sequence(n):
#     list = []
#     for i in range (-n, n):
#         list.append(i)
#     return(list)
# print(sequence(5))
# list1 =sequence(5) 

# with open('file.txt') as f:
#     n = int(f.read(1))-1
#     k = int(f.read(2))-1
   
# print(list1[n]*list1[k])

#18. Реализовать алгоритм перемешивания списка
# import random
# from operator import itemgetter
# list = [1, 3 , 4 , 5, 6, 6, 7]
# for i in range(0, len(list)-1):
#     k = random.randint(i, len(list)-1)
#     temp = list[i]
#     list[i] = list[k]
#     list[k] = temp
#    # print(list)
# print(list)

#Variant 2

# wigthed_list = []
# for x in list:
#     wigthed_list.append((random.random(), x))
# #print(wigthed_list)
# sorted_wigthed_list = sorted(wigthed_list, key=itemgetter(0))
# rand_list = []
# for x in sorted_wigthed_list:
#     rand_list.append(x[1])
# print(rand_list)

#19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел
                                    # Алгоритм:
                                    # 1. Форируем массив случайых чисел, запуская
                                    #  бота в чат и запрашивая число.
                                    # бот @fedmari_test_bot работает, массив
                                    #  чисел собран в файл numbers.txt
                                    # 2. При запросе случайного числа нам нужен индекс 
                                    # массива - его привязываем ко времени запроса.

# import time
# def my_bot_random(): # выдает случайное число в интервале от х до y
#                                 # создаем список на основе данных файла
#     import math
#     list = []
#     filePath = 'D:\\Razrabitchik\\python\\telegram_bot\\numbers.txt'
#     file = open(filePath, 'r')
#     for line in file:
#         list.append(line)
#                                 #print(list)
#                                 #print(len(list))
#                                 # получем нужный индекс
#     index = int(time.time())
#                                 #print(index)
#     while index>len(list):
#         index = index%len(list)
#                                 #print(index)
#         index_res=math.fabs(index)
#                                 #print(index_res)
#     file.close()
#     return(list[int(index_res)])
# print('Ваше число:' + my_bot_random())
 
# 20. Определить, присутствует ли в заданном списке строк, некоторое заданное число 
# def find(n):
#     list = ['1', '2', '3', '4','5', "ghwrig"]
#     for s in list:
#         if s == str(n):
#             return ("Yes")
#     return("No")
# print(find(2))

# def check(n):
#     list = []
#     filePath = 'D:\\Razrabitchik\\python\\telegram_bot\\numbers.txt'
#     file = open(filePath, 'r')
#     for line in file:
#         list.append(line)
#     print(list)
#     #list = ['1', '2', '3', '4','5', "ghwrig"]
#     flag = False
#     for s in list:
#         if s == str(n)+'\n':
#             flag = True
#             break
#     return flag
# print(check(5))

# def find(n):
#     list = ['1', '2', '3', '4','5', "ghwrig"]
#     for i in range(len(list)):
#         if list[i] != str(n):
#             # i +=1
#         else:
#             return ("Yes")
#     return("No")
# print(find(22))



                # Если просто ищем число:
# s = "28212"
# print(s.isdigit()) 
# s = "Mo3 nicaG el l22er"
# print(s.isdigit())

#21. Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
# from operator import index

# def find (x):
#     list = ['qr', 'awvr', 'fr', 'c4cw', '3rc', 'vfht']
#     if x in list:
#         index = list.index(x)
#         return(index+1)
#     return("No")
# print(find('fr'))

#22. Найти сумму чисел списка стоящих на нечетной позиции

# def summ2():
#     list = ['1', '2', '3', '4', '5', '12']
#     summ = 0
#     for i in range(1, len(list), 2):
#         summ += int(list[i])
#     return(summ)
# print(summ2())

#23. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
# def composition():
#     list = ['1', '2', '3', '4', '5', '2', '5']
#     mid = len(list)//2
#     list1 = list[0:mid]#задаем список первых множителей
#     list2 = list[mid+1:]#задаем список вторых множителей
#     res = 0
#     for i in range(len(list2)):
#         x = list1[i]
#         y = list2[len(list2)-1-i]
#         res += int(x)*int(y)
#     return(res)    
# print(composition())

#24. В заданном списке вещественных чисел найдите разницу между максимальным 
# и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.02, 3.1, 5, 10.01]
for i in range(len(list)):
    list[i] = str(list[i]).split('.')
#print(list)
list1 = []
for i in list:
    if len(i)>1:
        list1.append(i[1])
#print(list1)
max_len = 1
list_numbers_elements = []
for j in range(len(list1)): #ищем длинные элементы
    if len(list1[j])>=max_len:
        max_len = len(list1[j])
        list_numbers_elements.append(j)
if len(list1[0])<max_len:
    list_numbers_elements = list_numbers_elements[1:]
#print(list_numbers_elements)#получили позиции минимальных элементов
for k in range(len(list1)):
     for m in list_numbers_elements:
         if k!=m:
             list1[k] = float(list1[k])
         else:
             list1[k] = float(list1[k])/10**max_len
print(list1)
min = float(1.0000)
max = float(0)
for m in list1:
    if m<min:
        min = m
for m in list1:
    if m>max:
        max = m
print(max)
print(min)
print(max-min)



# print(list_numbers_elements) #позиция минимальных элементов?
# print(max_len) #количество знаков после запятой
#



    


    
    




    

    





