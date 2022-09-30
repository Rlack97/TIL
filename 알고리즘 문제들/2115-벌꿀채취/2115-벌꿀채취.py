# 2115-벌꿀채취 풀이
# 2022/09/29
# DFS

import sys
sys.stdin = open('input.txt','r')

def cal_profit(visited, worker_num):
    global answer

    if worker_num == 2:
        flist = [[] for _ in range(2)]
        for w in range(2):
            # 각 일꾼에 대하여 계산
            arr=[]
            maxv = 0
            for i in range(1<<M):
                subset=[]
                for j in range(M):
                    if i & (1<<j):
                        subset.append(worker[w][j])
                arr.append(subset)
            # 비트 연산을 통한 부분집합 구하기

            for a in arr:
                if sum(a) <= C:
                    suma = 0
                    for aa in a:
                        suma += aa**2
                        # 해당 부분집합의 이익을 저장
                    if suma > maxv:
                        maxv=suma
                        flist[w] = a  
                        # 최댓값보다 큰 것만 갱신 후 저장
        
        maxP = 0
        for f in flist:
            for s in f:
                maxP += s**2

        if maxP > answer:
            answer = maxP
        return
        # 저장된 최대 이익을 계산하고 리턴
        
    
    for i in range(N):
        for j in range(N-M+1):
            # M만큼의 가로길이를 가지는 탐색이므로 가로 범위 탐색을 해당 영역만큼 제외
            flag = 0

            for q in range(M):
                if visited[i][j+q] == 1:
                    flag = 1
            if flag !=0:
                continue
            # 탐색부부터 M길이 내부에 visited가 활성화되어 있으면 다음 지점 탐색

            for t in range(M):
                visited[i][j+t] = 1
                worker[worker_num].append(honeys[i][j+t])
                # 탐색 처리 후 꿀 값을 저장


            cal_profit(visited, worker_num+1)
            # 다음 노동자로 재귀

            for t in range(M):
                visited[i][j+t] = 0
                # 탐색 처리 해제

            worker[worker_num] = []
            # 저장된 꿀 값 해제
        
    


T = int(input())

for tc in range(1,T+1):
    N, M, C = map(int,input().split())
    # 선택할 수 있는 벌통의 개수 M, 채취할 수 있는 최대 양 C
    honeys = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    worker = [[] for _ in range(2)]

    answer = 0
    cal_profit(visited,0)
    print('#{} {}'.format(tc,answer))