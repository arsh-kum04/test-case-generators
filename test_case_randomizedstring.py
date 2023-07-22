import random

f = open("input.txt","w")
t = random.randint(15,30)
print(t,file=f)
for _ in range(t):
    n = random.randint(1,32)
    m = random.randint(1,500)
    s = 'a' * n + 'b' * m
    l = list(s)
    random.shuffle(l)
    s = ''.join(l)
    print(s, file=f)
f.close()
