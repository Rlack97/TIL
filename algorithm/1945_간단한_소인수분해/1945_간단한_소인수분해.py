# 1945_간단한 소인수분해 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

# 소인수분해 함수를 정의
def soinsu(N):
    a,b,c,d,e = 0,0,0,0,0

    while True:
        if N % 2 == 0:
            N = N/2
            a += 1
        
        elif N % 3 == 0:
            N = N/3
            b += 1

        elif N % 5 == 0:
            N = N/5
            c += 1

        elif N % 7 == 0:
            N = N/7
            d += 1

        elif N % 11 == 0:
            N = N/11
            e += 1
        # 각 소인수로 나눠지지 않을 때까지 나눈 후 횟수를 기록

        else:
            break
        # 더 이상 나눠지지 않는다면 반복문 종료

    return a,b,c,d,e


T = int(input())
for tc in range(1,T+1):
    N = int(input())   
    a,b,c,d,e = soinsu(N)
    # 인풋값에 함수를 적용하고 반환된 값을 다시 변수에 지정

    print('#{} {} {} {} {} {}'.format(tc,a,b,c,d,e)) 