# Дан файл из целых чисел. Используя дек, за один просмотр файла напечатать сначала все отрицательные числа, 
# затем все положительные числа, сохраняя исходный порядок в каждой группе.

with open("/Users/nikiforova.olesya/Desktop/сиаод/lab2/task7.txt") as f:
    arr = f.read().split()

d = []

while len(arr) != 0:
    if int(arr[0]) >= 0:
        d.append(arr[0])
        arr.pop(0)
    else:
        d.insert(0, arr[0])
        arr.pop(0)

print(*d, sep=" ")