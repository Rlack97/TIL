# 5248_그룹 나누기 풀이
# 2022/09/29

import sys
sys.stdin = open("input.txt","r")

def prime_of_set(a):
    global conjoined

    if a == conjoined[a]:
        return a
    return prime_of_set(conjoined[a])

    # 각 그룹의 대표값(루트값)을 알아내는 함수


T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    submits = list(map(int,input().split()))
    conjoined = [i for i in range(N+1)]
    # 자기 자신을 가리키는 리스트 형성


    for i in range(0,M*2,2):
        if prime_of_set(submits[i]) != prime_of_set (submits[i+1]):
            # 입력된 수 끼리의 대표값이 같지 않을 경우

            conjoined[prime_of_set (submits[i+1])] = prime_of_set(submits[i])
            # 뒤의 입력값의 대표값을 앞의 입력값의 대표값으로 변경
            
    root = set()
    for i in range(1,N+1):
        root.add(prime_of_set(i))
        # 모든 수들의 대표값을 set으로 합침

    answer = len(root)
    # 중복값이 제거되었으므로 루트값의 종류, 즉 그룹의 수가 나옴

    print('#{} {}'.format(tc, answer))