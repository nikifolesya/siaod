# Дан текстовый файл с программой на алгоритмическом языке. 
# За один просмотр файла проверить баланс квадратных скобок в тексте, используя дек.

with open("/Users/nikiforova.olesya/Desktop/сиаод/lab2/txt/task5.txt") as f:
    str = f.read()

d = []
fl = True

for i in str:
    if i in '[':
        d.append(i)
    elif i in ']':
        if len(d) == 0:
            fl = False
            break
        else:
            d.pop()

if fl and len(d) == 0:
    print("Correct")
else:
    print("Incorrect")