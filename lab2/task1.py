# Отсортировать строки файла, содержащие названия книг, в алфавитном порядке с использованием двух деков.

# def push(arr, item):
#     arr.append(item)

# def pushleft(arr, item):
#     arr.insert(0, item)

# def pop(arr):
#     arr.pop()

# def popleft(arr):
#     arr.pop(0)

with open("/Users/nikiforova.olesya/Desktop/сиаод/lab2/task1.txt") as f:
    arr = f.read().split("\n")

# print(arr)

d1 = []
d2 = []

while len(arr) != 0:
    if len(d1) == 0:
        d1.append(arr[-1])
        arr.pop()
    else:
        if arr[-1] < d1[0]:
            d1.insert(0, arr[-1])
            arr.pop()
        elif arr[-1] > d1[-1]:
            d1.append(arr[-1])
            arr.pop()
        else:
            while arr[-1] < d1[-1]:
                d2.append(d1[-1])
                d1.pop()
            d1.append(arr[-1])
            arr.pop()
            while len(d2) != 0:
                d1.append(d2[-1])
                d2.pop()
                
for i in range(len(d1)):
    print(d1[i])