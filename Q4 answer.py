# Q4 Answer Template
data = input('숫자로 이루어진 문자열을 입력하세요. ')
size = len(data)
result = 1
for i in range(size):
    if data[i] == '0':
        #result = result + int(data[i])
        continue
    else:
        result = result * int(data[i])

print(result)
