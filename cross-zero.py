import numpy as np
#create empty board
field = np.zeros((3,3))
print(field)
def motion(field): 
    str_1 = input("Введите координаты Вашего хода в формате: строка,столбец ")
    x1=int(str_1[0])
    y1=int(str_1[2])
    np.put(field, x1-1, 1)
    return(field)
print(motion(field))
