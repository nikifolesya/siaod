# Даны три стержня и n дисков различного размера. Диски можно надевать на стержни, образуя из них башни. 
# Перенести n дисков со стержня А на стержень С, сохранив их первоначальный порядок. 
# При переносе дисков необходимо соблюдать следующие правила:
# - на каждом шаге со стержня на стержень переносить только один диск;
# - диск нельзя помещать на диск меньшего размера;
# - для промежуточного хранения можно использовать стержень В.
# Реализовать алгоритм, используя три стека вместо стержней А, В, С. Информация о дисках хранится в исходном файле.

n = 7
    
arr = []    

a = []
b = []
c = []

for i in range(1, n + 1):
    arr.insert(0, i)
    
while len(arr) != 0:
    a.append(arr[-1])
    arr.pop()

def step(x, y):
    if len(x) == 0 and len(y) == 0:
        return
    elif len(x) == 0 and len(y) > 0:
        x.append(y.pop())
    elif len(y) == 0 and len(x) > 0:
        y.append(x.pop())
    elif x[-1] > y[-1]:
        x.append(y.pop())
    else:
        y.append(x.pop())

if n % 2 == 0:
    while len(c) != n:
        step(a, b)
        step(a, c)
        step(b, c)
        
else: 
    while len(c) != n:
        step(a, c)
        if len(c) == n:
            break
        step(a, b)

print(a)
print(b)
print(c)

