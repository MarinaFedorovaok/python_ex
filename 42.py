#42. Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
#li = [1,2,3,4,5,56,67,67,8]
import numpy as np
with open ('42.txt', 'r') as d:
    n = d.read()

n = list(map(int, n.split(',')))
print(n)
li = np.array([n])
unic_elements = np.unique(li)
print(unic_elements)
places_elements = np.unique(li, return_inverse = True)
print(places_elements)
print(li)
with open ('42_result.txt', 'w') as data:
    data.write(str(unic_elements))



# unic = list(frozenset(li))
# print(unic)
# counts_num = []
# place_element = []
# for i in range(0, len(unic)):
#     counts_num.append(li.count(unic[i]))
# print(counts_num)
# res = list(zip(unic, counts_num))
# print(res)

