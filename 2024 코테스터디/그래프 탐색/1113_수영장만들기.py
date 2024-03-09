from collections import deque
import sys
input = sys.stdin.readline

# 4방향탐색
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 입력
N, M = map(int, input().split())
map_list = [list(map(int, input().strip())) for _ in range(N)]
result = 0

# BFS 함수


def bfs(x, y):
    # 좌표 위치를 큐에 넣는다
    q = deque([(x, y)])

    # 시작 지점 기록
    init_val = map_list[y][x]
    min_border = 10
    result = set()
    result.add((x, y))
    while q:
        x, y = q.popleft()
        # 상하좌우 탐색
        for k in range(4):
            ax, ay = x + dx[k], y + dy[k]

            # 유효범위를 벗어낫을 경우 가장자리이므로 0을 반환
            if not (-1 < ax < M and -1 < ay < N):
                return 0, set()

            # 시작 위치보다 작거나 같은 값이고 기록되지 않은 위치일 경우
            if map_list[ay][ax] <= init_val and (ax, ay) not in result:
                # 위치를 기록
                result.add((ax, ay))
                q.append((ax, ay))

            # 시작 위치보다 값이 클 경우 = 벽
            # 벽 높이중 가장 작은 값을 저장
            elif map_list[ay][ax] > init_val:
                min_border = min(min_border, map_list[ay][ax])

    # 최소 높이와 결과값을 반환
    return min_border, result


# 결과값과 최소 벽 높이의 차이만큼의 물 양을 기록
def fill(val, coord_set):
    global result
    for x, y in coord_set:
        result += val - map_list[y][x]
        map_list[y][x] = val


for i in range(N):
    for j in range(M):
        val, coord_set = bfs(j, i)
        if coord_set:
            fill(val, coord_set)

print(result)
