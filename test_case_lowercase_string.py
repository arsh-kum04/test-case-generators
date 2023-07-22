import random

f = open("input.txt","w")
t = random.randint(3,10)
print(t,file=f)
for _ in range(t-2):
    n = random.randint(1,100)
    for i in range(n-1):
        c = random.randint(97,122)
        print(chr(c),file=f,end='')
    c = random.randint(97,122)
    print(chr(c), file=f,end=" ")
    for i in range(n-1):
        c = random.randint(97,122)
        print(chr(c),file=f,end='')
    c = random.randint(97,122)
    print(chr(c), file=f)

for _ in range(1):
    n = random.randint(990,1000)
    for i in range(n-1):
        c = random.randint(97,122)
        print(chr(c),file=f,end='')
    c = random.randint(97,122)
    print(chr(c), file=f,end=" ")
    for i in range(n-1):
        c = random.randint(97,122)
        print(chr(c),file=f,end='')
    c = random.randint(97,122)
    print(chr(c), file=f)

for _ in range(1):
    n = random.randint(1,100)
    s = ""
    for i in range(n-1):
        c = random.randint(97,122)
        s = s + chr(c)
        print(chr(c),file=f,end='')
    c = random.randint(97,122)
    s = s + chr(c)
    print(chr(c), file=f,end=" ")
    print(s, file=f)


f.close()
