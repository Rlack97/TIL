# 4834-숫자카드
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())                    # 숫자 리스트 길이
    L = list(map(int,input()))          # 숫자 리스트
    blanklist = [0]*10                  # 카운트를 위한 공백리스트

    for a in L:
        blanklist[a] += 1               
        # 각 숫자카드의 값을 인덱스로 하는 공백리스트의 위치에 횟수를 기록
    
    max = 0
    id = 0
    for k in range(10):
        if blanklist[k] >= max:
            max = blanklist[k]
            id = k
            # 횟수가 같더라도, 더 큰 수가 나오면 id(카드의 수) 갱신
    
    print('#{} {} {}'.format(tc,id,max))