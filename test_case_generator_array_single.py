import random

f = open("input.txt","w")
t = random.randint(1,20)
print(t,file=f)
for _ in range(t):
    n = random.randint(1,100)
    print(n,file=f)

    for i in range(n-1):
        a = random.randint(-10000,10000)
        print(a, end=" ", file=f)
    a = random.randint(-10000,10000)
    print(a, file=f)
f.close()
