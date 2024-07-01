# 가방문제랑 같다고?

import sys
input = sys.stdin.readline
# n명중 k명
# 힘 a, 스피드 b
# 모두 a+b가 동일함 = x 
# x가 왜 필요하지? 
# a,b값을 다 볼 필요 없이 하나만 보면 나머지를 알 수 있음
n,k,x = map(int,input().split())
str_list = []
for _ in range(n):
    a, b = map(int,input().split())
    str_list.append(a)

str_list.sort()

#dp[i] = i명을 뽑았을 때의 힘의 합
dp = [set() for _ in range(k+1)]
dp[0] = 0

for s in str_list:
    # selected 명을 뽑았을 때 (거꾸로 )
    for selected in range(k,0,-1):
        # selected -1 명을 뽑았을 때의 힘의 합들 + 현재 힘
        for ss in dp[selected-1]:
            dp[selected].add(ss + s)

# k명 뽑았을때의 힘의 합 * (사람수 * 능력치의 합(이거 왜??))
print(max(i*(k*x) for i in dp[-1]))