# Дан файл из символов. Используя стек, за один просмотр файла напечатать сначала все цифры, 
# затем все буквы, и, наконец, все остальные символы, сохраняя исходный порядок в каждой группе символов.

with open("/Users/nikiforova.olesya/Desktop/сиаод/lab2/txt/task6.txt") as f:
    str = f.read()
    
digit = []
alpha = []
symbol = []

for i in str:
    if i.isdigit():
        digit.append(i)
    elif i.isalpha():
        alpha.append(i)
    else:
        symbol.append(i)

print(*digit + alpha + symbol, sep="")