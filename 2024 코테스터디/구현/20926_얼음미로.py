# import sys
# input = sys.stdin.readline

# W, H = map(int, input().split())
# maze = [list(str(input().rstrip())) for _ in range(H)]
# visited = [[0]*W for _ in range(H)]
# terra = (-1, -1)
# out = (-1, -1)
# rocks = []
# holes = []
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# short = 1e9
# # 지형지물 기록
# for h in range(H):
#     for w in range(W):
#         if maze[h][w] == 'T':
#             terra == (h, w)
#         elif maze[h][w] == 'R':
#             rocks.append((h, w))
#         elif maze[h][w] == 'H':
#             holes.append((h, w))
#         elif maze[h][w] == 'E':
#             out = (h, w)
#         else:
#             maze[h][w] = int(maze[h][w])


# def test(now, time, dir):
#     for i in range(4):
#         # 방금 자신이 왔던 방향으로는 가지 않음
#         if dir != -1 and i == (dir + 2) % 4:
#             continue
#         ax = now[0] + dx[i]
#         ay = now[1] + dy[i]
#         dir = i

#         # 한 방향으로 계속 미끄러짐
#         while True:
#             if 0 <= ax < H and 0 <= ay < W and type(maze[ax][ay]) == int:
#                 time += maze[ax][ay]
#                 if 0 <= ax + dx[i] < H and 0 <= ay + dy[i] < W:
#                     ax += dx[i]
#                     ay += dy[i]

#                 # 범위 밖 = 절벽
#                 else:
#                     break
#             else:
#                 # 다음 칸에 뭔가가 있다? 멈춤
#                 if maze[ax][ay] == "R":
#                     # 돌 = 멈추고 다른 방향으로
#                     test((ax, ay), time, dir)
#                     # 해당 방향에서 되돌아오면 다음 방향
#                     continue
#                 if maze[ax][ay] == "H":
#                     # 구멍 = 빠지니까 끝
#                     break
#                 if maze[ax][ay] == "E":
#                     # 탈출구 = 탈출 후 시간기록
#                     short = min(short, time)
#                     break


# test(terra, 0, -1)

# print(short)


# 다익스트라
import sys
import heapq

m, n = map(int, sys.stdin.readline().rstrip().split())
INF = sys.maxsize
nodes = []
start = [0, 0]
end = [0, 0]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    row = list(sys.stdin.readline().rstrip())
    for j in range(m):
        if row[j] == 'T':
            row[j] = '0'
            start = [i, j]
        elif row[j] == 'E':
            end = [i, j]
    nodes.append(row)


def Dijkstra():
    distances = [[INF for _ in range(m)] for _ in range(n)]
    distances[start[0]][start[1]] = 0
    pq = []
    heapq.heappush(pq, [0, start[0], start[1]])

    while pq:
        cur_cost, cur_row, cur_col = heapq.heappop(pq)
        if distances[cur_row][cur_col] < cur_cost:
            continue

        for x, y in zip(dx, dy):
            next_row, next_col = cur_row, cur_col
            next_cost = 0
            while True:
                if next_row + y < 0 or next_col + x < 0 or next_row + y >= n or next_col + x >= m or not nodes[next_row+y][next_col+x].isdigit():
                    break
                next_row += y
                next_col += x
                next_cost += int(nodes[next_row][next_col])
            #     이동 가능할 때까지 빙판 이동
            if next_row + y < 0 or next_col + x < 0 or next_row + y >= n or next_col + x >= m or nodes[next_row+y][next_col+x] == 'H':
                continue
            #     다음 이동하는 곳이 구멍이라면 불가능
            elif nodes[next_row+y][next_col+x] == 'E':
                next_row += y
                next_col += x
            #     다음 이동하는 곳이 출구라면 가능
            if distances[next_row][next_col] > cur_cost + next_cost:
                distances[next_row][next_col] = cur_cost + next_cost
                heapq.heappush(pq, [cur_cost + next_cost, next_row, next_col])
    ans = distances[end[0]][end[1]]
    if ans == INF:
        return -1
    else:
        return ans


ans = Dijkstra()
print(ans)
