# 2491_수열 풀이
# 2022-08-28


N = int(input())
numlist = list(map(int,input().split()))

downtrack = 1
uptrack = 1
maxtrack = 0

for n in range(N-1):
    if numlist[n] <= numlist[n+1]:
        uptrack += 1
        if uptrack > maxtrack:
            maxtrack = uptrack
    else:
        uptrack = 1

for n in range(N-1):
    if numlist[n] >= numlist[n+1]:
        downtrack += 1
        if downtrack > maxtrack:
            maxtrack = downtrack
    else:
        downtrack = 1

print(maxtrack)