import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum = 0

# 모든 구간합이 M으로 나눠지는지 확인??? 시간초과가 날 것
# 한번의 누적합을 구할 때 나머지를 따로 뽑아서 저장
# 각 나머지 인덱스에서 2개의 수를 뽑아주면 나머지가 0인 구간을 구할 수 있다.
numRemainder = [0] * M

for i in range(N):
    sum += numbers[i]
    numRemainder[sum % M] += 1

result = numRemainder[0]

for i in numRemainder:
    result += i*(i-1)//2

# 그러니까... 누적합을 계산하면서 나머지가 0인 수 = M으로 나눠지는수
# i*(i-1)//2 식은 iC2 (i개 중 2개를 뽑는 조합)을 의미
# 나머지가 같은 구간 두 개(?)


print(result)
