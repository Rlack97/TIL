from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
students = [input().strip() for _ in range(5)]


# 25개의 좌표 (0, 0) ~ (4, 4) 중 7개를 선택하는 함수
def bfs(candidate):
    queue = deque([candidate[0]])
    visited = [candidate[0]]
    s_count = 0

    if students[candidate[0][0]][candidate[0][1]] == "S":
        s_count += 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if (
                0 <= nx < 5
                and 0 <= ny < 5
                and (nx, ny) in candidate
                and (nx, ny) not in visited
            ):
                visited.append((nx, ny))
                queue.append((nx, ny))
                if students[nx][ny] == "S":
                    s_count += 1

    # 7명 모두 연결되어 있고, S파 학생이 4명 이상이면 True 반환
    return len(visited) == 7 and s_count >= 4


# 좌표 리스트 생성
coordinates = [(i, j) for i in range(5) for j in range(5)]

result = 0

# 7명의 자리를 선택하는 모든 경우의 수
for candidate in combinations(coordinates, 7):
    if bfs(candidate):
        result += 1

print(result)
