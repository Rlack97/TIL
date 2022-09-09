# 연습문제2-괄호매칭 풀이
# 2022-08-12

import sys
sys.stdin = open('input.txt','r')
T = int(input())
for tc in range (1, T+1):
    strings = input()
    stacklist = []
    # 스택에 사용할 빈 리스트 생성
    answer = 1
    for s in strings:
        if s == '(':
            stacklist.append(s)
        elif s!='(' and stacklist:
            stacklist.pop()
            # 앞에 열린 괄호가 있어야만 pop으로 짝을 맞춤
        else:
            answer = -1
            # 닫힌 괄호가 먼저 온다면 틀린 괄호
    
    if stacklist:
        answer = -1
        # 괄호가 남아있다면 틀린 괄호

    print('# {} {}'.format(tc,answer))