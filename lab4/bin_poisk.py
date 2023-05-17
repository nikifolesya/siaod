import random

n = random.randint(10, 15)
min_limit = random.randint(-50, 0)
max_limit = random.randint(1, 50)

arr  = []
for i in range(n):
  arr.append(random.randint(min_limit, max_limit + 1))
 
print(arr)

def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr = bubble(arr)
# print(arr)

# Бинарный поиск:
# 1. Найти средний элемент заданного массива информации.
# 2. Сравнить полученный объект со значением, которое мы ищем (с так называемым ключом). 
# Если он меньше среднего элемента, поиск осуществляется в левой половине. В противном случае – в правой.
# 3. Когда ключ имеет такое же значение, что и средний элемент, происходит возврат индекса среднего элемента.
# 4. Продолжать выполнять 1-2 шаги до тех пор, пока не останется один объект.
# 5. Когда программа дойдет до последнего элемента, а ключ так и не был обнаружен, происходит возврат -1.

def binPoisk(arr, x):
    start = 0
    end = len(arr) - 1
    while end >= start:
        middle = (start + end + 1) // 2
        if x == arr[middle]:
            return middle
        elif x < arr[middle]:
            end = middle - 1
        elif x > arr[middle]:
            start = middle + 1
    return -1

x = random.randint(-50, 50)   
print(x)   
print(binPoisk(arr, x))


