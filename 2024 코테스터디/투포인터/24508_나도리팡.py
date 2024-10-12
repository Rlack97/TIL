import sys

input = sys.stdin.readline
N, K, T = map(int, input().split())
# 바구니 수, 터지는 기준, 옮기는 횟수
nadori = list(map(int, input().split()))
# 오름차순 정렬
nadori.sort()

start = 0
end = N - 1
d = 0

# 0인 바구니는 건너뛴다
while start < N and nadori[start] == 0:
    start += 1
    d += 1

while start <= end:
    # 포인터가 같은 위치에 있으면 해당 위치 체크 후 종료
    if start == end:
        if nadori[start] >= K:
            d += 1
        break

    # end 위치 바구니가 K에 도달하기 위해 필요한 수
    need = K - nadori[end]

    # 필요한 만큼 이동할 수 없으면 종료
    if T < need:
        break

    # start의 갯수에 따라 다르게 작동
    if nadori[start] == need:
        T -= need
        end -= 1
        start += 1
        d += 2

    elif nadori[start] > need:
        nadori[start] -= need
        T -= need
        end -= 1
        d += 1

    elif nadori[start] < need:
        nadori[end] += nadori[start]
        T -= nadori[start]
        start += 1
        d += 1

    # 이동횟수 부족 시 종료
    if T <= 0:
        break

if d >= N:
    print("YES")
else:
    print("NO")
