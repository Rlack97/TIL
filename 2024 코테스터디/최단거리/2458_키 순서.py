# 0227
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# graph = [[set(), set()] for n in range(N+1)]
# for _ in range(M):
#     # a학생이 b학생보다 작음
#     a, b = map(int, input().split())
#     graph[a][1].add(b)
#     graph[b][0].add(a)

# 각 인덱스에 (나보다 작음, 나보다 큼) 의 배열 생성
# A 학생보다 작은 학생이 지닌 [나보다 작음] 배열의 학생들은 사람들은 A보다 작고,
# A 학생보다 큰 학생이 지는 [나보다 큼] 배열의 학생들은 A보다 크다
# 두 배열을 합쳤을 때 N-1 개의 요소가 있어야 자신의 위치를 정확히 알 수 있음.


# def set_update(a, h):
#     flag = True
#     while flag is True:
#         res = set()
#         for i in a:
#             if a.issubset(graph[i][h]):
#                 continue
#             else:
#                 res.update(graph[i][h])
#         a.update(res)
#         if res == set():
#             flag = False

#     return a


# for g in graph:
#     g[0].update(set_update(g[0], 0))
#     g[1].update(set_update(g[1], 0))


# ans = 0

# for g in graph:
#     total = len(g[0]) + len(g[1])
#     if total == N-1:
#         ans += 1

# print(ans)

# 플로이드와샬

height = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    tall, short = map(int, sys.stdin.readline().split())
    height[tall][short] = 1

# 플로이드 와샬 알고리즘
for k in range(1, N+1):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(1, N+1):
        for j in range(1, N+1):
            if height[i][j] == 1 or (height[i][k] == 1 and height[k][j] == 1):
                height[i][j] = 1  # 자신보다 작은 경우


# 출력
answer = 0
for i in range(1, N+1):
    known_height = 0
    for j in range(1, N+1):
        known_height += height[i][j] + height[j][i]  # 자신보다 작은사람과 큰사람의 합
    if known_height == N-1:  # 자신의 키 순서를 알 경우
        answer += 1
print(answer)
