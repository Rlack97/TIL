# 1224_계산기3 풀이
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')


def prior(k):
    if k == '*':
        return 3
    elif k == '+':
        return 2
    elif k == '(' or k == ')':
        return 0
    else:
        return 1
# 우선도를 출력하는 함수 정의

def change(c):
    stack = []
    done = []
    for i in c:
        k = prior(i)
        # 요소의 우선도를 검사

        if i == '(':
            stack.append(i)
        elif i == ')':
            while True:
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    done.append(stack.pop())
                    # 닫힌 괄호가 나온다면 스택에서 열린 괄호가 나올 때 까지 pop하여
                    # 처리 완료 리스트에 추가. 
                    # 열린 괄호 자체는 pop하여 제거

        elif k == 3:
            while stack:
                if prior(stack[-1]) < k:
                    break
                done.append(stack.pop())
            stack.append(i)

        elif k == 2:
            while stack:
                if prior(stack[-1]) < k:
                    break
                done.append(stack.pop())
            stack.append(i)
            # 각 연산자는 자신보다 우선도가 낮은 연산자가 나오기 전까지
            # stack에 저장되어 있는 연산자를 pop하여 완료 리스트에 추가
            # 그 후 자신을 스택에 저장

        else:
            done.append(int(i))
            # 숫자는 정수화하여 바로 완료 리스트에 추가

    while stack:
        done.append(stack.pop())
        # 스택에 남아있는 연산자가 있을 경우 추가

    return done


def calculate(num):
    stack = []
    for i in num:
        if i == '+':
            B = stack.pop()
            A = stack.pop()
            stack.append(A+B)
        elif i == '*':
            B = stack.pop()
            A = stack.pop()
            stack.append(A*B)
        else:
            stack.append(i)
    return stack
    # 완성된 후위표기식을 계산하는 함수.
    # 첫번째 pop이 뒤에 오는 수임을 주의 (-나 /의 경우)


for tc in range(1, 11):
    length = int(input())
    code = input()
    print('#{} {}'.format(tc, *calculate(change(code))))
