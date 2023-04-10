# Дан текстовый файл с программой на алгоритмическом языке. 
# За один просмотр файла проверить баланс круглых скобок в тексте, используя стек.

with open("/Users/nikiforova.olesya/Desktop/сиаод/lab2/txt/task4.txt") as f:
    str = f.read()

st = []
fl = True

for i in str:
    if i in '(':
        st.append(i)
    elif i in ')':
        if len(st) == 0:
            fl = False
            break
        else:
            st.pop()

if fl and len(st) == 0:
    print("Correct")
else:
    print("Incorrect")