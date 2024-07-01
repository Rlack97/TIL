import sys
input = sys.stdin.readline

N = int(input())
liquids = sorted(list(map(int, input().split())))
res = 4000000000 # 임의의 max값
container = []

# 두 포인터를 제외한 나머지 N-2개 값에 대하여
for i in range(N-2):
    xman = liquids[i]
    l = i+1
    r = N-1

    while l < r:
        tmp = xman + liquids[l] + liquids[r]

        # 기록보다 작은 값이 나올 시 좌표기록
        if abs(tmp) <= abs(res):
            container = [xman, liquids[l], liquids[r]]
            res = tmp
            
        # 합이 음수면 왼쪽 포인터 진행 (음수값이 작아짐)
        if tmp < 0:
            l += 1
        # 양수면 오른쪽 포인터 진행 (양수값이 작아짐)
        elif tmp > 0:
            r -= 1
        # 세 개의 합이 0일 경우 거기서 끝
        else:
            print(*container)
            sys.exit()

print(*container)