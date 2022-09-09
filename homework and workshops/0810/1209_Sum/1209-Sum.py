# 1209_Sum 풀이
# 2022-08-10

import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    T = int(input())
    beyeol = [list(map(int,input().split())) for _ in range(100)]
    # 입력값을 받음

    list_of_sum = [] 
    # 합들을 넣을 리스트
    dsum1 = 0  # \ 대각선 합
    dsum2 = 0  # / 대각선 합

    for i in range(100):
        gsum = 0           # 가로 합
        ssum = 0           # 세로 합    
        for j in range(100):
            gsum += beyeol[i][j]
            ssum += beyeol[j][i]
        dsum1 += beyeol[i][i]
        dsum2 += beyeol[i][100-1-i]
        
        list_of_sum.append(gsum)
        list_of_sum.append(ssum)
    
    list_of_sum.append(dsum1)
    list_of_sum.append(dsum2)
    
    Mmax = 0

    for k in list_of_sum:
        if Mmax < k:
            Mmax = k
    # 최댓값 추출

    print('#{} {}'.format(tc,Mmax))
