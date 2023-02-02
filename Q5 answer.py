# Q5 Answer Template

n = input('숫자를 입력하세요. ')
size = len(n)
lresult = 0
rresult = 0

for i in range(0, size//2):
    lresult = lresult + int(n[i])
for i in range(size//2, size):
    rresult = rresult + int(n[i])
    
if lresult == rresult:
    print("LUCKY")
else:
    print("READY")
