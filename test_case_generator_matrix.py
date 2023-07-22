import random

f = open("input.txt","w")
t = random.randint(5,7)
print(t,file=f)
print("3 3",file=f)
print("1 3 4 5 2 9 8 7 6",file=f)
print("3 2",file=f)
print("5 4 1 3 2 7",file=f)
for _ in range(t):
    n = random.randint(1,15)
    m = random.randint(1,15)
    print(n, m,file=f)
    l = []
    #a = random.randint(1,100000)
    for i in range(n*m):
        a = random.randint(1,100000)
        if(a in l) :
            i-=1;
            continue
        print(a, end=" ", file=f)
    print(file=f)
f.close()
