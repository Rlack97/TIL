# 1223_계산기2 풀이
# 2022-08-22

import sys
sys.stdin = open('input.txt', 'r')

def priority(char):
    if char == '*':
        return 3
    if char == '+':
        return 2
    else:
        return 1
# 우선순위 설정

def postfix():
    stack = []
    done = []
    for i in range(N):
        num = priority(case[i])    # case 내의 요소들에 대한 우선도
        if num ==3:
            while stack:
                if priority(stack[-1]) < num:
                    break
                done.append(stack.pop())
            stack.append(case[i])
        elif num ==2:
            while stack:
                if priority(stack[-1]) < num:
                    break
                done.append(stack.pop())
            stack.append(case[i])
        else:
            done.append(int(case[i]))

            # 연산자가 나왔을 경우, 스택 안에 저장된 다른 연산자들이 자신보다 우선순위가
            # 낮을 때까지 pop을 진행
    
    while stack:
        done.append(stack.pop())
    # 남아 있는 연산자 추가

    return done

def calculate(num):
    stack = []
    for i in range(N):
        if num[i] == '+':
            B = stack.pop()
            A = stack.pop()
            stack.append(A+B)
        elif num[i] == '*':
            B = stack.pop()
            A = stack.pop()
            stack.append(A*B)
        else:
            stack.append(num[i])
    return stack


for tc in range(1,11):
    N = int(input())
    case = list(map(str, input()))

    print('#{} {}'.format(tc, *calculate(postfix())))