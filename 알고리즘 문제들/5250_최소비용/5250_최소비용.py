# 5250_최소비용 풀이
# 2022/09/29
# 다익스트라 알고리즘
# 다른 방법은 정말 없을까...
# 일반 BFS로는 0,1 형태의 방문처리가 까다로웠던거 같다.

import sys
sys.stdin = open("input.txt","r")

from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def BFS(x,y):
    dijkstra [x][y] = 0
    # 시작지점을 0으로 지정

    q = deque()
    q.append((x,y))
    while q:
        a,b = q.popleft()
        # 맨 앞의 값을 꺼냄(BFS)

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            # 4방향 탐색

            if 0<= nx <N and 0<= ny <N:
                # 유효 인덱스
                cost = 1
                if mapping[a][b] < mapping[nx][ny]:
                    cost += mapping[nx][ny] - mapping[a][b]
                # 기본 코스트 1, 추가 코스트 계산
                
                if dijkstra[a][b] + cost < dijkstra[nx][ny]:
                    # 진행 예정인 칸의 코스트가 현재 계산한 코스트보다 클 때
                    dijkstra[nx][ny] = dijkstra[a][b] + cost
                    # 현재 계산한 코스트(최소값)으로 갱신
                    q.append((nx,ny))
                    # 다음 위치에서의 계산을 추가
    

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    mapping = [list(map(int,input().split())) for _ in range(N)]
    dijkstra = [[float('inf')]*N for _ in range(N)]
    # 해당 칸까지의 코스트 최소값을 입력하기 위해 inf로 이루어진 표 

    BFS(0,0)

    answer = dijkstra[N-1][N-1]

    print('#{} {}'.format(tc, answer))