# 4864_문자열 비교 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    N, M = len(str1), len(str2)
    # 입력값을 받고 길이를 잼

    n, m = 0, 0
    # str1과 str2의 인덱스 정보
    while n < N and m < M:
        if str1[n] != str2[m]:
            m = m-n
            n = -1
            # 두 str의 값이 맞지 않는다면 str1은 0으로 초기화,
            # str2는 n을 진행했던 만큼 뒤로 간다.

        if n == N-1:
            answer = 1
            break
            # str1의 끝까지 순회가 완료되었다면 문자열이 존재하는 것이므로 1
            # 이후 브레이크

        n += 1
        m += 1
            # 두 문자열의 인덱스를 1 진행

        answer = 0
            # 브레이크 되기 전까지는 문자열이 존재하지 않으므로 0

    
    print('#{} {}'.format(tc, answer))