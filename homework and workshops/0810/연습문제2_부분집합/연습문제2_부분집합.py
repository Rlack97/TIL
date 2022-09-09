# 연습문제2-부분집합 풀이
# 2022-08-10

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    real_num = list(map(int,input().split())) 
    #10개의 정수
    total_part = []
    # 부분집합의 합을 담을 리스트

    for i in range(1<<10):  
        # 부분집합의 총 갯수 2^10 = 1024 개 

        part = []   
        # 부분집합을 담을 리스트


        for j in range(10):
            # 10개의 정수들 중에서

            if i & (i<<j):
                # 비트연산을 통해 해당 요소가 부분집합에 포함되는지 검증

                part.append(real_num[j])
                # 검증된 요소를 부분집합에 담음
        
        Asum = 0   
        for k in part:
            Asum += k
        total_part.append(Asum)
        
        # 부분집합의 합을 구해 리스트에 추가

    del total_part[0] 
    # 첫 번째 부분집합, 즉 공집합을 제거

    if 0 in total_part:
        answer = 1
    else:
        answer = 0
    # 합이 0이 되는 부분집합이 존재하는지 검증

    print('#{} {}'.format(tc,answer))




