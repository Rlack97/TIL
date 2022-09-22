# 5202_화물도크 풀이
# 2022/09/22

import sys
sys.stdin = open("input.txt","r")


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    total_workout = []
    last_end = 0
    # 마지막 작업이 끝난 시간

    cnt = 0
    # 이용한 화물차 댓수

    for _ in range(N):
        s, e = map(int,input().split())
        total_workout.append((s, e))
        # 작업시간 입력

    total_workout.sort(key=lambda x: (x[0], x[1]))
    # 시작 시간을 기준으로 오름차순 정렬, 만약 시작 시간이 같다면 종료시간으로도 정렬

    for i in range(N):
        end_times = []
        for j in range(i,N):
            if total_workout[j][0] >= last_end:
                end_times.append(total_workout[j])
                # 자신보다 시작시간이 늦은 모든 값들에 대하여
                # 자신의 종료시간보다 시작시간이 느린 값들의 리스트 생성

        if end_times:
            end_times.sort(key=lambda x: x[1])
            last_end = end_times[0][1]
            # 그 값들 중 종료시간이 가장 빠른(작은) 값을 선택하고, 마지막 작업 종료시간 갱신
            cnt += 1
            # 이용 댓수 +1

    answer = cnt
    print('#{} {}'.format(tc, answer))
