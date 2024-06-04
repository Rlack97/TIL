# from collections import defaultdict
# import sys
# input = sys.stdin.readline

# # a가 수열에서 등장한 횟수 A
# # a의 오등큰수 = 오른쪽에 있으면서 등장한 횟수가 A보다 큰 수 중 가장 왼쪽에 있는 수(?)
# # 없으면 -1

# N = int(input())
# num_list = list(map(int, input().split()))
# count = defaultdict(int)
# for n in num_list:
#     count[n] += 1


# answer = []

# for n in range(N-1):
#     main = count[num_list[n]]
#     flag = False
#     for i in range(n+1, N):
#         if count[num_list[i]] > main:
#             answer.append(num_list[i])
#             flag = True
#             break

#     if flag == False:
#         answer.append(-1)
# answer.append(-1)

# for number in answer:
#     print(number, end=' ')


N = int(input())
seq = list(map(int, input().split()))

count = [0] * 1000001
stack = []
res = [-1] * N
for num in seq:
    count[num] += 1

for i in range(N):
    while stack and count[seq[stack[-1]]] < count[seq[i]]:

        res[stack.pop()] = seq[i]
    stack.append(i)

print(" ".join(map(str, res)))
