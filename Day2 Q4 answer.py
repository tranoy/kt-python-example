# Q4 Answer Template
def Least_common_Multi(a, b):
    if a > b:
        a, b = b, a
    for i in range(a, (a*b)+1):
        if i%a == 0 and i%b == 0:
            return i
        
def solutionQ4(arr):
    L1, L2 = 0, 0
    for i in range(len(arr)-1):
        L1 , L2= arr[i], arr[i+1]
        L3 = Least_common_Multi(L1, L2)
        arr[i+1] = L3
    
    return arr[-1]

arr = [None]*15
#arr = [2,6,8,14]
arr = [1, 2, 3]
answer = solutionQ4(arr)
print(answer)
