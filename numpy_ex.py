import numpy as np 
# 1
A = np.array([[1, 2, 3], [4, 5, 6]]) # преобразование список в массив
#print(A)
# 2 
# a = [1,2,3]
# b = np.array(a, dtype='float64')
# print(b)
# print(type(a))
# print(type(b))

# Характеристикик массива
#print(len(A))

#Заполнить массив
c = np.zeros(8)
d = np.zeros_like(c)
#
e = np.arange(1, 20, 3) #задаем начало, конец и интервал
f =np.linspace(1, 20, 10)#задаем начало, конец и количество точек
#print(f)
        #операции над массивами
#print(e)
m = np.linspace(11, 30, 10)
# print(m)
# print(f+m)
# print(f*5)
        #функции
#print(np.cos(f))
        #константы
#print(np.e, np.pi)
        #складываем послеующий элемент с предыдущим
#print(np.cumsum(e))
m = np.array([1, 34, 324, 2, 3, -4, 0])
#print(m)
#print(np.sort(m)) # массив не меняется
m.sort()            #масссив изменился
#print(m)
    #объединим и разъединим массивы
v = np.hstack((m, e, 5*e))
print(v)
x1, x2, x3 = np.split(v, [3, 8])
# print(x1)
# print(x2)
# print(x3)
    #delete, insert

#print(np.delete(v, [2, 5])) # удалил элементы с индексаи 2 и 5
#print(np.insert(v, 1, [-1, 3])) # добавили в индекс 1 элементы: -1 и 3

    # Инжексирование и срезы
f = v[::-1] #массив в обратном порядке копия не создается
print(f)
print(np.sum(f))