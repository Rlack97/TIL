from itertools import combinations
from collections import deque
import copy

# 입력 받기
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 바이러스 퍼트리기
def bfs(temp_lab):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if temp_lab[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                queue.append((nx, ny))


# 안전지대 세기
def get_safe_area(temp_lab):
    safe_area = 0
    for i in range(n):
        for j in range(m):
            if temp_lab[i][j] == 0:
                safe_area += 1
    return safe_area


# 풀기
def solve():
    # 빈칸좌표
    empty_spaces = [(i, j) for i in range(n) for j in range(m) if lab[i][j] == 0]
    max_safe_area = 0

    # 그냥 3개 뽑아서 벽세우기
    for walls in combinations(empty_spaces, 3):
        temp_lab = copy.deepcopy(lab)
        for wall in walls:
            temp_lab[wall[0]][wall[1]] = 1

        bfs(temp_lab)

        max_safe_area = max(max_safe_area, get_safe_area(temp_lab))

    return max_safe_area


print(solve())

# 시간초과 날 줄 알았는데, 깡 콤비네이션 + 이중for문 사용해도 괜찮았다...
