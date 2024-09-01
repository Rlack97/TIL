import sys

input = sys.stdin.readline

N = int(input())
stack = []
pair_count = 0

heights = [int(input()) for _ in range(N)]

for height in heights:
    # 스택의 마지막 사람이 현재 사람보다 키가 작으면 쌍을 이룰 수 있음
    while stack and stack[-1][0] < height:
        pair_count += stack.pop()[1]

    # 스택의 마지막 사람이 현재 사람과 같은 키를 가진 사람이 있다면
    if stack and stack[-1][0] == height:
        count = stack.pop()[1]
        pair_count += count  # 같은 키를 가진 사람끼리 볼 수 있는 쌍의 수 추가
        if stack:
            pair_count += (
                1  # 같은 키를 가진 사람이 있는 경우 스택에 남아있는 사람과 볼 수 있음
            )
        stack.append((height, count + 1))

    else:
        if stack:
            pair_count += 1  # 스택에 남아있는 사람과 볼 수 있음

        stack.append((height, 1))


print(pair_count)
