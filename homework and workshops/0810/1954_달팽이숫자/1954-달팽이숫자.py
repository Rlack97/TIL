# 1954_달팽이숫자 풀이
# 2022-08-10

import sys
sys.stdin = open("input.txt")

T = int(input())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    # 이차원 리스트 초기화

    i, j, k = 0, 0, 0
    # x좌표, y좌표, dxdy의 인덱스값

    for n in range(1, N*N + 1): # 총 N*N의 수
        snail[i][j] = n 
        i += dy[k]
        j += dx[k]
        # 값을 할당하고 움직임 좌표에 맞춰 좌표를 변경

        if i < 0 or j < 0 or i >= N or j >= N or snail[i][j] != 0:
            i -= dy[k]
            j -= dx[k]
            # 변경한 좌표가 범위를 벗어났거나 이미 방문한 곳일 경우 취소

            k = (k + 1) % 4
            # 방향(k값)을 바꾸고 4로 나눈 나머지 인덱스로 이동

            i += dy[k]
            j += dx[k]
            # 다시 칸을 전진

    print("#{}".format(tc))
    for a in snail:
        print(*a)
