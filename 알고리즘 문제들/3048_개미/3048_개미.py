# 3048_개미 풀이
# 2022-08-28


N1, N2 = map(int,input().split())
N1list = list(str(input()))
N2list = list(str(input()))
T = int(input())

N1list = N1list[::-1]

basiclist = N1list + N2list
answerlist = N1list + N2list

for i in range(T):
    for i in range(N1+N2-1):
        if basiclist[i] in N1list and basiclist[i+1] in N2list:
            answerlist[i], answerlist[i+1] = answerlist[i+1], answerlist[i]


    basiclist = answerlist.copy()
    

answer = ''
for i in answerlist:
    answer += i 

print(answer)