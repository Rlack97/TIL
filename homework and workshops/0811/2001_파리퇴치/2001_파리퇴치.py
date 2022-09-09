# 2001_파리퇴치 풀이
# 2022-08-11

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    flies = [list(map(int,input().split()))for _ in range(N)]
    # 입력값 처리

    score = []
    # 파리 킬 수 적을 리스트

    for i in range(N-M+1):
        for j in range(N-M+1):
            # 인덱스에러가 나지 않게 조정한 범위 내부에서

            killed = 0
            for k in range(M):
                for h in range(M):
                    killed += flies[i+k][j+h]
                    # 제시된 영역을 순회하면서 값을 더함
                    
            score.append(killed)

    max_score = 0
    for t in score:
        if t > max_score:
            max_score = t
            #킬 수 리스트에서 최댓값을 구한다.

    print('#{} {}'.format(tc, max_score))