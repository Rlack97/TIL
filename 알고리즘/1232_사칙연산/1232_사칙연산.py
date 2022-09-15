# 1232_사칙연산 풀이
# 2022/09/15

import sys
sys.stdin = open('input.txt','r')

def centerorder(node):
    global answer_value

    if cal[node]:
        return_value = cal[node]
        centerorder(L[node])
        answer.append(cal[node])
        centerorder(R[node])

        if cal[node] == '+':
            return_value = centerorder(L[node]) + centerorder(R[node])

        elif cal[node] == '-':
            return_value = centerorder(L[node]) - centerorder(R[node])

        elif cal[node] == '*':
            return_value = centerorder(L[node]) * centerorder(R[node])

        elif cal[node] == '/':
            return_value = centerorder(L[node]) / centerorder(R[node])


        return return_value
    # 중위 순회를 통해 사칙연산을 하는 함수

for tc in range(1,11):
    N = int(input())
    cal = [0]*(N+1)
    L = [0]*(N+1)
    R = [0]*(N+1)
    # 트리 값, 자손을 기록하기 위한 빈 리스트

    for n in range(1,N+1):
        value_list = list(map(str,input().split()))

        if value_list[1].isdigit():
            cal[n] = int(value_list[1])
            # 값이 숫자일 때는 숫자로 변환해서 저장
        else: 
            cal[n] = value_list[1]            
            # 연산부호는 그대로 저장
        
        if len(value_list) >= 3:
            L[n] = int(value_list[2])

        if len(value_list) >= 4:    
            R[n] = int(value_list[3])

    answer = []
    
    print('#{} {}'.format(tc, int(centerorder(1))))