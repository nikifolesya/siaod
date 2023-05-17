import random

n = random.randint(10, 15)
min_limit = random.randint(-50, 0)
max_limit = random.randint(1, 50)

# arr  = []
# for i in range(n):
#   arr.append(random.randint(min_limit, max_limit + 1))

arr = [1, -7, 19, 22, 3, 77, 6, -11, -22, 53]
 
print(arr)

arr.sort()
# print(arr)

def fibonacci(n):
    arr = []
    arr.append(0)
    arr.append(1)
    for i in range(2, n):
        arr.append(arr[i-2] + arr[i-1])
    return arr

# print(fibonacci(len(arr)))
    
def fibonacciPoisk(arr, x):
    N = len(arr)
    arr2 = fibonacci(N)
    fl = 0
    for k in range(len(arr2)):
        if arr2[k] >= N + 1:
            M = arr2[k] - (N + 1)
            i = arr2[k - 1] - M
            p = arr2[k - 1]
            q = arr2[k - 2]
            # print(k)
            # print(arr2[k])
            break
    while (x != arr[i] or fl != -1):
        if i < 0:
            if p == 1:
                fl = -1
                return fl
            i = i + q
            p = p - q
            q = q - p
        elif i >= N:
            if q == 0:
                fl = -1
                return fl
            i = i - q
            p, q = q, (p - q)
        elif arr[i] == x:
            break
        elif x < arr[i]:
            if q == 0:
                fl = -1
                return fl
            i = i - q
            p, q = q, (p - q)
        elif x > arr[i]:
            if p == 1:
                fl = -1
                return fl
            i = i + q
            p = p - q
            q = q - p
    return i

# x = random.randint(-100, 100)  
x = 22 
print(x)   
print(fibonacciPoisk(arr, x))