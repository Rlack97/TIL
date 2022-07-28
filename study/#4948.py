def prime(x):
    for z in range(2,int(x**(1/2))):
        if x % z == 0:
            return False
    return True

K = []
while True:
    i = int(input())
    if i == 0:
        break

    result = 0
    for k in range(i+1,2*i+1):
        if prime(k) == True:
            result += 1
    
    K.append(result)

    
for q in K:
    print(q)