import sys
input = sys.stdin.readline


N, M = map(int, input().split())
colleages = list(map(str, input().rstrip().split(' ')))
roads = [list(map(int, input().split())) for _ in range(M)]

# 간선정보 가중치 기준 정렬
roads.sort(key=lambda x: x[2])
# 자기 자신을 값으로 갖는 부모 기록 리스트
parent = [i for i in range(N+1)]
answer = 0

# x = 노드번호
# 자기 자신의 부모가 자신이 아닐 경우, 부모의 부모를 자신의 부모로 삼는다.


def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 노드의 부모 크기를 비교하여, 값이 더 작은 쪽이 다른 쪽의 부모가 된다.


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


edge = 0
# 가중치 순으로 정렬해 둔 리스트를 순회하면서
for a, b, cost in roads:
    if colleages[a-1] == colleages[b-1]:
        continue

    # 두 노드의 부모가 같지 않다면 union함수를 실행 후 최단거리 가중치 계산에 더한다.
    elif find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost

        # MST의 간선 수를 카운트하기 위함
        edge += 1

# 모든 학교를 연결하는 경로가 없을 경우
# 크루스칼 알고리즘 실행 이후 MST가 아니다?
# = 연결되지 않는 노드가 있다 (순환 불가능)
# 즉 MST의 간선 수가 노드 수 -1보다 작아진다
if edge < N-1:
    print(-1)
else:
    print(answer)
