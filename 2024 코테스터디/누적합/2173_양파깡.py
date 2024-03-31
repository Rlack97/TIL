n, m = map(int, input().split())
maps = [[0] * 31 for _ in range(31)]
sw = [[0] * 31 for _ in range(31)]
sh = [[0] * 31 for _ in range(31)]
visit = [[False] * 31 for _ in range(31)]
arr = []
res = []


def init():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sh[j][i] = sh[j - 1][i] + maps[j][i]
            sw[i][j] = sw[i][j - 1] + maps[i][j]


def get_taste(x, y, height, width):
    return sh[x + height - 1][y] - sh[x - 1][y] \
        + sh[x + height - 1][y + width - 1] - sh[x - 1][y + width - 1] \
        + sw[x][y + width - 2] - sw[x][y] \
        + sw[x + height - 1][y + width - 2] - sw[x + height - 1][y]


def check(x, y, height, width):
    for i in range(x, x + height):
        if visit[i][y] or visit[i][y + width - 1]:
            return False
    for i in range(y + 1, y + width - 1):
        if visit[x][i] or visit[x + height - 1][i]:
            return False
    return True


def visit_check(x, y, height, width):
    for i in range(x, x + height):
        visit[i][y] = visit[i][y + width - 1] = True
    for i in range(y + 1, y + width - 1):
        visit[x][i] = visit[x + height - 1][i] = True


for i in range(1, n + 1):
    maps[i][1:n+1] = list(map(int, input().split()))
init()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(3, n + 2 - i):
            for l in range(3, n + 2 - j):
                arr.append((-get_taste(i, j, k, l), i, j, k, l))
arr.sort()
for i in range(len(arr)):
    v = arr[i]
    if check(v[1], v[2], v[3], v[4]):
        visit_check(v[1], v[2], v[3], v[4])
        res.append((-v[0], v[1], v[2], v[1] + v[3] - 1, v[2] + v[4] - 1))
        m -= 1
        if m == 0:
            break

if m == 0:
    for i in range(len(res)):
        print(*res[i])
else:
    print(0)
