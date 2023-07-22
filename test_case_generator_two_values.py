import random

f = open("input.txt","w")
t = random.randint(1,30)
print(t,file=f)
for _ in range(t):
    n = random.randint(1,300)
    print(n,file=f)
    l = []
    #a = random.randint(1,100000)
    for i in range(n):
        p = random.randint(1,10000)
        a = random.randint(p,100000)
        print(a, end=" ", file=f)
    print(file=f)
f.close()
