# 4873_반복문자_지우기 풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt','r')

# 리스트로 받은 뒤 a[i] == a[i+1] 과 같이
# 요소 간 검증을 진행하게 되면 index 재분배로 인한
# 연산 수, 즉 시간복잡도가 증가

# 스택 사용

# 반복문을 지우는 함수 정의
def delete_multi(string):
    stack = []
    # 비어있는 스택 정의

    for a in string:
        if stack == []:
            stack.append(a)
            continue
        # 스택이 비어 있다면 자신을 스택에 push하고 다음 요소 진행
        else:
            if a == stack[-1]:
                stack.pop()
                continue
            # 스택의 가장 마지막 값과 자신이 같다면 반복문이므로 
            # 자신을 push하지도 않고, 스택에서 pop을 해줌으로써
            # 반복되는 문자 2개를 제거
            else:
                stack.append(a)
            # 반복문이 아닌 경우 스택에 push
    
    return stack
            



T = int(input())
for tc in range(1,T+1):
    strings = input()

    S = delete_multi(strings)
    
    cnt=0
    for s in S:
        cnt += 1

    # len 미사용을 위한 for문
    # 함수 정의에 섞어서 연산수를 줄일 수 있지 않았을까?

    print('#{} {}'.format(tc,cnt))