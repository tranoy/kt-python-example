# Q2 Answer template

def solutionQ2(numbers):
    for i in range(len(numbers)):
        for j in range(10):
            if numbers[i] == j:
                check[j] = 1
    
check = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#numbers = [1,2,3,4,6,7,8,0]
numbers = [5, 8, 4, 0, 6, 7, 9]

solutionQ2(numbers)
sumnum =0
for i in range(10):
    if check[i] == 0:
        sumnum = sumnum + i

print(sumnum)
