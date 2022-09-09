# 1220_magnetic 풀이
# 2022-08-19

import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, 11):
    one_length = int(input())
    magnet_field = [list(map(int, input().split())) for _ in range(100)]
    # 1이 빨강, 2가 파랑
    # 교착 상태의 갯수를 반환, 스택 사용
    lock = 0
    for i in range(100):
        magnet_stack = []
        for j in range(100):
            if magnet_field[j][i] != 0:
                # 세로탐색, 해당 위치에 자성체가 있을 때
                if magnet_stack:
                    if magnet_field[j][i] == 2 and magnet_stack[-1] == 1:
                        # 방향이 맞는 자성체가 인접해있다면
                        lock += 1
                        # 교착상태 +1
                        magnet_stack = []
                        # pop으로 지워주면 교착상태가 늘어나므로 스택 초기화
                    else:
                        magnet_stack.append(magnet_field[j][i])
                else:
                    magnet_stack.append(magnet_field[j][i])
                        # 자성체의 종류 기록

    print('#{} {}'.format(tc, lock))

