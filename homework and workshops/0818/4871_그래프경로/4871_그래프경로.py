# 4871_그래프경로 풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt','r')

# DFS 정의
def routesearch(start,goal,nodlength,nod):
    visited = [False]*(nodlength+1) 
    # 방문리스트 작성 (인덱스를 그대로 활용하기 위해 길이+1)

    nodstack = []
    # 정점을 기록할 스택 생성

    visited[start] = True
    # 시작지점 방문처리

    while True:
        #반복 

        if start == goal:
                return 1
                # 연결되어 있으면 1

        for i in nod[start]:
            # nod 리스트에 기록한 간선의 목적지에 대해 반복
            # 중요, 이 for문이 있어야 nod 리스트에 간선정보를 중복기입 할 수 있음

            if visited[i] == False: 
                nodstack.append(start)
                start = i
                visited[start] = True
                break
                
                # 방문한 적이 없으면 스택푸시 + 방문처리 후 브레이크
        
        else:
            if nodstack:
                start = nodstack.pop()
                # 주변에 방문 안 한 곳이 없으면
                # 직전의 정점으로 돌아감
            else:
                return 0       
                # 전부 순회했는데 연결되어 있지 않았으므로 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    nod = [[] for _ in range(V+1)]
    # 이중리스트는 *로 하면 할당이라서 다 복사되니 주의
    for e in range(E):
        a,b = map(int,input().split())
        nod[a].append(b)
    S,G = map(int,input().split())

    answer = routesearch(S,G,V,nod)
    print('#{} {}'.format(tc,answer))