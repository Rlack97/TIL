#연습문제1_Gravity 풀이
#2022-08-08
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

for i in range(T):           
    n = 0
    N = int(input())         # 가로
    H = list(map(int,input().split()))      # 상자 높이 리스트
    downfall = 0                            # 낙차값 초기화         

   #각 상자들의 낙차를 비교하면 됨

    for t in range(0,N):               
        for k in range(1,H[t]+1):      # 각 상자들에 대해서         
            cnt = 0
            for i in range(t+1,N):         # 나머지 상자들을 쌓아둔 공간을 대조
                if k > H[i]:                # 자신보다 낮은 값이 있어야 빈 공간(낙차)가 생김
                    cnt += 1         
            if cnt > downfall:           # 계산된 상자의 낙차 카운트가 기존보다 크다면
                downfall = cnt             # 최댓값을 업데이트
    
    n += 1  

    print(f'#{n} {downfall}')