import sys
input = sys.stdin.readline

N,K,L = map(int,input().split())
hambugers = sorted(list(map(int,input().split())))
cola_time = list(map(int,input().split()))
cola_list = [0] * N
# i번째 콜라는 cola_time[i] 번째 햄버거 직전에 마신다

total = 0

for c in cola_time:
  cola_list[c-1] += 1
  if c-1 + L < N:
    cola_list[c-1+L] -= 1

# 가장 많이 중첩된 콜라 효과
max_cola = cola_list[0]

for i in range(1,N):
  cola_list[i] += cola_list[i-1]
  max_cola = max(max_cola, cola_list[i])

cola_list.sort()

# 콜라 햄버거 모두 오름차순으로 정렬
p = [1] * (max_cola + 1)
for i in range(1, max_cola + 1):
    p[i] = 2 * p[i - 1]


for i in range(N):
    total += hambugers[i] // p[cola_list[i]]

print(total)

# 햄버거를 다 먹기 위한 위의 용량의 최솟값
