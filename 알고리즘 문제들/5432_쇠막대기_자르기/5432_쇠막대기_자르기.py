# 5432_쇠막대기_자르기 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    A = []
    pipe = input()
    cnt = 0
    for i in pipe:
        cnt += 1
    
    stick = 0
    layer = 0
    for k in range(cnt):
        if pipe[k] == '(' and pipe[k+1] != ')':
            layer += 1

        elif pipe[k] == ')':
            if pipe[k-1] == '(':
                stick += layer
            else:
                layer -=1
                stick +=1
  

    print('#{} {}'.format(tc, stick))