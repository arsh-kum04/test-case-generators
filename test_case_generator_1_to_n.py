import random

f = open("input.txt","w")
t = 100
for _ in range(t,0,-1):
    print(_,file=f,end= ' ')
f.close()
