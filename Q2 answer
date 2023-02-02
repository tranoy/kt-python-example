# Q2 Answer template

N = int(input('N을 입력해주세요. :'))
M = N
count = 1
while True:
    if M//10 ==0:
        M = M*10 + M
    else:
        a = M//10 + M%10
        if a>=10:
            a = a%10
        M = (M%10*10) + a
    if M == N:
        break
    count += 1

print(count)
