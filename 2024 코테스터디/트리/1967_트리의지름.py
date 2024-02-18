# 1967 트리의 지름 240126
# 한 노드에서 최대거리를 지닌 다른 노드를 구하는 함수로 dfs 2번을 하면 됨

import sys

iuput = sys.stdin.readline
sys.setrecursionlimit(10**9) # 무한 재귀 방지

n = int(input())
graph = [[]for _ in range(n+1)]

# 입력된 트리를 양방향으로 기록
for _ in range(n-1):
  a,b,c = map(int,input().split()) 
  graph[a].append([b,c])
  graph[b].append([a,c])


# 트리를 순환하면서 거리를 기록하는 재귀함수
# x = 노드번호 wei = 가중치 = 거리
def dfs(x,wei):
  for i in graph[x]:
    a,b = i # i = [노드번호, 가중치]
    if distance[a] == -1: # 해당 노드까지의 거리가 기록되어 있지 않다면
      distance[a] = wei +b # 지금까지의 가중치 + 현 가중치값
      dfs(a,wei+b) # 재귀


# 1번 노드에서 가장 먼 노드
distance = [-1] * (n+1) # 거리 기록용 리스트
distance[1] = 0
dfs(1,0)

# 찾은 노드에서 가장 먼 노드
start = distance.index(max(distance))
distance = [-1] * (n+1) # 거리 기록 리스트 초기화
distance[start] = 0
dfs(start,0)

print(max(distance))