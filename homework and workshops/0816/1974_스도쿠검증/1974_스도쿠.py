# 1974_스도쿠 검증 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt','r')

complete_list = {1,2,3,4,5,6,7,8,9}

T = int(input())
for tc in range(1,T+1):
    map1 = [list(map(int,input().split())) for _ in range(9)]
    answer = 1
    # 가로
    for i in range(9):
        row = set()
        for j in range(9):
            row.add(map1[i][j])
        if row != complete_list:
            answer = 0
            break

    # 세로
    for i in range(9):
        colunm = set()
        for j in range(9):
            colunm.add(map1[j][i])
        if colunm != complete_list:
            answer = 0
            break

    # 사각형
    for i in [0,3,6]:
        for j in [0,3,6]:
            square = set()
            for k in range(3):
                for t in range(3):
                    square.add(map1[i+k][i+t])
            if square != complete_list:
                answer = 0
                break
    
    print('#{} {}'.format(tc, answer))
