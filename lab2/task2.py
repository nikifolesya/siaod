# Дек содержит последовательность символов для шифровки сообщений. Дан текстовый файл, содержащий зашифрованное сообщение. 
# Пользуясь деком, расшифровать текст. 
# Известно, что при шифровке каждый символ сообщения заменялся следующим за ним в деке по часовой стрелке через один.

with open("/Users/nikiforova.olesya/Desktop/сиаод/lab2/txt/task2.txt") as f:
    str = f.read()
    
d = []
s = ""

for i in range(26):
        d.append(chr(i+97))

for i in str:
    while i != d[-1]:
        d.insert(0, d.pop())
    d.insert(0, d.pop())
    d.insert(0, d.pop())
    s += d[-1]

print(s)

