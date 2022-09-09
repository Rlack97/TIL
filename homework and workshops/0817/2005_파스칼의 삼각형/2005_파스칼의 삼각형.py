# 2005-파스칼의 삼각형 풀이
# 2022-08-12


import sys
sys.stdin = open('input.txt','r')

def pascal(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else: 
        p = [1]
        for a in range(n-2):
            p.append(pascal(n-1)[a]+ pascal(n-1)[a+1])
        p.append(1)
        return p

# 파스칼의 삼각형의 각 행을 구하는 함수를 정의


T = int(input())
for tc in range(1,T+1):
    N = int(input())
       
    
    print('#{}'.format(tc))
    for i in range(1,N+1):
        print(*pascal(i))
        # 각 행을 언패킹해서 출력