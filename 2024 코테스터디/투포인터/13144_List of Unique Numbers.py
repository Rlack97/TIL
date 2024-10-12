import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

start, end = 0, 0
seen = set()
count = 0

while end < N:
    if numbers[end] not in seen:
        # 중복이 없으면 현재 end를 추가하고 윈도우 크기 계산
        seen.add(numbers[end])
        end += 1
        # 현재 윈도우의 크기만큼 경우의 수를 추가
        count += end - start
    else:
        # 중복이 있으면 start를 증가시키며 중복 제거
        seen.remove(numbers[start])
        start += 1


print(count)
