# 연습문제1_델타검색 풀이
# 2022-08-10

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    M = int(input())
    target_list = [list(map(int, input().split())) for _ in range(M)]
    # 입력값을 2차원 리스트로 받음

    di = [0,0,1,-1]
    dj = [1,-1,0,0]
    # 상하좌우 요소에 사용할 좌표

    summary = []
    for i in range(M):
        for j in range(M):
            O = target_list[i][j]
            # 모든 요소에 접근 후 원본 요소 값 저장

            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 상하좌우 요소에 접근

                if 0<= ni < M and 0 <= nj < M:
                    S = target_list[ni][nj]
                    summary.append(abs(O-S))
                    # 리스트 좌표값을 벗어나지 않았을 경우에 차의 절댓값을 구해서 리스트에 저장
    answer = 0
    for a in summary:
        answer += a
    # 리스트에 저장된 값을 전부 합침

    print('#{} {}'.format(tc,answer))

