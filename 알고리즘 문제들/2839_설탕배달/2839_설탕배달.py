# 2839_설탕배달
# 2023-04-13


import sys
sys.stdin = open('input.txt','r')

T = int(input())
X = T // 5
Y = (T -(5 * X)) // 3

if (T -(5 * X)) % 3 == 0:
    print(X+Y)

else:
    while X > 0:
        X -= 1
        Y = (T -(5 * X)) // 3
        if (T -(5 * X)) % 3 == 0:
            print(X+Y)
            break
    else:
        print(-1)