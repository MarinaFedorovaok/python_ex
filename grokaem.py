# бинарный поиск
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <=high:
        mid = (low+high)//2
        guess = list[mid]
        #print(mid)
        if guess == item:
            return mid
        if guess >item:
            high = mid-1
        else:
            low = mid+1
    return None
my_list = [1, 3, 5, 7, 8, 9, 24, 35, 3521, 423423]
#print(binary_search(my_list, 3))
# for i in my_list:
#     print(binary_search(my_list, i))

# Рекурсия
def countdown(i):
    print(i)
    if i <=0:
        return 0
    else:
        countdown(i-1)
        
#countdown(10)

#Стек вызовов

def sum_li(n):
    
    if n<=0:
        return 0
    else:
       return n%10 + sum_li(n//10)
print(sum_li(2567))
#p 84