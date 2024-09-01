import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
curves = [list(map(int, input().split())) for _ in range(N)]
# 시작 점x,y, 시작 방향, 세대
max_gene = max(curve[3] for curve in curves)

board = [[0] * 101 for _ in range(101)]
dir = defaultdict(list)

# 0세대의 방향 = 0 (추후 조정)
dir[0] = [0]

# 최대 세대만큼 계산해두면 기본 방향값만 계산해두면 차후 방향이 다 나오므로
# 각 세대의 드래곤 커브 방향
for i in range(1, max_gene + 1):
    # 이전 세대(i-1) + 이전 세대를 거꾸로 한 값에 방향 + 1(시계방향 전환) (i-1)[::-1]에 x+1%4연산
    dir[i] = dir[i - 1] + list(map(lambda x: (x + 1) % 4, dir[i - 1][::-1]))

# 우 상 좌 하, d값 0 1 2 3 순서
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

# 보드에 드래곤 커브 그리기
for s, e, d, g in curves:
    board[e][s] = 1

    # 해당 세대에 맞는 드래곤 커브 방향마다
    for dd in dir[g]:
        # 초기 드래곤커브를 감안한 방향 수정
        ad = (d + dd) % 4

        # 방향에 맞는 진행 및 기록
        e += directions[ad][0]
        s += directions[ad][1]
        board[e][s] = 1

answer = 0
for x in range(100):
    for y in range(100):
        if board[x][y] and board[x][y + 1] and board[x + 1][y] and board[x + 1][y + 1]:
            answer += 1

print(answer)
