import random

f = open("input.txt","w")
t = random.randint(50,100)
print(t,file=f)
for _ in range(t):
    n = random.randint(1,1000)
    print(n,file=f)
f.close()
