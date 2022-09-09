# 3143_가장빠른문자열타이핑 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    A, B = map(str,input().split())
    # 입력값을 받습니다

    A = A.replace(B,' ')
    # A 안의 B를 빈칸 하나로 변경

    c = 0
    for a in A:
        c += 1
    # A 내의 요소 갯수 확인

    print('#{} {}'.format(tc, c))
    