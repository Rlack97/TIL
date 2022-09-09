# 1234_비밀번호 풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    word_length, password = map(str,input().split())
    # int로 받으면 앞부분의 0이 다 사라져버리므로 주의.
    # word_length를 사용하고 싶으면 이렇게 받은 뒤에 다시 int화 해주자
    
    stack = []
    for p in password:
        if stack and p == stack[-1]:
            stack.pop()
        else:
            stack.append(p)

    answer = ''.join(stack)
    # '구분자'.join(list) 기억해두자

    print('#{} {}'.format(tc,answer))