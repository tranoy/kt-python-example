# Q3 Answer template

def solution(left, right):
    global answer
    answer = 0
    for i in range(left, right+1):
        leftc = 0
        for j in range(1, i+1):
            if i % j ==0:
                leftc += 1
        if leftc % 2 ==0:
            answer = answer + i
        else:
            answer = answer - i
    return answer
left = 24
right = 27
c = solution(left, right)
print(c)
