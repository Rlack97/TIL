# 시청률 = 인기도 a + 인기도 b / abs(실력a - 실력b) 보다 작거나 같은 가장 큰 정수
# 승 패를 임의로 정할 수 있음
# 시청률이 최대가 되게 하려면?
# 진 사람이 계속 경기를 하게 된다 = 토너먼트 구조 = 트리 = 최대 스패닝 트리 (시청률 최댓값)
# 1. 시청률 최댓값
# 2. 해당 경우의 대전표 (패 승 순으로 출력)
# 최소 x,  최대 신장 트리 = find union 함수 + heapq
import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
chef_list = [[0, 0]]
for _ in range(N):
    chef_list.append(list(map(int, input().split())))
parent = [i for i in range(N+1)]

# 자기 자신의 부모가 자신이 아닐 경우, 부모의 부모로 값을 타고 올라감


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

# 노드번호가 작은 쪽을 다른쪽의 부모로 삼는다

# 두 노드의 부모가 같을 경우 생략
# 다를 경우 b의 부모가 a가 된다? 왜지


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False
    else:
        parent[b] = a
        return True

# 시청률 계산 함수


def view_rate(a, b):
    p1, c1 = chef_list[a][0], chef_list[a][1]
    p2, c2 = chef_list[b][0], chef_list[b][1]
    rate = int((c1+c2)/abs(p1-p2))
    return rate


hq = []
nodes = [[] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(i+1, N+1):
        # 최대 스패닝 트리 = 최소 스패닝 트리에서
        # 가중치(얻고자 하는 값)에 - 붙여버리면 된다
        heapq.heappush(hq, [-view_rate(i, j), i, j])


total = 0

while hq:
    cost, node1, node2 = heapq.heappop(hq)
    if union(node1, node2):
        total += cost
        nodes[node1].append(node2)
        nodes[node2].append(node1)
        # 인접리스트 생성

print(-total)

visited = [False for _ in range(N+1)]
answer = []


def DFS(node):
    visited[node] = True
    for next in nodes[node]:
        if not visited[next]:
            DFS(next)
            print(node, next)


DFS(1)
