# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')
size = len(data)
result = 1
for i in range(size):
    if i < size-1:
        if data[i] == '0' or data[i] == '1':
            result = result + int(data[i])
            print(f'{data[i]} + ', end='')
        else:
            result = result * int(data[i])
            print(f'{data[i]} * ', end='')
    else:
        if data[i] == '0' or data[i] == '1':
            result = result + int(data[i])
            print(f'{data[i]} = ', end='')
        else:
            result = result * int(data[i])
            print(f'{data[i]} = ', end='')
print(result)
