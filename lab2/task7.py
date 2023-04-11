# Дан файл из целых чисел. Используя дек, за один просмотр файла напечатать сначала все отрицательные числа, 
# затем все положительные числа, сохраняя исходный порядок в каждой группе.

with open("/Users/nikiforova.olesya/Desktop/сиаод/lab2/txt/task7.txt") as f:
    arr = f.read().split()

d = []

for i in range(len(arr)):
    if int(arr[i]) >= 0:
        d.append(arr[i])
    else:
        d.insert(0, arr[i])

print(*d, sep=" ")