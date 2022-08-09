# 1208_Flatten 풀이
# 2022-08-09

import sys
sys.stdin = open('input.txt','r')

# 최댓값과 최솟값을 구하는 함수 정의
def max_min(list):
    max = 0
    min = 100
    for i in range(100):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    return [max, min]


# 범위 100인 리스트 안의 최댓값과 최솟값을 1씩 교환하는 함수 정의
def solution(list):
    [max, min] = max_min(list)
    
    for i in range(100):
        if list[i] == max:
            list[i] -= 1
            break
    
    for i in range(100):
        if list[i] == min:
            list[i] += 1
            break
    return list



for tc in range(1,11):
    DT = int(input())
    Boxes = list(map(int,input().split()))
    count = 0
    while count < DT:        # 제시된 횟수만큼
        solution(Boxes)      # 덤프를 진행
        count += 1

    answer = max_min(Boxes)[0] - max_min(Boxes)[1] 
        # 최댓값 - 최솟값을 구함

    print('#{} {}'.format(tc, answer))
   

