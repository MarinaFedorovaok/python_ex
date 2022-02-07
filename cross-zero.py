import numpy as np
#create empty board
field = np.zeros((3,3))
print(field)
def motion(field, num_player): 
    str_1 = input("Введите координаты Вашего хода в формате: строка,столбец ")
    x1=int(str_1[0])
    y1=int(str_1[2])
    # np.put(field, [x1-1, y1-1], 1)
    field[x1-1][y1-1] = num_player
    return(field)
#добавить условие - пока клетки не равно 0
print(motion(field, 1))
print(motion(field, 2))
