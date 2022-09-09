# 4869_종이붙이기 풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt','r')


# N의 최댓값이 300이므로 총 30종류의 답만 구하면 된다
# 인덱스가 30까지 있는 리스트 생성 및 기본값 입력
result = [0]*31
result[1] = 1
result[2] = 3

# 나머지 리스트를 파악한 패턴을 활용하여 입력한다
for n in range(3,31):
    result[n] = result[n-1] + result[n-2]*2

T = int(input())
for tc in range(1,T+1):
    N = int(input())    
    
    # N은 10의 배수이므로 자릿수를 줄여주기 위해 10으로 나눔
    n = int(N/10)

    answer = result[n]
    
    print('#{} {}'.format(tc,answer))