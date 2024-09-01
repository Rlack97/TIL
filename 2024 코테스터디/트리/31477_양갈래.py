import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
N = int(input())
nodes = [[] for _ in range(N+1)]

for _ in range(N-1):
  A,B,V = map(int,input().split())
  nodes[A].append((B,V))
  nodes[B].append((A,V))

# 독이 퍼지기 시작하는 곳은 연결된 곳이 하나밖에 없는 곳, 즉 리프노드
# 양갈래가 있는 곳은 1번
# 루트노드와(1) 리프노드(독)을 제외한 노드들 중에서
# 부모 노드와 연결된 가지의 두께 vs 자식 노드와 연결된 가지의 두께 합 중 작은 값을 골라야 한다.

# dfs 부모노드를 기록하면서 하위 dfs(자식노드)에서의 반환값과 부모노드로의 간선 가중치를 비교
parents = [0] * (N+1)
def dfs(node,parent):
  # 리프 노드의 경우 부모와의 연결비용 반환
  if len(nodes[node]) == 1 and node != 1:
    parent_cost = next(weight for child, weight in nodes[node] if child == parent)
    return parent_cost
  
  total_child_cost = 0
  parents[node] = parent

  for child, weight in nodes[node]:
    if child != parent:
      child_cost = dfs(child,node)
      total_child_cost += min(child_cost,weight)
    
  # 부모와의 연결 비용, 자식과의 연결 비용 중 작은 값을 반환
  if node != 1:
    parent_cost = next(weight for child, weight in nodes[node] if child == parent)
    return min(total_child_cost, parent_cost)
  # 1은 루트노드니까 부모가 없음
  else:
    return total_child_cost


answer = dfs(1,-1)
print(answer)

