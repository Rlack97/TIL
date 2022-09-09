# 4875_미로 풀이
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    stack = []
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                a, b = i, j

   if 0 <= a < N and 0 <= b < N:
       if visited[a][b] or miro [a][b] == 1:
           return?
       elif maze[a][b] == 3:
           answer = 1
       else:
           stack.append([a,b])
           visited[a][b] = 1





    print('#{} {}'.format(tc, answer))
