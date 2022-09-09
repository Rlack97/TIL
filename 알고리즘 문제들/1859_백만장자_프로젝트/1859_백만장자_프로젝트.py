# 1859_백만장자_프로젝트 풀이
# 2022-08-16

import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    answer = 0

    price.reverse()
    # 이윤을 보기 위해서는 앞에서 높은 가격을 사서 뒤에서 가장 비싼 가격으로 팔 필요가 있으므로
    # 리스트를 뒤집음
    high_price = 0

    for n in price:
        if n > high_price:
            high_price = n
            # 최고가 갱신
        
        if n < high_price:
            answer += high_price-n
            # 최고가보다 낮은 가격은 하나 사서 이윤을 차이만큼 남길 수 있음

    


    print('#{} {}'.format(tc, answer))