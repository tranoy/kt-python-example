# Q1 Answer template
def rank_lotto(a):
    if a==6:
        return 1
    elif a==5:
        return 2
    elif a==4:
        return 3
    elif a==3:
        return 4
    elif a==2:
        return 5
    else:
        return 6
    
#lottos = [44, 1, 0, 0, 31, 25]
#win_nums = [31, 10, 45, 1, 6, 19]
#lottos = [0, 0, 0, 0, 0, 0]
#win_nums = [38, 19, 20, 40, 15, 25]
lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
count = 0
lcount = 0
for i in range(6):  #0 개수
    if lottos[i] == 0:
        count += 1

for i in range(6):  #0을 제외한 맞춘 개수
    for j in range(6):
        if win_nums[i] == lottos[j]:
            lcount += 1


print(f'[{rank_lotto(lcount+count)}, {rank_lotto(lcount)}]')
