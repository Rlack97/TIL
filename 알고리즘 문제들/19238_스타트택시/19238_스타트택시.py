# 19238_스타트택시 풀이
# 2022/10/04

from collections import deque
import sys
sys.stdin = open('input.txt','r')

N,M,FF = map(int,input().split())

city = [list(map(int,input().split())) for _ in range(N)]

count = [[0] * N for _ in range(N)]
starty, startx = map(int,input().split())

# 행 = y, 열 = x
guest = dict()
goal = dict()
for m in range(M):
    y,x,zy,zx = map(int,input().split())
    guest[m] = (y,x)
    goal[m] = (zy,zx)
# 데이터 입력

dy = [0,1,0,-1]
dx = [1,0,-1,0]
# 1. 각 손님과의 최단 거리를 구하는 함수 정의
def BFS(starty,startx):
    visited = [[0] * N for _ in range(N)]
    Q = deque()
    Q.append(starty,startx)
    visited[starty][startx] = 1

    while Q:
        popy,popx = Q.popleft()

        for i in range(4):
            ny = popy + dy[i]
            nx = popx + dx[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if city[ny][nx] == 1 or visited[ny][nx] != 0:
                continue

            visited[ny][nx] = visited[popy][popx] +1
            Q.append(ny,nx)
    
    return visited

def check_distance(visited: list, people: dict):
    i = 0
    for px, py, ax, ay in people:
        people[i]

                

# 2. 최단거리의 손님까지 이동 -> 손님의 목적지까지 이동하는 함수
    # FF - 손님까지의 최단거리 - 손님의 목적지까지의 최단거리
    # if FF < 0: return False(-1)
    # FF + (목적지까지의 최단거리 *2) 
    # 손님과 목적지를 딕셔너리에서 제거 
    # 1번 함수를 통해 최단거리 손님을 다시 확인
    # 2번 함수로 재귀
    # if guest == [] and goal == [] 이라면 FF를 출력

