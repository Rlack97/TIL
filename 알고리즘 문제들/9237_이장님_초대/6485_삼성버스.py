# 9237_이장님 초대
# 2023-03-16
import sys
sys.stdin = open('input.txt','r')
# 최대한 빨리 이장님을 초청할 수 있는 경우
# 하루에 1개만 심을 수 있으므로, 가장 오래 걸리는 나무부터 심는다.
# 나무가 다 자라는 날을 기록하고, 기록 중에서 가장 늦는 날 +1하면 답.
T = int(input())


# 끝나는 날을 기록할 변수
duration = list(map(int,sys.stdin.readline().split()))
# for i in range(T-1,0,-1):
#     for j in range(0,i):
#         if duration[j] < duration[j+1] :
#             duration[j+1], duration[j] = duration[j], duration[j+1]
#버블정렬 (시간초과)

duration.sort()
# 기본 라이브러리는 착실히 씁시다... 야발

endDay = 0
for i in range(1,T+1):
    treeGrowth = i+duration[-i]
    if endDay < treeGrowth:
        endDay = treeGrowth
    
print(endDay+1)