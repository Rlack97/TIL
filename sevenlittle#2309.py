import random

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())

K = [a,b,c,d,e,f,g,h,i]


while True:
    T = random.sample(K, 7)
    if sum(T) == 100:
        T.sort()
        for Q in T:
            print(Q)
        break
        


