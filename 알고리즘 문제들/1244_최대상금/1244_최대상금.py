# 1244_최대상금 풀이
# 2022/09/22

import sys
sys.stdin = open("input.txt","r")

def dfs(idx, cnt):
    global answer
    if cnt == int(target):
        answer = max(int("".join(nums)), answer)
        return
    for now in range(idx, n):
        for max_idx in range(now + 1, n):
            if nums[now] <= nums[max_idx]:
                nums[now], nums[max_idx] = nums[max_idx], nums[now]
                print(nums)
                dfs(now, cnt + 1)
                nums[now], nums[max_idx] = nums[max_idx], nums[now]
    if not answer and cnt < int(target):
        rotate = (int(target) - cnt) % 2
        if rotate:
            nums[-1], nums[-2] = nums[-2], nums[-1]
        dfs(idx, int(target))


for test in range(1, int(input()) + 1):
    nums, target = input().split()
    n = len(nums)
    nums = list(nums)
    answer = 0
    dfs(0, 0)
    print(f'#{test} {answer}')


# 그리디로 풀려고 했지만 완전탐색이 더 일반적인 풀이방법인 듯 하여 변경함.
# 베낌... 내 풀이 조금이라도 남기려고 하면 다 틀어진다.
