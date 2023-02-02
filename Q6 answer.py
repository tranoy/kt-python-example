# Q6 Answer template

n = int(input())
result = 0
flag = 0
for i in range(1, n+1):
    if i * i == n:
        result = i + 1
        flag = 1
        break
if flag == 0:
    print(-1)
else:
    print(result ** 2)
