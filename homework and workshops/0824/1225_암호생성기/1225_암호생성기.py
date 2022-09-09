# 1225_암호생성기 풀이
# 2022-08-24

import sys
sys.stdin = open('input.txt', 'r')

# 사이클을 순환하는 함수
def cycle(numlist):
    while True: 
        for i in range(1,6): # 빼주는 값은 1부터 5까지 바뀜
            if numlist[0]-i <= 0: # 맨 앞 값에서 i를 뺀 값이 0 이하이면 
                numlist.append(0) # 맨 뒤에 0을 넣고
                numlist.pop(0)    # 맨 앞을 제거한 후 리턴
                return numlist
            numlist.append(numlist[0]-i)  # 맨 앞의 값에서 i를 뺀 뒤 맨 뒤로 보냄
            numlist.pop(0)                # 맨 앞의 값을 제거

# pop(0)를 사용하지 않으면 리스트가 너무 길어짐.
    

for T in range(1,11):
    tc = int(input())
    data = list(map(int,input().split()))

    answer = cycle(data)
    print('#{} {} {} {} {} {} {} {} {}'.format(tc,*answer))