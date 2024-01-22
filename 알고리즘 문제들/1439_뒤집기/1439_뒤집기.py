# 1859_백만장자_프로젝트 풀이
# 2023-08-22

zero = 0
one = 0

S = str(input())

for s in range(len(S)-1):
    if S[s] == '0' and S[s+1] == '1':
        zero += 1
    if S[s] == '1' and S[s+1] == '0': 
        one += 1
    
if S[-1] == '0':
    zero += 1
else: 
    one += 1

if zero > one:
    print(one)
else:
    print(zero)

# 입력값이 int인지 str인지 의식하지 않아서 조건문이 작동하지 않았다.
# 두 값이 바뀌는 것을 기준으로 0 그룹과 1 그룹의 수를 세고, 더 작은 쪽의 수가 가장 작은 행동횟수가 된다.