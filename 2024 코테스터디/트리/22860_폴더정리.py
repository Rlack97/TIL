import sys
from collections import defaultdict

sys.setrecursionlimit(10000)

input = sys.stdin.readline

N, M = map(int, input().split())
folders = defaultdict(list)
files = defaultdict(list)

for _ in range(N + M):
    P, F, C = map(str, input().rstrip().split())

    if C == "0":  # 자식 요소가 파일
        files[P].append(F)

    else:  # 자식 요소가 폴더
        folders[P].append((F))


Q = int(input())


for _ in range(Q):
    file_route = list(map(str, input().rstrip().split("/")))
    final_route = file_route[-1]

    files_var = set()
    file_count = 0

    def dfs(n):
        global file_count, files_var

        for item in files[n]:
            file_count += 1
            files_var.add(item)

        for item in folders[n]:
            dfs(item)

    dfs(final_route)

    print(len(files_var), file_count)
