import random

f = open("input.txt","w")
t = random.randint(1,20)
print(t,file=f)
for _ in range(t):
    n = random.randint(1,100)
    m = random.randint(1,10000)
    print(n,m,file=f)

    l = []
    for i in range(n-1):
        a = random.randint(1,1000)
        while(m % a != 0):
            a = random.randint(1,1000)    
        print(a, end=" ", file=f)
        l.append(a)
    a = random.randint(1,1000)
    while(m % a != 0):
        a = random.randint(1,1000)    
    print(a, file=f)
    l.append(a)

    for i in range(n-1):
        a = random.randint(1,l[i])
        print(a, end=" ", file=f)
    a = random.randint(1,l[i])
    print(a, file=f)
f.close()
