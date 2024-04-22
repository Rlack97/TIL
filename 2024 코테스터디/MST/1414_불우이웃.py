import sys
input = sys.stdin.readline

N = int(input())

# find union


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a

    else:
        parent[a] = b


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])

    return parent[x]


# 부모 리스트/간선리스트 생성
# 총 랜선 길이 기록
parent = list(range(N))
edges = []
total_length = 0
for n in range(N):
    line_lt = list(str(input().rstrip()))
    for m in range(N):
        if line_lt[m] == '0':
            continue
        # 대문자일경우의 ord
        elif line_lt[m].isupper():
            length = ord(line_lt[m]) - ord('A') + 27
            total_length += length
            edges.append((n, m, length))
        # 소문자일때의 ord
        else:
            length = ord(line_lt[m]) - ord('a') + 1
            total_length += length
            edges.append((n, m, length))

# 랜선 길이 오름차순 정렬
edges.sort(key=lambda x: x[2])
# 연결된 컴퓨터의 수
cnt = 0
# 컴퓨터 연결에 사용한 랜선 길이
answer = 0

# find union을 하면서
for (a, b, c) in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c
        cnt += 1

if cnt == N-1:
    print(total_length - answer)
else:
    print(-1)
