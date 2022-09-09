# 12712_파리퇴치 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    flies = [list(map(int,input().split())) for _ in range (N)]
    score = []
    for i in range(N):
        for j in range(N):
            # 이차원리스트에 접근

            kill_cross = 0
            kill_X = 0
            # 킬 수를 기록할 변수 생성

            for k in range(M):
                if i+k < N:
                    kill_cross += flies[i+k][j]
                if i-k >= 0:
                    kill_cross += flies[i-k][j]
                if j+k < N:
                    kill_cross += flies[i][j+k]
                if j-k >= 0:
                    kill_cross += flies[i][j-k]

            kill_cross -= 3*flies[i][j]
                # 십자 모양일 경우의 파리 처치 수
            score.append(kill_cross)

            for k in range(M):
                if i+k < N and j+k < N:
                    kill_X += flies[i+k][j+k]
                if i-k >=0 and j-k >=0:
                    kill_X += flies[i-k][j-k]
                if i-k >=0 and j+k <N:
                    kill_X += flies[i-k][j+k] 
                if i+k <N and j-k >=0 :
                    kill_X += flies[i+k][j-k]

            kill_X -= 3*flies[i][j]
            #     # X자 모양일 경우의 파리 처치 수
            score.append(kill_X)
    

    max_score = 0
    for s in score:
        if s > max_score:
            max_score = s

    print('#{} {}'.format(tc,max_score))