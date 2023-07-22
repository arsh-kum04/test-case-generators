import random

f = open("input.txt","w")
t = random.randint(30,50)
print(t,file=f)
l = [2,3,4,5,9]
for _ in range(t-4):
    n = random.randint(1,1000)
    m = random.choice(l)
    print(n,m,file=f)
    for i in range(n-1):
        c = random.randint(0,9)
        print(c,file=f,end='')
    c = random.randint(0,9)
    print(c, file=f)
f.close()
