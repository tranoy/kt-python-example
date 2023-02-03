# Q7 Answer Template

def solutionQ7(arr):
    num = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != num[-1]:
            num.append(arr[i])
    return num

#arr = [1,1,3,3,0,1,1]
arr = [4,4,4,3,3]
answer= solutionQ7(arr)

print(answer)
