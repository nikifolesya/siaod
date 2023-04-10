# Дан текстовый файл. Используя стек, сформировать новый текстовый файл, содержащий строки исходного файла, 
# записанные в обратном порядке: первая строка становится последней, вторая – предпоследней и т.д.

with open("/Users/nikiforova.olesya/Desktop/сиаод/lab2/task1.txt") as f:
    arr = f.read().split("\n")

s = []

while len(arr) != 0:
    s.append(arr[-1])
    arr.pop()
for i in range(len(s)):
    print(s[i])
    
    