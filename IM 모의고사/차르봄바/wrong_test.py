import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, P = map(int, input().split())
    virus = [list(map(int, input().split())) for _ in range(N)]
    # 바이러스 수가 기록된 행렬을 받아옵니다.

    max_terminated = 0
    # 합들을 따로 구한 뒤에 리스트 내부의 최댓값을 찾아도 되지만, 실행시간 절약을 위해
    # 새로운 최댓값이 나올 때마다 갱신하는 로직을 사용

    for i in range(N):
        for j in range(N):
            # N x N 행렬 내부 좌표 i,j에게 각각 계산

            # 1. 가로 세로 범위
            summed = 0
            # 가로세로 합을 담을 변수 초기화

            for k in range(P+1):
                # P번째의 칸까지 포함해야 하므로 범위를 P+1로 계산
                if i + k < N:
                    summed += virus[i + k][j]
                    # 아랫부분 인덱스 영역 유무 확인 후 더하기
                if j + k < N:
                    summed += virus[i][j + k]
                    # 오른쪽 인덱스 영역 유무 확인 후 더하기
                if i - k >= 0:
                    summed += virus[i - k][j]
                    # 윗부분 인덱스 영역 유무 확인 후 더하기
                if j - k >= 0:
                    summed += virus[i][j - k]
                    # 왼쪽 인덱스 영역 유무 확인 후 더하기
            summed -= virus[i][j] * 3
            # k = 0일때 자기 자신을 4번 더하므로 3개를 빼 줘야 함

            if summed > max_terminated:
                max_terminated = summed
                # 이 합이 합의 최댓값 변수보다 클 경우 그 값을 최댓값으로 간주

            # 2. 대각선 범위
            cross_sum = 0
            for t in range(P+1):
                if i + t < N and j + t < N:
                    cross_sum += virus[i + t][j + t]
                if i + t < N and j - t >= 0:
                    cross_sum += virus[i + t][j - t]
                if i - t >= 0 and j - t >= 0:
                    cross_sum += virus[i - t][j - t]
                if i - t >= 0 and j + t < N:
                    cross_sum += virus[i - t][j + t]
            cross_sum -= virus[i][j] * 3

            if cross_sum > max_terminated:
                max_terminated = cross_sum
                # 가로세로와 동일한 방식으로 계산

    print('#'+str(tc)+' '+str(max_terminated))
    # print 시 포맷을 사용하지 않으면 내부 요소는 전부 같은 타입이어야 하므로
    # str로 통일해 줌.