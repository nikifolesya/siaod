import random

n = random.randint(10, 20)
min_limit = random.randint(-100, 0)
max_limit = random.randint(1, 100)

arr  = []
for i in range(n):
  arr.append(random.randint(min_limit, max_limit + 1))
 
print(arr)

arr.sort()
print(arr)

