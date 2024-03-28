# 1644

import sys
input = sys.stdin.readline


# N 이하의 소수 리스트를 구하는 함수
# 시간초과 이슈
# def prime_list(N):
#     primes = []
#     for num in range(2, N+1):
#         if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
#             primes.append(num)
#     return primes

# 에라토스테네스의 체


def eratos(N):
    configure_prime = [False, False] + [True] * (N-1)
    primes = []
    for i in range(2, N+1):
        # 특정한 값 i가 참 (소수)라면
        if configure_prime[i]:
            # 소수 리스트에 넣어주고
            primes.append(i)
            # i의 모든 배수는 소수가 아니라고 기록
            for j in range(2*i, N+1, i):
                configure_prime[j] = False
    return primes


N = int(input())
answer = 0
under_n = eratos(N)
left = 0
right = 0
while -1 < left <= right < len(under_n):
    # 투 포인터 내부의 연속된 소수들의 합
    in_range = sum(under_n[left:right+1])

    # 합이 N과 같을 때 = 횟수 추가
    if in_range == N:
        answer += 1
        left += 1
        right += 1

    # 이 합이 N보다 작음 => 범위 증가 (값 증가)
    if in_range < N:
        right += 1

    # 이 합이 N보다 큼 => 범위 감소 (값 감소)
    elif in_range > N:
        left += 1

print(answer)
