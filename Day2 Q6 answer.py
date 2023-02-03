# Q6 Answer template
def min_of(a):
    minimum = 0
    index = 0
    for i in range(len(a)):
        if a[i] < minimum:
            minimum = a[i]
            index = i
    return (minimum,i)

def solutionQ6(arr):
        minnum, index = min_of(arr)
        arr.pop(index)
        return arr

#arr = [4, 3, 2, 1]
arr = [10]
answer = solutionQ6(arr)
if len(answer) ==0:
    answer = [-1]
print(answer)
