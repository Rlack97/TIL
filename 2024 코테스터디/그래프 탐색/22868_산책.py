import sys
input = sys.stdin.readline
# 중복없이 갔다 돌아는 것들 중 가장 짧은 경로
# 사전순으로 먼저 오는 것을 선택함
# 다익스트라 = heapq
import heapq

N, M = map(int,input().split())
nodes = [[]for _ in range(N+1)]
for m in range(M):
  A,B = map(int,input().split())
  nodes[A].append(B)
  nodes[B].append(A)
S, E = map(int,input().split())
# 거리 + 부모노드
distance = [[1e9, i] for i in range(N+1)]
answer = 0

visited = []
def dijk(start):
  q = []
  heapq.heappush(q,(0, start))
  distance[start][0] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now][1] in visited:
      continue

    if distance[now][0] < dist:
      continue
    
    for i in nodes[now]:
      cost = dist + 1
      if cost < distance[i][0]:
        distance[i][0] = cost
        distance[i][1] = now
        heapq.heappush(q,(cost,i))

dijk(S)

length = distance[E][0] # 최단 길이
answer += length
parent_node=E
path=[]
while parent_node!=S:        
    path.append(parent_node)
    parent_node = distance[parent_node][1]

for p in path:
  if p == S or p == E:
    continue
  else:
    visited.append(p)


distance = [[1e9, i] for i in range(N+1)]
dijk(E)

answer += distance[S][0]

print(answer)
