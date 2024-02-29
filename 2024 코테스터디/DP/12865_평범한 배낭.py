#0226
#DP
# https://claude-u.tistory.com/208
import sys

N, K = map(int, input().split())
stuff = [[0,0]]

# 무게 X 물건의 수 로 된 이중그래프 생성
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# 물건의 무게와 가치를 리스트에 삽입
for _ in range(N):
    stuff.append(list(map(int, input().split())))


# 1부터 순회 (물건 수, 무게 순서)
for i in range(1, N + 1):
    for j in range(1, K + 1):
        
        # i번째 물건의 무게와 가치
        weight = stuff[i][0] 
        value = stuff[i][1]
       
       # j, 즉 현재의 무게 제한이 물건의 무게보다 작으면?
        if j < weight:
            #weight보다 작으면 위 칸의 값을 그대로 가져온다
            knapsack[i][j] = knapsack[i - 1][j] 
        else:
            # 그렇지 않으면 현재 물건 가치 + 이전 물건 | 현재 물건 무게를 뺀 가능한 무개, 이전 물건 | 현재 가방 무게 중 큰 것을 선택한다.
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])