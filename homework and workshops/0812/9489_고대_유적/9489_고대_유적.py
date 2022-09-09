# 9789_고대유적 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    ground = [list(map(int,input().split()))for _ in range(N)]
    maxlength = 0
    # 입력값 저장 및 최대값 초기화
    # N X M 사이즈는 가로길이(세로갯수) M, 세로길이(가로갯수) N을 의미한다

    for i in range(N): 
        cnt = 0
        for j in range(M):
            if ground[i][j] == 1:
                cnt += 1          
                if maxlength < cnt:
                    maxlength = cnt
            else:
                cnt = 0            


    # 세로 검증은 앞뒤 바꿔서 하면 됨
    for i in range(M):
        cnt = 0
        for j in range(N):
            if ground[j][i] == 1:
                cnt += 1           
                if maxlength < cnt:
                    maxlength = cnt
            else:
                cnt = 0            


    print('#{} {}'.format(tc,maxlength))