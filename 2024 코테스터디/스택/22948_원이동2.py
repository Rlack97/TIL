import sys
from collections import deque
input = sys.stdin.readline

# 각 원은 접점이 없음 = 각 원은 모두 하나의 부모를 지님
# 트리 형태로 구축 가능 => 이후 bfs를 통해 가장 짧은 노드 탐색
# 트리구축 = x축과의 접점을 통해 괄호여닫기

# 기본입력
N = int(input())
circles = [list(map(int,input().split())) for _ in range(N)]
start, end = map(int,input().split())

# x축 좌표 입력 및 순차화
x_line = []
for c in circles:
  x_line.append((c[1] - c[2],+c[0]))
  x_line.append((c[1] + c[2],-c[0]))
x_line.sort()

stack = [0]
graph = [[]for _ in range(N+1)]

# 트리 생성
for c in x_line:
  x, p = c[0], c[1]

  # 음수 = 원 닫힘 = 부모 원 번호 바뀜
  if p < 0:
    stack.pop()
  
  # 양수 = 원 열림 = 부모 원 바뀜 + 직전 원과의 부모관계
  else:
    # 트리 연결처리
    graph[p].append(stack[-1])
    graph[stack[-1]].append(p)
    stack.append(p)

# 부모를 기록하며 들어가는 BFS(큐)
def bfs(graph, start, goal):
  visited = set([start])
  parent = {start:None}
  queue = deque([start])

  while queue:
    current = queue.popleft()
    
    if current == goal:
      path = []
      while current is not None:
        path.append(current)
        current = parent[current]
      path.reverse()
      return len(path), path
      
    for neighbor in graph[current]:
      if neighbor not in visited:
        visited.add(neighbor)
        parent[neighbor] = current
        queue.append(neighbor)
  
  return None

distance, track = bfs(graph, start, end)

print(distance)
print(*track)
