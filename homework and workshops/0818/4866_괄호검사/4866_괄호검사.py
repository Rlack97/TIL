# 4866_괄호검사 풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt','r')

# 괄호검증 함수 정의
def Test(S):
    stack = []
    # 스택 초기화

    for si in S:
        if si == '(' or si == '{':
            stack.append(si)
            # 여는 괄호는 스택에 저장

        elif si == ')':
            if  stack and stack[-1] == '(' :
                stack.pop()
                # 닫는 괄호가 나왔을 때, 스택이 존재하고
                # 마지막 값의 짝이 맞을 때 pop
            else:
                return 0
                # 위의 조건 중 하나라도 맞지 않는다면 틀린 괄호
        elif si == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0
                # 위와 동일한 구조
    
    if stack == []:
        return 1
        # 모든 작업이 끝난 후 스택이 비어있어야 옳은 괄호
        
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    code = input()
  
    answer = Test(code)

    print('#{} {}'.format(tc,answer))