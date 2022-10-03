# 10726 이진수 표현
# 2022/10/13

import sys
sys.stdin = open('input.txt','r')

T= int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())

    for _ in range(N):
        if M % 2 == 0:
            flag = "OFF"
            # 뒤에서부터 N 자리의 비트 값이라는 것은
            # 이진수 계산 앞부분의 N번 계산 내라는 뜻이므로
            # N번동안 2로 나눌 때 나머지가 전부 1이어야 한다는 것이다.
            break
        else:
            M = M // 2
        
    else: 
        flag = "ON"
    
   
    print('#{} {}'.format(tc, flag))
