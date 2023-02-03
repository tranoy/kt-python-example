# Q3 answer template

def solutionQ3(store, customer):
    for i in range(len(customer)):
        for j in range(len(store)):
            if customer[i] == store[j]:
                customer[i] = -1

#store = [2,3,7,8,9]
#customer = [7,5,9]
store = [1,2,3,7,8]
customer = [1,5,8,4,6]


solutionQ3(store, customer)

answer = [None]*len(customer)
for i in range(len(customer)):
    if customer[i] == -1:
        answer[i] = 'yes'
    else:
        answer[i] = 'no'
        
print(answer)
