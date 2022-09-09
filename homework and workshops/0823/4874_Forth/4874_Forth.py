# 4874_Forth 풀이
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    code = list(map(str, input().split()))
    stack = []
    answer = 0
    for c in code:
        try:
            if c == '+':
                B = stack.pop()
                A = stack.pop()
                C = int(A) + int(B)
                stack.append(C)
            elif c == '-':
                B = stack.pop()
                A = stack.pop()
                C = int(A) - int(B)
                stack.append(C)
            elif c == '*':
                B = stack.pop()
                A = stack.pop()
                C = int(A) * int(B)
                stack.append(C)
            elif c == '/':
                B = stack.pop()
                A = stack.pop()
                C = int(A) // int(B)
                stack.append(C)
            elif c == '.':
                if len(stack) >= 2:
                    answer = 'error'
                else:
                    answer = stack[-1]
            else:
                stack.append(c)
        except IndexError:
            answer = 'error'

    print('#{} {}'.format(tc, answer))
