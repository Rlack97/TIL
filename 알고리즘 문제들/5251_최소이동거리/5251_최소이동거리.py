# 5251_최소이동거리 풀이
# 2022/09/29

import sys
sys.stdin = open("input.txt","r")

# DFS정의
def DFS(n,g,cost):
    global answer

    if n == g:
        answer = min(answer,cost)
    # 목적지에 도달했을 때, 최소값을 저장

    else:
        if cost > answer:
            return
        # 최소값보다 가격이 커진다면 되돌아감

        for a in range(N+1):
            if roads[n][a] != 0:
                DFS (a,g,cost+roads[n][a])
                # 시작점에서 가능한 방향으로 DFS
            

T = int(input())
for tc in range(1,T+1):
    N, E = map(int,input().split())
    roads = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        a,b,c = map(int,input().split())
        roads[a][b] = c

    answer = float('inf')
    # 최소값을 구하기 위한 무한대수 지정
    
    DFS(0,N,0)

    print('#{} {}'.format(tc, answer))