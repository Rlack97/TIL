import sys
input = sys.stdin.readline

# 이중 for문으로 인한 시간초과
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     books = []
#     for _ in range(n):
#         books.append(str(input()))

#     flag = 0

#     for b in books:
#         l = len(b)
#         for bb in books:
#             l2 = len(bb)
#             if bb != b and l2 >= l:
#                 if bb[0:l-1] == b.rstrip():
#                     print('NO')
#                     flag = 1
#                     break
#         if flag == 1:
#             break
#     if flag == 0:
#         print('YES')


# 입력값을 정렬하면 일관성 없는 두 번호는 반드시 인접함.
T = int(input())
for _ in range(T):
    n = int(input())
    books = []
    for _ in range(n):
        books.append(str(input()).rstrip())
    books.sort()

    flag = 0
    for i in range(n-1):
        if books[i+1][:len(books[i])] == books[i]:
            print('NO')
            flag = 1
            break

    if flag == 0:
        print('YES')
