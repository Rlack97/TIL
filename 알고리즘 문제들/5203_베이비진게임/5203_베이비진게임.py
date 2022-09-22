# 5203_베이비진게임 풀이
# 2022/09/22

import sys
sys.stdin = open("input.txt","r")

from collections import Counter

def check(cards, num):
    global winner
    lune = 0
    triple = 0

    hand = Counter(cards)
    counts = hand.most_common(1)
    # 가장 갯수가 많은 요소를 [(요소,갯수)] 형태로 반환해주는
    # counter 함수의 .most_common 메서드 사용

    if counts[0][1] >= 3:
        triple = True
        # 3 이상이면 트리플
    
    for c in range(len(cards)):
        if cards[c]+1 in cards and cards[c]+2 in cards:
            lune = True
            # 한 값에 대해서 1 큰 값과 2 큰 값이 리스트 안에 있으면 런
    
    if triple == True or lune == True:
        winner = num
        # 둘 중 하나라도 맞으면 승리
            

T = int(input())
for tc in range(1,T+1):
    num_list = list(map(int,input().split()))
    player1 = [num_list[0],num_list[2]]
    player2 = [num_list[1],num_list[3]]
    # 3장째를 뽑기 전에는 승부를 낼 수 없으므로 2장까지는 뽑아둔 상태

    winner = 0

    for i in range(4,12):
        if i % 2: # 5,7,9,11
            player2.append(num_list[i])
            check(player2, 2)
            if winner != 0:
                break
            # 승자가 결정된 시점에서 게임을 그만두기 위한 break

        else: # 4,6,8,10
            player1.append(num_list[i])
            check(player1, 1)
            if winner != 0:
                break
    

    print('#{} {}'.format(tc, winner))
