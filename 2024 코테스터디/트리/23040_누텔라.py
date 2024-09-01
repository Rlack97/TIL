# 누텔라 트리 (Easy) : 골드 3
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
E = [[] for _ in range(N+1)] # 간선
P = [i for i in range(N+1)] # 집합 부모 정보
L = [0 for _ in range(N+1)] # 집합 크기(rank)
B = []  # 검정 노드
R = []  # 빨강 노드
answer = 0

# 유니온 파인드 사용
def union(a, b):
    a = find(a)
    b = find(b)
    if a!=b:
        P[b] = a
        L[a] += L[b]

def find(a):
    if a!=P[a]:
        P[a] = find(P[a])
    return P[a]


# 간선 정보 저장
for _ in range(N-1):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)


# 노드 색상별로 분리
C = " " + input()

for i in range(1, len(C)):
    if C[i] == "R":
        R.append(i)
        # 집합 크기(rank) 초기화
        L[i] = 1

    elif C[i] == "B":
        B.append(i)

# 빨강 노드에 대해 유니온파인드 실행
for n in R:
    for m in E[n]:
        if C[m]=="R":
            union(n, m)

# 검정 노드를 포함하는 모든 누텔라 찾기
for n in B:
    # 검정끼리는 L[m]이 0이므로 다 더함
    for m in E[n]:
        answer += L[find(m)]

print(answer)