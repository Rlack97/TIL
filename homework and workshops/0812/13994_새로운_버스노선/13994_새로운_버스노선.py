# 13994_새로운 버스노선 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = [0]*1001    
    for n in range(N):
        C, A, B = map(int,input().split())
            # 입력값 받기

        if C == 1:
            staions = list(range(A,B+1))
            # 일반노선

        elif C == 2:
            staions = [A,B]
            if A % 2: # 홀수면
                for a in range(A+1,B):
                    if a % 2: # 범위 사이 홀수
                        staions.append(a)
            else:
                for a in range(A+1,B):
                    if a % 2 == 0:
                        staions.append(a)
            # 급행노선

        else: 
            staions = [A,B]
            if A % 2 != 0:
                for a in range(A+1,B):
                    if a % 3 == 0 and a % 10 != 0:
                        staions.append(a)
            elif A % 2 == 0:
                for a in range(A+1,B):
                    if a % 4 == 0:
                        staions.append(a)
            # 광역급행노선
        print(staions)
    
        for k in staions:
            cnt[k] += 1
        
    
    mymax = 0
    for i in cnt:
        if i >= mymax:
            mymax = i

    print('#{} {}'.format(tc,mymax))