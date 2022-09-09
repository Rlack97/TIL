# 연습문제3_DFS구현풀이
# 2022-08-12


adjlist = [[0],
[2,3],
[1,4,5],
[1,7],
[2,6],
[2,6],
[4,5,7],
[3,6]]

# 제시된 그래프의 인접리스트


def dfs(v):
    visited = [0]*8
    stack = [0]*8
    top = -1
    print(-v,end='')    
    # 방문리스트와 정점 스택 초기화
    # 시작 지점 출력
    visited [v] = 1
    while True:
        for w in adjlist[v]:
            if visited[w] == 0:
                top +=1
                stack[top] = v        # 스택에 v를 기록
                v = w
                visited[v] = 1        # w에 방문 후 기록 
                print(-v,end='')      # 방문 지점 출력
                break

        else:                    # w가 없는 경우
            if top != -1:        # 스택이 비어있지 않으면
                v = stack[top]
                top -= 1         # pop()
            else:               
                break
            
                
dfs(1)