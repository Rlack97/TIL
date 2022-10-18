# 4008_숫자 만들기 풀이
# 2022-10-14

import math

def calculation(list1,list2):
    global answer,idx, S, M

    if list2 == [0,0,0,0]:
        if answer < S:
            S = answer
        
        if answer > M:
            M = answer
        

        return None

    else:
        for i in range(4):
            if i == 0 and list2[i] !=0 :
                answer += list1[idx]
                idx += 1
                list2[i] -= 1
                calculation(list1,list2)
                idx -= 1
                answer -= list1[idx]
                list2[i] += 1

            elif i == 1 and list2[i] !=0 :
                answer -= list1[idx]
                idx += 1
                list2[i] -= 1
                calculation(list1,list2)
                idx -= 1
                answer += list1[idx]
                list2[i] += 1

            elif i == 2 and list2[i] !=0 :
                answer = answer*list1[idx]
                idx += 1
                list2[i] -= 1
                calculation(list1,list2)
                idx -= 1
                answer = answer/list1[idx]
                list2[i] += 1

            elif i == 3 and list2[i] !=0 :
                temp = answer
                answer = math.trunc(answer/list1[idx])
                idx += 1
                list2[i] -= 1
                calculation(list1,list2)
                idx -= 1
                answer = temp
                list2[i] += 1
            
        


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    symbols = list(map(int,input().split()))
    numbers = list(map(int,input().split()))
    idx = 1
    answer = numbers[0]
    S = 100000000
    M = -100000000
    calculation(numbers,symbols)
    print('#{} {}'.format(tc, round(M-S)))