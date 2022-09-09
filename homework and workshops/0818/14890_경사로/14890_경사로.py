# 2300_기지국 풀이
# 2022-08-18

import sys
sys.stdin = open('input.txt','r')

N, L = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(N)]
road = 0

# 가로검정
global c
c = 0

for i in range(N):
    
    for j in range(N-1):
        used = [0]*N

        if abs(map[i][j] - map[i][j+1]) > 1:
            break        
       
        else:
            if map[i][j] < map[i][j+1]:
                for k in range(L):
                    if j-k < 0 or used[k] or map[i][j] != map[i][j-k]:
                        break
                    else:
                        used[j-k] = True
                
            elif map[i][j] > map[i][j+1]:
                for k in range(L):
                    if j+k > N or used[k] or map[i][j] != map[i][j+k]:
                        break
                    else:
                        used[j+k] = True
                
    else:
        road += 1
        print(map[i])


        
        
        
print(road)