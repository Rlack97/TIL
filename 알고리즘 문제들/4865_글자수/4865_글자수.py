# 4865_글자수 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    C = []
    mmax = 0
    # 입력값 받고 출력값 초기화

    for a in str1:
        # str1 안의 각 글자에 대해서

        cnt = 0
        for b in str2:
            if a == b:
                cnt += 1
                # str2를 순회하면서 글자가 같으면 카운트 +1 
        C.append(cnt)

    for k in C:
        if k >= mmax:
            mmax = k
            # 완성된 리스트에서 최대값 출력

    print('#{} {}'.format(tc, mmax))