## 2579_계단오르기
## 2022-10-21

import sys
sys.stdin = open('input.txt','r')

stairs = int(input())
scores = [0]*(stairs+1)

for i in range(1,stairs+1):
    scores[i] = int(input())

dp = [0]* (stairs+1)

if stairs ==1:
    print(scores[1])
    exit()
elif stairs==2:
    print(sum(scores[:3]))
    exit()
dp[1] = scores[1]
dp[2] = scores[1] + scores[2]

for i in range(3, stairs+1):
    dp[i] = max(dp[i-2]+scores[i], dp[i-3]+scores[i-1]+scores[i])

print(dp[-1])


# 한번에 한 계단 또는 두 계단씩
# 연속된 세 개의 계단을 모두 밟으면 안된다. 
# 마지막 계단은 반드시 밟아야 한다.
# 점수의 최댓값은?

# DP? DFS같은데.
# score = 0
# idx = -1
# stack = 0
# max_score = 0

# def DFS():
#     global idx, score, max_score, stack

#     if idx == stairs-1:
#         if max_score < score:
#             max_score = score

#     else:
#         if stack < 2:
#             idx +=1 
#             stack += 1
#             score += scores[idx]
#             DFS()
#             score -= scores[idx]
#             stack -=1
#             idx-=1

#         if idx < stairs-2 :
#             idx +=2
#             stack =1
#             score += scores[idx]
#             DFS()
#             score -= scores[idx]
#             stack -=1
#             idx -=2
    

# DFS()

# print(max_score)
## DFS는 시간초과 

#계단 계수는 300

value = 0