# Q5 Answer template
def solutionQ5(n, s):
    maxmulti = 0
    for i in range(s//2+1):
        num = i * (s-i)
        if num > maxmulti:
            maxmulti = num
            answer = [i, s-i]
        elif maxmulti == 0:
            answer = [-1]
    return answer

n = 2
#s = 9
#s = 1
s = 8
answer = solutionQ5(n, s)
print(answer)
