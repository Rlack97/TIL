import sys
input = sys.stdin.readline

N, S = map(int, input().split())
cars = list(map(int, input().split()))
fuel = list(map(int, input().split()))

# 왼쪽 및 오른쪽 포인터
l = r = S - 1

# 초기 지점으로부터 가능한 범위 설정
minl = cars[l] - fuel[l]
maxr = cars[r] + fuel[r]

while True:
    flag = False

    # 왼쪽으로의 확장 여부
    if l > 0 and cars[l - 1] >= minl: # 이동 가능 범위 안에 다른 차가 존재하면
        l -= 1
        minl = min(minl, cars[l] - fuel[l])
        maxr = max(maxr, cars[l] + fuel[l])
        flag = True

    # 오른쪽으로 확장 여부
    if r < N - 1 and cars[r + 1] <= maxr:
        r += 1
        minl = min(minl, cars[r] - fuel[r])
        maxr = max(maxr, cars[r] + fuel[r])
        flag = True

    # 어느 쪽으로도 이동할 수 없다면
    if not flag:
        break

# 획득한 범위의 차 번호 출력
print(*range(l + 1, r + 2))