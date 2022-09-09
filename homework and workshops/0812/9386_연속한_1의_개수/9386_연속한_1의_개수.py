# 9386_연속한 1의 개수 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int,input()))
    maxone = 0
    cnt = 0

    for a in numbers:
        if a == 1:
            cnt += 1
            if maxone < cnt:
                maxone = cnt  # 1이 나올때마다 최댓값과 비교해서 기록
        else:
            cnt = 0           # 0 나오면 초기화
    
    print('#{} {}'.format(tc,maxone))