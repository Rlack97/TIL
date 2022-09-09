# 연습문제 1 후위표기법 풀이
#2022/08/22

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    Q = input()
    stack = []
    answer = ''
    for a in Q:
        if a == '+':
            stack.append(a)
        elif a == '-':
            stack.append(a)
        elif a == '*':
            stack.append(a)
        elif a == '/':
            stack.append(a)
        else:
            answer += a

    while stack:
        answer += stack.pop()

    print('#{} {}'.format(tc, answer))