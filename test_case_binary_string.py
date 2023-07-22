import random

f = open("input.txt","w")
t = 100000000
print(t,file=f)
for _ in range(t):
    n = random.randint(1,1000)
    print(str(n%2),file=f,end='')
f.close()
