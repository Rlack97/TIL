import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nodes = [[]for _ in range(N+1)]

for _ in range(N-1):
  u,v = map(int,input().split())
  nodes[u].append(v)
  nodes[v].append(u)

# 트리의 중심 구하기
# = 특정 지점에서 다른 노드와의 거리 최대가 최소가 되는 지점 
# 말 어렵게도 쓴다...
# 최적의 위치에서 다른 노드로 이동해야하는 거리들 중 최대 거리를 구하자
# '최소화된 최대 거리'

# 거리 가중치가 없으므로 다익스트라보단 BFS를 통한 탐색이 효율적

def bfs(nodes,start):
  visited = [False] * (N+1)
  distance = [0] * (N+1)

  queue = deque([start])
  visited[start] = True

  max_distance = 0
  farhest_node = start

  while queue:
    current = queue.popleft()
    for neighbor in nodes[current]:
      if not visited[neighbor]:
        visited[neighbor] = True
        distance[neighbor] = distance[current] + 1 
        queue.append(neighbor)

        if distance[neighbor] > max_distance:
          max_distance = distance[neighbor]
          farhest_node = neighbor
  
  return farhest_node, max_distance


start_node = 1
farhest_node, _ = bfs(nodes,start_node)
duble_far, tree_diameter = bfs(nodes, farhest_node)

if tree_diameter %2 == 0:
  print(tree_diameter//2)
else:
  print(tree_diameter//2 +1)