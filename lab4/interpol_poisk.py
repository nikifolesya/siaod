import random

n = random.randint(10, 15)
min_limit = random.randint(-50, 0)
max_limit = random.randint(1, 50)

arr  = []
for i in range(n):
  arr.append(random.randint(min_limit, max_limit + 1))
 
print(arr)

# arr.sort()
# print(arr)

# На каждом шаге поиска интерполяционный поиск вычисляет, в каком оставшемся пространстве поиска может находиться цель, 
# на основе нижнего и верхнего значений пространства поиска и целевого значения. 
# Затем значение, найденное в этой предполагаемой позиции, сравнивается с целевым значением. 
# Если оно не равно, то оставшееся пространство поиска сокращается до части до или после предполагаемой позиции в зависимости от сравнения. 
# Этот метод будет работать только в том случае, если разумны расчеты размера различий между целевыми значениями.

def interpolPoisk(arr, x):
    start = 0
    end = len(arr) - 1
    
    while arr[start] != arr[end] and x >= arr[start] and x <= arr[end]:
        mid = start + ((x - arr[start]) * (end - start) // (arr[end] - arr[start]))
        if x == arr[mid]:
            return mid
        # отбрасываем все элементы в правой области поиска, включая средний элемент
        elif x < arr[mid]:
            end = mid - 1
        # отбрасываем все элементы в левой области поиска, включая средний элемент
        else:
            start = mid + 1
            
    if x == arr[start]:
        return start
    
    return -1

x = random.randint(-50, 50)   
print(x)  
print(interpolPoisk(arr, x))