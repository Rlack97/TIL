# 9367_점점커지는당근의개수 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    C = list(map(int,input().split()))
    cnt = 1
    maxcnt = 0
    for i in range(N-1):
        if C[i+1] > C[i]:
            cnt += 1
            if maxcnt <= cnt:
                maxcnt = cnt
        elif C[i+1] <= C[i]:
            cnt = 1
    
    print('#{} {}'.format(tc,maxcnt))