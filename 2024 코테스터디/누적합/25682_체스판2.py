# import sys

# input = sys.stdin.readline
# N, M, K = map(int, input().split())
# board = [str(input()).rstrip() for _ in range(N)]
# min_effort = 1e9


# # K*K 영역에서 칠하는 횟수를 구하는 함수
# def count(K_board, start_color):
#     cnt = 0
#     if start_color == "B":
#         # 왼쪽 위가 검은색
#         for k in range(K):
#             for kk in range(K):
#                 if (k + kk) % 2 == 0 and K_board[k][kk] == "W":
#                     cnt += 1
#                 elif (k + kk) % 2 == 1 and K_board[k][kk] == "B":
#                     cnt += 1
#     else:
#         # 왼쪽 위가 흰색
#         for k in range(K):
#             for kk in range(K):
#                 if (k + kk) % 2 == 0 and K_board[k][kk] == "B":
#                     cnt += 1
#                 elif (k + kk) % 2 == 1 and K_board[k][kk] == "W":
#                     cnt += 1

#     return cnt


# # 보드에서 K*K영역을 전부 순회하는 함수
# for n in range(N - K + 1):
#     for m in range(M - K + 1):
#         sub_board = [row[m : m + K] for row in board[n : n + K]]
#         paint = count(sub_board, board[n][m])
#         if paint < min_effort:
#             min_effort = paint

# print(paint)

# # 시간초과 O(N * M * K^2)

import sys

input = sys.stdin.readline

# 입력 받기
N, M, K = map(int, input().split())
board = [input().strip() for _ in range(N)]

# B로 시작하는 체스판과 W로 시작하는 체스판에 대한 불일치 배열을 만든다
mismatch_B = [[0] * (M + 1) for _ in range(N + 1)]
mismatch_W = [[0] * (M + 1) for _ in range(N + 1)]

# 체스판의 불일치 계산
for i in range(N):
    for j in range(M):
        if (i + j) % 2 == 0:
            mismatch_B[i + 1][j + 1] = (
                mismatch_B[i][j + 1]
                + mismatch_B[i + 1][j]
                - mismatch_B[i][j]
                + (board[i][j] != "B")
            )
            mismatch_W[i + 1][j + 1] = (
                mismatch_W[i][j + 1]
                + mismatch_W[i + 1][j]
                - mismatch_W[i][j]
                + (board[i][j] != "W")
            )
        else:
            mismatch_B[i + 1][j + 1] = (
                mismatch_B[i][j + 1]
                + mismatch_B[i + 1][j]
                - mismatch_B[i][j]
                + (board[i][j] != "W")
            )
            mismatch_W[i + 1][j + 1] = (
                mismatch_W[i][j + 1]
                + mismatch_W[i + 1][j]
                - mismatch_W[i][j]
                + (board[i][j] != "B")
            )

min_paint = float("inf")

# K*K 크기의 영역에서 최소 칠하기 횟수를 찾는다
for i in range(K, N + 1):
    for j in range(K, M + 1):
        repaints_B = (
            mismatch_B[i][j]
            - mismatch_B[i - K][j]
            - mismatch_B[i][j - K]
            + mismatch_B[i - K][j - K]
        )
        repaints_W = (
            mismatch_W[i][j]
            - mismatch_W[i - K][j]
            - mismatch_W[i][j - K]
            + mismatch_W[i - K][j - K]
        )

        min_paint = min(min_paint, repaints_B, repaints_W)

print(min_paint)
