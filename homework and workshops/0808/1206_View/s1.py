# 1206_View 풀이
# 2022-08-08 
# 정답코드
import sys
sys.stdin = open('input.txt','r')

for tc in range(1,11):          # testcase 10개
    T = int(input())
    Z = list(map(int,input().split()))
    answer = 0

    for i in range(2, T-2):
        K = [Z[i-2],Z[i-1],Z[i],Z[i+1],Z[i+2]]
			  # 조망권 확인을 위한 5칸짜리 영역을 가져옴

        for s in range(4, 0, -1):
            for j in range(0, s):
                if K[j] > K[j + 1]:
                    K[j], K[j + 1] = K[j + 1], K[j]
        # 5개 영역 안에서의 버블소팅을 진행

        if Z[i] == K[4] and K[4] != K[3]:  
        # 중앙값이 가장 높고, 중복값이 없어야 조망권이 형성되므로 이를 확인

            answer += Z[i]-K[3]
        # 주위 2칸 내의 가장 높은 값을 빼 주면 조망권이 확보된 구역의 값이 나오기 때문에 더해줌.
            
    print(f'#{tc} {answer}')
        #결과를 출력