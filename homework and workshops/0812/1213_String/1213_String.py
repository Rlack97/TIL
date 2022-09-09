# 1213_String 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt','r', encoding='UTF_8')

for tc in range(10):
    # 브루트 포스 사용
    T = int(input())
    goal = input()
    obj = input()

    cnt = 0
    for a in goal:
        cnt +=1
    M = cnt
    # 패턴의 길이 구하기

    cnt2 = 0
    for k in obj:
        cnt2+= 1
    N = cnt2
    # 전체 텍스트의 길이

    i=0 # 텍스트 인덱스
    j=0 # 패턴 인덱스

    words = 0

    while j<M and i<N:
        if obj[i] != goal[j]:
            i = i - j 
            j = -1
            # 반복문에서 1칸씩 더하는 것을 고려하여 위치 초기화

        i += 1
        j += 1 # 한 칸씩 나아가면서 비교

        if j == M:  # 패턴의 끝에 도달하면 카운트 +1 한 뒤에 초기화
            words += 1
            j = 0

    print('#{} {}'.format(T,words))