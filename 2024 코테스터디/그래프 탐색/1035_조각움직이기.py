from itertools import combinations, permutations
from collections import deque

import sys
input = sys.stdin.readline

# 두 지점 사이의 이동거리 구하기
def calDist(A,B):
    return abs(A[0]-B[0])+abs(A[1]-B[1])

# 점끼리 연결되어 있는지 검증
def isConnect(nowL):
    visited=[[0]*5 for _ in range(5)]
    tempL=[[0]*5 for _ in range(5)]
    for r,c in nowL:
        tempL[r][c]=1
    visited[nowL[0][0]][nowL[0][1]]=1
    cntCon=1
    q=deque([[nowL[0][0],nowL[0][1]]])
    while(q):
        r,c=q.popleft()
        for k in range(4):
            tempR=r+dx[k]
            tempC=c+dy[k]
            if 0<=tempR<5 and 0<=tempC<5 and visited[tempR][tempC]==0 and tempL[tempR][tempC]==1:
                visited[tempR][tempC]=1
                q.append([tempR,tempC])
                cntCon+=1
    if cntCon==size:
        return True
    else:
        return False


board = [list(map(str,input().rstrip())) for _ in range(5)]

# 점들 위치 기록
loc = []
for i in range(5):
    for j in range(5):
        if board[i][j]=="*":
            loc.append([i,j])

size=len(loc)
comb=list(combinations([i for i in range(25)],size))
ans=1e9

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for numL in comb:
    # 번호->행렬
    nowLoc=[]
    for i in numL:
        r=i//5
        c=i%5
        nowLoc.append([r,c])

    # 연결여부확인
    if not isConnect(nowLoc):
        continue

    # 거리확인
    nowAns=1e9
    per=list(permutations([i for i in range(size)],size))
    for myTuple in per:
        temp=0
        for i in range(size):
            temp+=calDist(loc[i],nowLoc[myTuple[i]])
        if temp<nowAns:
            nowAns=temp

    if nowAns<ans:
        ans=nowAns

print(ans)