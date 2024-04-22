import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())

board = [[0]*A for _ in range(B)]
directions = ['N', 'E', 'S', 'W']
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
robots = []
for n in range(N):
    x, y, d = map(str, input().split())
    x, y, d = B-int(y), int(x)-1, directions.index(d)

    robots.append((x, y, d))
    board[x][y] = n+1


for m in range(M):
    robot, order, repeat = map(str, input().split())
    robot_num, repeat = int(robot), int(repeat)
    x, y, d = robots[robot_num-1]

    if order == "L":
        d -= repeat
        if d < 0:
            d = -d
        d = d % 4
        robots[robot_num-1] = (x, y, d)

    elif order == "R":
        d += repeat
        d = d % 4
        robots[robot_num-1] = (x, y, d)

    else:
        for _ in range(repeat):
            ax = x+dx[d]
            ay = y+dy[d]
            if 0 <= ax < B and 0 <= ay < A:
                if board[ax][ay]:
                    print(
                        f"Robot {robot_num} crashes into robot {board[ax][ay]}")
                    exit()
                else:
                    continue
            else:
                print(f"Robot {robot_num} crashes into the wall")
                exit()


print('OK')
